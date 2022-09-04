from datetime import date

from harmonizer_bot.blocks import NEW_LINE, Balloon, Sentence, Sentences

from .base import Content


class FroovieWholeGoodsContent(Content):
    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence(f"{self._date:%Y/%m/%d}の #アイの歌声を聴かせて グッズ情報📣"),
            Sentence("松竹の映画・アニメグッズ通販サイトFroovieさんにて、関連グッズ販売中！"),
            Sentence("https://froovie.jp/shop/c/cainouta/"),
            NEW_LINE,
            Balloon("ステキなグッズを届けます。"),
        )
        return sentences.format()
