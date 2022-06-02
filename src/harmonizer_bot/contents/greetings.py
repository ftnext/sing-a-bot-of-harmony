from datetime import date

from sparkling_counter import DayCountDown, XthDayCount

from .base import Content


class MorningGreetingContent(Content):
    AINOUTA_XDAY_COUNT = XthDayCount(date(2021, 10, 29))

    DISK_RELEASE_DAY = date(2022, 7, 27)
    # 7/26であと1日になってほしい（翌日にはリリース）
    DISK_RELEASE_COUNT = DayCountDown(DISK_RELEASE_DAY, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            f"{self._date:%-m/%-d}は #アイの歌声を聴かせて 公開🎬から"
            f"{self.AINOUTA_XDAY_COUNT(self._date)}日目です。\n"
        )
        text += (
            "Blu-ray&DVDリリース📀まで今日を含めて"
            f"あと{self.DISK_RELEASE_COUNT(self._date)}日です"
            f"({self.DISK_RELEASE_DAY:%-m/%-d}発売。現在予約期間)。\n\n"
        )
        return text + "今日も、元気で、頑張るぞっ、おーっ"
