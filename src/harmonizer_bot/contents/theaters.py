from datetime import date

from sparkling_counter import DayCountDown

from .base import Content


class Nagoya109CinemasContent(Content):
    RUN_1ST = date(2022, 5, 28)
    UNTIL_RUN_1ST = DayCountDown(RUN_1ST, include=False)
    RUN_2ND = date(2022, 5, 31)
    UNTIL_RUN_2ND = DayCountDown(RUN_2ND, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = "#アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！\n\n"
        text += f"- 5/28(土) 16:30〜 （あと{self.UNTIL_RUN_1ST(self._date)}日！）\n"
        text += f"- 5/31(火) 16:35〜 （あと{self.UNTIL_RUN_2ND(self._date)}日）\n\n"
        text += "チケット発売中！🎫\n"
        text += "詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！"
        return text
