from __future__ import annotations

import locale
import os
from datetime import date, datetime
from random import randint
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from requests_oauthlib import OAuth1Session
from sparkling_counter import DayCountDown, XthDayCount

from harmonizer_bot.contents import Content, Nagoya109CinemasContent

if TYPE_CHECKING:
    from collections.abc import Mapping

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

ASIA_TOKYO = ZoneInfo("Asia/Tokyo")

AINOUTA_XDAY_COUNT = XthDayCount(date(2021, 10, 29))

STREAMING_LAST_DAY = date(2022, 6, 10)
# 6/10であと1日（その日が最後）になってほしい
STREAMING_PERIOD_COUNT = DayCountDown(STREAMING_LAST_DAY, include=True)

DISK_RELEASE_DAY = date(2022, 7, 27)
# 7/26であと1日になってほしい（翌日にはリリース）
DISK_RELEASE_COUNT = DayCountDown(DISK_RELEASE_DAY, include=False)

consumer_key = os.getenv("TWITTER_API_KEY")
client_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_API_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_API_ACCESS_TOKEN_SECRET")

oauth = OAuth1Session(
    consumer_key, client_secret, access_token, access_token_secret
)


def generate_text(today: date) -> str:
    text = (
        f"{today:%-m/%-d}は #アイの歌声を聴かせて 公開🎬から{AINOUTA_XDAY_COUNT(today)}日目です。\n"
    )
    text += (
        f"Blu-ray&DVDリリース📀まで今日を含めてあと{DISK_RELEASE_COUNT(today)}日です"
        f"({DISK_RELEASE_DAY:%-m/%-d}発売。現在予約期間)。\n\n"
    )
    return text + "今日も、元気で、頑張るぞっ、おーっ"


def generate_information_text(today: date) -> str:
    text = (
        "アイの歌声を聴かせて 劇場で上映中！🎬 "
        "https://eigakan.org/theaterpage/schedule.php?t=ainouta\n"
    )
    text += (
        f"期間限定配信🎥は今日を含めてあと{STREAMING_PERIOD_COUNT(today)}日です"
        f"({STREAMING_LAST_DAY:%-m/%-d}まで)。\n\n"
    )
    text += "今夜はきれいなお月さまでしょうか？"
    return text


SIGNAL_SCENE_PHRASES = [
    "👧🏻「😴」",  # index: -len(SIGNAL_SCENE_PHRASES)
    "👩🏻‍🔬「悟美」",
    "👩🏻‍🔬「さーとーみ」",
    "👧🏻「... 😳」",
    "👧🏻「えっ、いま何時？」",
    "👩🏻‍🔬「にぃじ」",  # index: -1
]


def generate_time_signal_text(today: date) -> str:
    index = randint(-len(SIGNAL_SCENE_PHRASES), -1)
    return "\n".join(
        SIGNAL_SCENE_PHRASES[index:]
        + [
            "",
            f"アイの歌声を聴かせて 非公式Botが{today:%-m/%-d}の午後2時をお伝えします🌈",
        ]
    )


class WasedaShochikuContent(Content):
    LAST_DAY = date(2022, 5, 13)
    COUNT_DOWN = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            f"#アイの歌声を聴かせて 早稲田松竹さんで{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.COUNT_DOWN(self._date)}日）\n"
            "竜そば・サイコトと日替わり2️⃣本立て\n\n"
        )
        text += (
            "開映時間は\n"
            "- 5/7(土)・10(火)・13(金) 13:00 / 17:45\n"
            "- 5/9(月)・12(木) 12:25 / 16:35 / 20:45\n"
            "- 5/8(日)・11(水) 上映なし\n\n"
        )
        text += "詳しくは http://wasedashochiku.co.jp/archives/schedule/19087 をどうぞ"
        return text


class CinemaNekoContent(Content):
    START_DAY = date(2022, 4, 22)
    LAST_DAY = date(2022, 5, 15)
    END_COUNT = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 青梅のシネマネコさんで"
            f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.END_COUNT(self._date)}日）\n\n"
        )
        text += "たたーん🎵 上映時間は、毎日 15:40〜 （5/10(火)は定休日）\n"
        text += "詳しくは https://cinema-neko.com/movie_detail.php?id=94c58c03-e4b1-484d-8a0f-bc9bb885493c をどうぞ！\n\n"  # NOQA: E501
        text += "シネマネコさんのラッキープレイスはー、カフェ！☕️"
        return text


class SumotoOrionContent(Content):
    START_DAY = date(2022, 4, 29)
    LAST_DAY = date(2022, 5, 12)
    END_COUNT = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 淡路島の洲本オリオンさんで"
            f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.END_COUNT(self._date)}日）\n\n"
        )
        text += "たたーん🎵 上映時間は、毎日 15:30〜\n"
        text += "詳しくは https://www.sumoto-orion.com/?p=895 をどうぞ！"
        if self._add_yelling():
            text += "\n\n"
            text += "さらに水曜日・日曜日は 18:00〜 無発声応援上映追加！🤗"
        return text

    def _add_yelling(self):
        # 水曜(2)・日曜(6)と前日は無発生応援上映を追加する
        return self._date.weekday() in (1, 2, 5, 6)


THEATER_CONTENT_CLASSES = {
    "waseda-shochiku": WasedaShochikuContent,
    "cinema-neko": CinemaNekoContent,
    "sumoto-orion": SumotoOrionContent,
    "nagoya-109cinemas": Nagoya109CinemasContent,
}


def tweet(text: str) -> None:
    payload = {"text": text}
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    if response.status_code != 201:
        raise Exception(f"[Error] {response.status_code} {response.text}")


def lambda_handler(event: Mapping, context: Mapping) -> None:
    print(event)
    mode = event.get("bot-mode")
    today = datetime.now(ASIA_TOKYO).date()
    if mode == "information":
        text = generate_information_text(today)
        tweet(text)
        return
    elif mode == "time-signal":
        text = generate_time_signal_text(today)
        tweet(text)
        return
    elif mode == "theater":
        theater = event.get("theater")
        content_class = THEATER_CONTENT_CLASSES.get(theater)
        content = content_class(today)
        text = content.generate()
        tweet(text)
        return
    text = generate_text(today)
    tweet(text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="bot_mode")

    theater_parser = subparsers.add_parser("theater")
    theater_parser.add_argument("theater", choices=THEATER_CONTENT_CLASSES)

    args = parser.parse_args()

    tweet = print  # NOQA: F811 (redefine for debug)

    if args.bot_mode == "theater":
        lambda_handler({"bot-mode": "theater", "theater": args.theater}, {})
