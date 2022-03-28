import os
from datetime import date, datetime, timedelta, timezone

from requests_oauthlib import OAuth1Session

JST = timezone(timedelta(hours=9), "JST")
AINOUTA_DAY = date(2021, 10, 29)
STREAMING_LAST_DAY = date(2022, 6, 10)

consumer_key = os.getenv("TWITTER_API_KEY")
client_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_API_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_API_ACCESS_TOKEN_SECRET")

oauth = OAuth1Session(
    consumer_key, client_secret, access_token, access_token_secret
)


def passed_days(td: timedelta) -> int:
    return td.days + 1


def calculate_passed_timedelta(today: date) -> timedelta:
    return today - AINOUTA_DAY


def streaming_rest_days(the_day: date) -> int:
    # 6/10であと1日（その日が最後）になってほしい
    between_timedelta = STREAMING_LAST_DAY - the_day
    return between_timedelta.days + 1


def disk_rest_days(the_day: date) -> int:
    # 7/26であと1日になってほしい（翌日にはリリース）
    between_timedelta = date(2022, 7, 27) - the_day
    return between_timedelta.days


def generate_text():
    today = datetime.now(JST).date()
    passed_td = calculate_passed_timedelta(today)
    text = f"{today:%-m/%-d}は アイの歌声を聴かせて 公開🎬から{passed_days(passed_td)}日目です。\n"
    text += f"Blu-ray&DVDリリース📀まで今日を含めてあと{disk_rest_days(today)}日です(7/27発売。現在予約期間)。\n\n"
    return text + "今日も、元気で、頑張るぞっ、おーっ"


def generate_information_text():
    today = datetime.now(JST).date()
    text = "アイの歌声を聴かせて 劇場で上映中！🎬 https://eigakan.org/theaterpage/schedule.php?t=ainouta\n"
    text += f"期間限定配信🎥は今日を含めてあと{streaming_rest_days(today)}日です(6/10まで)。\n\n"
    text += "今夜はきれいなお月さまでしょうか？"
    return text


def tweet(text):
    payload = {"text": text}
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    if response.status_code != 201:
        raise Exception(f"[Error] {response.status_code} {response.text}")


def lambda_handler(event, context):
    print(event)
    mode = event.get("bot-mode")
    if mode == "information":
        text = generate_information_text()
        tweet(text)
        return
    text = generate_text()
    tweet(text)


if __name__ == "__main__":
    lambda_handler(None, None)
