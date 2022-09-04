from datetime import date

from harmonizer_bot.contents.goods import FroovieWholeGoodsContent

from .support import ContentTestCase


class FroovieWholeGoodsContentTestCase(ContentTestCase):
    target_class = FroovieWholeGoodsContent
    generation_date = date(2022, 9, 4)
    generated_content = """
    2022/09/04の #アイの歌声を聴かせて グッズ情報📣
    松竹の映画・アニメグッズ通販サイトFroovieさんにて、関連グッズ販売中！
    https://froovie.jp/shop/c/cainouta/

    ／
     ステキなグッズを届けます。
    ＼
    """
