from __future__ import annotations

import os
import random
from datetime import date, datetime
from random import randint
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from requests_oauthlib import OAuth1Session
from sparkling_counter import DayCountDown

from harmonizer_bot.contents import (
    MorningGreetingContent,
    Nagoya109CinemasContent,
)
from harmonizer_bot.contents.birthday import ShionBirthdayContent
from harmonizer_bot.core import TextGenerator

if TYPE_CHECKING:
    from collections.abc import Mapping

ASIA_TOKYO = ZoneInfo("Asia/Tokyo")

STREAMING_LAST_DAY = date(2022, 6, 10)
# 6/10であと1日（その日が最後）になってほしい
STREAMING_PERIOD_COUNT = DayCountDown(STREAMING_LAST_DAY, include=True)

consumer_key = os.getenv("TWITTER_API_KEY")
client_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_API_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_API_ACCESS_TOKEN_SECRET")

oauth = OAuth1Session(
    consumer_key, client_secret, access_token, access_token_secret
)

root_generator = TextGenerator()


@root_generator.register("morning-greeting")
def generate_text(today: date, /, **kwargs) -> str:
    greetings = [
        "https://twitter.com/ainouta_movie/status/1455308673669029891",
        "https://twitter.com/ainouta_movie/status/1456033452499914767",
        "https://twitter.com/ainouta_movie/status/1456395834946465794",
        "https://twitter.com/ainouta_movie/status/1457483003983134721",
        "https://twitter.com/ainouta_movie/status/1457845393379577860",
        "https://twitter.com/ainouta_movie/status/1458207779118673920",
        "https://twitter.com/ainouta_movie/status/1458570163771555840",
        "https://twitter.com/ainouta_movie/status/1458932549925978112",
    ]
    content = MorningGreetingContent(today)
    text = content.generate()
    return text + f"\n{random.choice(greetings)}"


@root_generator.register("information")
def generate_information_text(today: date, /, **kwargs) -> str:
    text = (
        "#アイの歌声を聴かせて 期間限定配信🎥は"
        f"今日を含めてあと{STREAMING_PERIOD_COUNT(today)}日です"
        f"({STREAMING_LAST_DAY:%-m/%-d}まで)。\n\n"
    )
    text += "📣たたーん！ 6/10(金)20:30〜 Twitterスペースで #みんなでアイうた\n"
    text += "作品の感想やお気に入りのシーンなど公式先輩が募集中！詳しくは👇\n"
    text += "https://twitter.com/ainouta_movie/status/1533649254425968640"
    return text


SIGNAL_SCENE_PHRASES = [
    "👧🏻「😴」",  # index: -len(SIGNAL_SCENE_PHRASES)
    "👩🏻‍🔬「悟美」",
    "👩🏻‍🔬「さーとーみ」",
    "👧🏻「... 😳」",
    "👧🏻「えっ、いま何時？」",
    "👩🏻‍🔬「にぃじ」",  # index: -1
]


@root_generator.register("time-signal")
def generate_time_signal_text(today: date, /, **kwargs) -> str:
    index = randint(-len(SIGNAL_SCENE_PHRASES), -1)
    return "\n".join(
        SIGNAL_SCENE_PHRASES[index:]
        + [
            "",
            f"アイの歌声を聴かせて 非公式Botが{today:%-m/%-d}の午後2時をお伝えします🌈",
        ]
    )


theater_text_generator = TextGenerator()
Nagoya109CinemasContent = theater_text_generator.register("nagoya-109cinemas")(
    Nagoya109CinemasContent
)


@root_generator.register("theater")
def generate_theater_text(today: date, /, *, theater: str, **kwargs) -> str:
    return theater_text_generator.generate(theater, date_=today)


@root_generator.register("birthday")
def count_down_birthday(today: date, /, **kwargs):
    content = ShionBirthdayContent(today)
    return content.generate()


def tweet(text: str) -> None:
    payload = {"text": text}
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    if response.status_code != 201:
        raise Exception(f"[Error] {response.status_code} {response.text}")


def lambda_handler(event: Mapping, context: Mapping) -> None:
    print(event)
    mode = event.get("bot-mode")
    today = datetime.now(ASIA_TOKYO).date()
    text = root_generator.generate(
        mode, date_=today, theater=event.get("theater")
    )
    tweet(text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="bot_mode")

    morning_greeting_parser = subparsers.add_parser("morning-greeting")
    information_parser = subparsers.add_parser("information")
    time_signal_parser = subparsers.add_parser("time-signal")
    birthday_parser = subparsers.add_parser("birthday")

    theater_parser = subparsers.add_parser("theater")
    theater_parser.add_argument(
        "theater", choices=theater_text_generator.event_handlers
    )

    args = parser.parse_args()

    tweet = print  # NOQA: F811 (redefine for debug)

    event = {"bot-mode": args.bot_mode}
    if args.bot_mode == "theater":
        event["theater"] = args.theater
    lambda_handler(event, {})
