from __future__ import annotations

import locale
import os
from abc import ABC, abstractmethod
from datetime import date, datetime
from random import randint
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from requests_oauthlib import OAuth1Session
from sparkling_counter import DayCountDown, XthDayCount

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


class Content(ABC):
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError


class WasedaShochikuContent(Content):
    START_DAY = date(2022, 5, 7)
    # 各劇場の上映開始の前日であと1日になってほしい
    COUNT_DOWN = DayCountDown(START_DAY, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            f"#アイの歌声を聴かせて 早稲田松竹さんで{self.START_DAY:%-m/%-d(%a)}から上映開始！"
            f"（今日を含めて{self.COUNT_DOWN(self._date)}日後）\n\n"
        )
        text += (
            "たたーん🎵 開映時間は\n"
            "- 5/7(土)・10(火)・13(金)が 13:00 / 17:45\n"
            "- 5/9(月)・12(木)が 12:25 / 16:35 / 20:45\n"
            "- 5/8(日)・11(水)は上映なし\n\n"
        )
        text += (
            "詳しくは "
            "http://wasedashochiku.co.jp/archives/schedule/19087#film2 をどうぞ！"
        )
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


THEATER_CONTENT_CLASSES = {
    "waseda-shochiku": WasedaShochikuContent,
    "cinema-neko": CinemaNekoContent,
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
    lambda_handler({}, {})
