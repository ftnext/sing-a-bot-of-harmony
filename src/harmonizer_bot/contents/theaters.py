from datetime import date

from sparkling_counter import DayCountDown
from sparkling_counter.core import IllegalDayCountError

from .base import Content


class WasedaShochikuContent(Content):
    LAST_DAY = date(2022, 5, 13)
    COUNT_DOWN = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            f"#アイの歌声を聴かせて 早稲田松竹さんで{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.COUNT_DOWN(self._date)}日）\n"
            "竜そば・サイコトと日替わり2️⃣本立て\n\n"
        )
        text += (
            "開映時間は\n"
            "- 5/7(土)・10(火)・13(金) 13:00 / 17:45\n"
            "- 5/9(月)・12(木) 12:25 / 16:35 / 20:45\n"
            "- 5/8(日)・11(水) 上映なし\n\n"
        )
        text += "詳しくは http://wasedashochiku.co.jp/archives/schedule/19087 をどうぞ"
        return text


class CinemaNekoContent(Content):
    START_DAY = date(2022, 4, 22)
    LAST_DAY = date(2022, 5, 15)
    END_COUNT = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 青梅のシネマネコさんで"
            f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.END_COUNT(self._date)}日）\n\n"
        )
        text += "たたーん🎵 上映時間は、毎日 15:40〜 （5/10(火)は定休日）\n"
        text += "詳しくは https://cinema-neko.com/movie_detail.php?id=94c58c03-e4b1-484d-8a0f-bc9bb885493c をどうぞ！\n\n"  # NOQA: E501
        text += "シネマネコさんのラッキープレイスはー、カフェ！☕️"
        return text


class SumotoOrionContent(Content):
    START_DAY = date(2022, 4, 29)
    LAST_DAY = date(2022, 5, 12)
    END_COUNT = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 淡路島の洲本オリオンさんで"
            f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.END_COUNT(self._date)}日）\n\n"
        )
        text += "たたーん🎵 上映時間は、毎日 15:30〜\n"
        text += "詳しくは https://www.sumoto-orion.com/?p=895 をどうぞ！"
        if self._add_yelling():
            text += "\n\n"
            text += "さらに水曜日・日曜日は 18:00〜 無発声応援上映追加！🤗"
        return text

    def _add_yelling(self):
        # 水曜(2)・日曜(6)と前日は無発生応援上映を追加する
        return self._date.weekday() in (1, 2, 5, 6)


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
        text += f"- {self.RUN_1ST:%-m/%-d(%a)} 16:30〜{rest_to_1st_run}\n"
        text += f"- {self.RUN_2ND:%-m/%-d(%a)} 16:35〜{rest_to_2nd_run}\n\n"
        text += "チケット発売中！🎫\n"
        text += "詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！"
        return text


class CinePipiaContent:
    ...
