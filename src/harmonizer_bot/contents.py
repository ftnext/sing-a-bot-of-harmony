from abc import ABC, abstractmethod
from datetime import date

from sparkling_counter import DayCountDown


class Content(ABC):
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError


class Nagoya109CinemasContent(Content):
    RESERVE_START = date(2022, 5, 13)
    UNTIL_RESERVE_START = DayCountDown(RESERVE_START, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = "#アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！\n\n"
        text += "- 5/28(土) 16:30〜\n"
        text += "- 5/31(火) 16:35〜\n\n"
        text += (
            f"チケットは、{self.UNTIL_RESERVE_START(self._date)}日後の"
            f"{self.RESERVE_START:%-m/%-d(%a)} 0時から発売！\n\n"
        )
        text += "詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！"
        return text
