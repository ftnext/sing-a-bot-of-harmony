from datetime import date, timedelta

from sparkling_counter import DayCountDown

from harmonizer_bot.blocks import NEW_LINE, Sentence, Sentences

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
            f"で・す・が、{self.STREAMING_LAST_DAY:%-m/%-d(%a)}の"
            "Twitterスペース #みんなでアイうた が楽しめます"
            "（1週間程度とのことなので、"
            f"今日を含めてあと{self.REPLAY_PERIOD_COUNT(self._date)}日くらい）。\n\n"
        )
        text += "公式先輩、ありがとうございます❤️\n"
        text += "もう一度ラジオを聴かせて！\n"
        text += "https://twitter.com/ainouta_movie/status/1535260028474896384"
        return text


class PublishingLimitedTimeContent(Content):
    LAST_DAY = date(2022, 7, 27)
    # 「7/27まで期間限定公開」だが7/27になった直後に見られない可能性が高くなった
    PUBLISHING_PERIOD_COUNT = DayCountDown(
        LAST_DAY + timedelta(days=-1), include=True
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence("#アイの歌声を聴かせて 冒頭17分がYouTubeで期間限定公開中！"),
            Sentence(
                f"Blu-ray&DVD発売、さらにレンタル配信開始する{self.LAST_DAY:%-m/%-d(%a)}まで公開"
                f"（今日を含めてあと{self.PUBLISHING_PERIOD_COUNT(self._date)}日）"
            ),
            NEW_LINE,
            Sentence(
                "https://twitter.com/ainouta_movie/status/1548502758092931072"
            ),
        )
        return sentences.format()


class DiskReleaseFestivalContent(Content):
    FESTIVAL_DAY = date(2022, 8, 6)
    FESTIVAL_COUNT = DayCountDown(FESTIVAL_DAY, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence(
                "#アイの歌声を聴かせて Blu-ray&DVD発売（さらにレンタル配信開始）記念の"
                f"吉浦監督スペシャルトークイベントまであと{self.FESTIVAL_COUNT(self._date)}日！"
            ),
            Sentence("イベントの配信チケット販売中！（「アーカイブは8/20 22:00まで購入可」とのこと）"),
            NEW_LINE,
            Sentence(
                "https://twitter.com/LOFTPLUSONE/status/1550390521314820096"
            ),
        )
        return sentences.format()


class HappyProjectContent(Content):
    ANNOUNCEMENT_DAY = date(2022, 6, 20)
    ANNOUNCEMENT_COUNT = DayCountDown(ANNOUNCEMENT_DAY, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = "先日の「みんなでアイうた」スペースで告知がありましたが、\n"
        text += "ヒナタカさんがアイの歌声を聴かせて関連の企画を進めていらっしゃるそうです！\n\n"
        text += (
            f"あと{self.ANNOUNCEMENT_COUNT(self._date)}日で発表予定！"
            f"（{self.ANNOUNCEMENT_DAY:%-m/%-d}までの残り日数を数えています）\n"
        )
        text += "https://twitter.com/HinatakaJeF/status/1535251286014427137"
        return text
