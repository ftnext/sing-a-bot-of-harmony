from __future__ import annotations

import os
import random
from datetime import date, datetime
from random import randint
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from requests_oauthlib import OAuth1Session

from harmonizer_bot.birth_date import MainCharacterBirthdayDispatcher
from harmonizer_bot.contents import (
    CinemaCityContent,
    HappyProjectContent,
    MorningGreetingContent,
    ShinjukuPiccadillyContent,
    ShowingTheatersContent,
    WowowBroadCastContent,
)
from harmonizer_bot.core import TextGenerator

if TYPE_CHECKING:
    from collections.abc import Mapping

ASIA_TOKYO = ZoneInfo("Asia/Tokyo")

consumer_key = os.getenv("TWITTER_API_KEY")
client_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_API_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_API_ACCESS_TOKEN_SECRET")

oauth = OAuth1Session(
    consumer_key, client_secret, access_token, access_token_secret
)

root_generator = TextGenerator()


def refer_slots(content_class, today):
    on_and_after_schedules = content_class.SCHEDULES.select_on_and_after(today)
    schedules_map = {
        schedule.date.to_date(): schedule
        for schedule in on_and_after_schedules
    }
    if schedule := schedules_map.get(today):
        return " & ".join(str(start_time) for start_time in schedule.slots)
    return ""


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
    candidates = [("立川", CinemaCityContent), ("新宿", ShinjukuPiccadillyContent)]
    slots = [
        f"{area} {start_times}"
        for area, content_class in candidates
        if (start_times := refer_slots(content_class, today))
    ]

    on_the_screen_day_count = MorningGreetingContent.AINOUTA_XDAY_COUNT(today)
    disk_and_stream_count = MorningGreetingContent.DISK_XDAY_COUNT(today)

    text = f"""\
{today:%-m/%-d}は #アイの歌声を聴かせて 公開🎬から{on_the_screen_day_count}日目、
本日は映画館での上映が{len(slots)}件（{'、'.join(slots)}）、
Blu-ray&DVD発売中📀
また各所で配信中です（発売&配信開始から{disk_and_stream_count}日目）

今日も、元気で、頑張るぞっ、おーっ
{random.choice(greetings)}"""
    return text


_ = root_generator.register("information")(ShowingTheatersContent)


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
            f"アイの歌声を聴かせて 非公式Botが{today:%Y/%-m/%-d(%a)}の午後2時をお伝えします🌈",
        ]
    )


theater_text_generator = TextGenerator()
_ = theater_text_generator.register("cinema_city")(CinemaCityContent)
_ = theater_text_generator.register("shinjuku_piccadilly")(
    ShinjukuPiccadillyContent
)
_ = theater_text_generator.register("wowow")(WowowBroadCastContent)


@root_generator.register("theater")
def generate_theater_text(today: date, /, *, theater: str, **kwargs) -> str:
    return theater_text_generator.generate(theater, date_=today)


@root_generator.register("birthday")
def count_down_birthday(today: date, /, **kwargs):
    content = MainCharacterBirthdayDispatcher().dispatch(today)
    return content.generate()


@root_generator.register("hinataka-project")
def happy_project_text(today: date, /, **kwargs):
    content = HappyProjectContent(today)
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
    project_parser = subparsers.add_parser("hinataka-project")

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
