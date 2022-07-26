from datetime import date

from sparkling_counter import XthDayCount

from ..blocks import NEW_LINE, Sentence, Sentences
from .base import Content


class MorningGreetingContent(Content):
    AINOUTA_XDAY_COUNT = XthDayCount(date(2021, 10, 29))
    DISK_XDAY_COUNT = XthDayCount(date(2022, 7, 27))

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence(
                f"{self._date:%-m/%-d}は #アイの歌声を聴かせて 公開🎬から"
                f"{self.AINOUTA_XDAY_COUNT(self._date)}日目、"
            ),
            Sentence(
                "Blu-ray&DVDリリース📀&レンタル配信開始から"
                f"{self.DISK_XDAY_COUNT(self._date)}日目です。"
            ),
            NEW_LINE,
            Sentence("今日も、元気で、頑張るぞっ、おーっ"),
        )
        return sentences.format()
