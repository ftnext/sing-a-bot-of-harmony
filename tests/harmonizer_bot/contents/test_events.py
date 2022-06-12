from datetime import date

from harmonizer_bot.contents.events import PlayAllTogetherContent

from .support import ContentTestCase


class PlayAllTogetherContentTestCase(ContentTestCase):
    target_class = PlayAllTogetherContent
    generation_date = date(2022, 6, 16)
    generated_content = """
    #アイの歌声を聴かせて 期間限定配信🎥は終了。
    で・す・が、6/10(金)のTwitterスペース #みんなでアイうた が楽しめます（1週間程度とのことなので、今日を含めてあと2日くらい）。

    公式先輩、ありがとうございます❤️
    もう一度ラジオを聴かせて！
    https://twitter.com/ainouta_movie/status/1535260028474896384
    """
