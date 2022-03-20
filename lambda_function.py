import os
from datetime import date, datetime, timedelta, timezone

from requests_oauthlib import OAuth1Session

JST = timezone(timedelta(hours=9), "JST")
AINOUTA_DAY = date(2021, 10, 29)

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


def generate_text():
    today = datetime.now(JST).date()
    passed_td = calculate_passed_timedelta(today)
    text = f"{today:%-m/%-d}は #アイの歌声を聴かせて 公開から{passed_days(passed_td)}日目です。\n"
    return text + "今日も、元気で、頑張るぞっ、おーっ"


def tweet(text):
    payload = {"text": text}
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    if response.status_code != 201:
        raise Exception(f"[Error] {response.status_code} {response.text}")


def lambda_handler(event, context):
    text = generate_text()
    tweet(text)


if __name__ == "__main__":
    lambda_handler(None, None)
