from datetime import date

from sparkling_counter import DayCountDown

from .base import Content


class PlayAllTogetherContent(Content):
    STREAMING_LAST_DAY = date(2022, 6, 10)
    # 6/10であと1日（その日が最後）になってほしい
    STREAMING_PERIOD_COUNT = DayCountDown(STREAMING_LAST_DAY, include=True)
    RADIO_REPLAY_LAST_DAY = date(2022, 6, 17)
    REPLAY_PERIOD_COUNT = DayCountDown(RADIO_REPLAY_LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 期間限定配信🎥は終了。\n"
            "で・す・が、6/10(金)のTwitterスペース #みんなでアイうた が楽しめます"
            "（1週間程度とのことなので、"
            f"今日を含めてあと{self.REPLAY_PERIOD_COUNT(self._date)}日くらい）。\n\n"
        )
        text += "公式先輩、ありがとうございます❤️\n"
        text += "もう一度ラジオを聴かせて！\n"
        text += "https://twitter.com/ainouta_movie/status/1535260028474896384"
        return text
