from datetime import date

from sparkling_counter import DayCountDown

from .base import Content


class PlayAllTogetherContent(Content):
    STREAMING_LAST_DAY = date(2022, 6, 10)
    # 6/10であと1日（その日が最後）になってほしい
    STREAMING_PERIOD_COUNT = DayCountDown(STREAMING_LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 期間限定配信🎥は"
            f"今日を含めてあと{self.STREAMING_PERIOD_COUNT(self._date)}日です"
            f"({self.STREAMING_LAST_DAY:%-m/%-d}まで)。\n\n"
        )
        text += "📣たたーん！ 6/10(金)20:30〜 Twitterスペースで #みんなでアイうた\n"
        text += "作品の感想やお気に入りのシーンなど公式先輩が募集中！詳しくは👇\n"
        text += "https://twitter.com/ainouta_movie/status/1533649254425968640"
        return text
