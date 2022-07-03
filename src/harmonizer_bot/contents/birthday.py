import random
from datetime import date

from sparkling_counter import DayCountDown

from harmonizer_bot.blocks import NEW_LINE, Sentence, Sentences

from .base import Content


class ShionBirthdayContent(Content):
    BIRTHDAY_COUNTER = DayCountDown(date(2022, 6, 6), include=False)
    PROFILE_LINKS = [
        "https://twitter.com/ainouta_movie/status/1440982253895446535",
        "https://twitter.com/ainouta_movie/status/1459355340886085634",
        "https://twitter.com/ainouta_movie/status/1470619559820283907",
    ]
    LINES = [
        "サトミ！ いま、幸せ？",
        "私が幸せにしてあげる！",
        "サトミを幸せにする方法、思い付いちゃった！",
        "秘密はね、最後に明かされるんだよ",
    ]

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = "#アイの歌声を聴かせて のキャラクターで次に誕生日を迎えるのは、シオン！\n"
        text += f"6/6まであと{self.BIRTHDAY_COUNTER(self._date)}日\n\n"
        text += "／\n"
        text += f" {random.choice(self.LINES)}\n"
        text += "＼\n"
        text += random.choice(self.PROFILE_LINKS)
        return text


class AyaBirthdayContent(Content):
    def __init__(self, birthday: date, date_: date) -> None:
        self._birthday = birthday
        self._date = date_

    def generate(self) -> str:
        count_down = DayCountDown(self._birthday, include=False)
        sentences = Sentences(
            Sentence("#アイの歌声を聴かせて のキャラクターで次に誕生日を迎えるのは、アヤ！"),
            Sentence(f"{self._birthday:%-m/%-d}まであと{count_down(self._date)}日"),
            NEW_LINE,
            Sentence(
                "https://twitter.com/ainouta_movie/status/1442413708462858244"
            ),
        )
        return sentences.format()
