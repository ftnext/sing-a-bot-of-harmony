from __future__ import annotations

import os
from datetime import date, datetime
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from requests_oauthlib import OAuth1Session
from sparkling_counter import DayCountDown, XthDayCount

if TYPE_CHECKING:
    from collections.abc import Mapping

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


def generate_time_signal_text(today: date) -> str:
    return "\n".join(
        [
            "👧🏻「えっ、いま何時？」",
            "👩🏻‍🔬「にぃじ」",
            "",
            f"アイの歌声を聴かせて 非公式Botが{today:%-m/%-d}の午後2時をお伝えします🌈",
        ]
    )


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
    text = generate_text(today)
    tweet(text)


if __name__ == "__main__":
    lambda_handler({}, {})