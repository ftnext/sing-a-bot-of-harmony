from datetime import date

from sparkling_counter import DayCountDown
from sparkling_counter.core import IllegalDayCountError

from .base import Content


class Nagoya109CinemasContent(Content):
    RUN_1ST = date(2022, 5, 28)
    UNTIL_RUN_1ST = DayCountDown(RUN_1ST, include=False)
    RUN_2ND = date(2022, 5, 31)
    UNTIL_RUN_2ND = DayCountDown(RUN_2ND, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        try:
            days_to_1st_run = self.UNTIL_RUN_1ST(self._date)
        except IllegalDayCountError:
            rest_to_1st_run = ""
        else:
            rest_to_1st_run = f" （あと{days_to_1st_run}日！）"

        rest_to_2nd_run = (
            f" （あと{self.UNTIL_RUN_2ND(self._date)}日"
            f"{'' if rest_to_1st_run else '！'}）"
        )

        text = "#アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！\n\n"
        text += f"- 5/28(土) 16:30〜{rest_to_1st_run}\n"
        text += f"- 5/31(火) 16:35〜{rest_to_2nd_run}\n\n"
        text += "チケット発売中！🎫\n"
        text += "詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！"
        return text
