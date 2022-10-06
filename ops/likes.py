import argparse
import os

from requests_oauthlib import OAuth1Session

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tweet_id", nargs="+")
    args = parser.parse_args()

    consumer_key = os.getenv("TWITTER_API_KEY")
    client_secret = os.getenv("TWITTER_API_KEY_SECRET")
    access_token = os.getenv("TWITTER_API_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_API_ACCESS_TOKEN_SECRET")
    bot_id = os.getenv("TWITTER_BOT_SELF_ID")

    oauth = OAuth1Session(
        consumer_key, client_secret, access_token, access_token_secret
    )
    url = f"https://api.twitter.com/2/users/{bot_id}/likes"
    for tweet_id in args.tweet_id:
        response = oauth.post(url, json={"tweet_id": tweet_id})
        if response.status_code != 200:
            print(f"Failed at tweet {tweet_id}")
