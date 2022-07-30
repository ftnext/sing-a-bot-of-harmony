from datetime import date

from harmonizer_bot.contents.events import (
    DiskReleaseFestivalContent,
    HappyProjectContent,
    PlayAllTogetherContent,
    PublishingLimitedTimeContent,
)

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


class PublishingLimitedTimeContentTestCase(ContentTestCase):
    target_class = PublishingLimitedTimeContent
    generation_date = date(2022, 7, 25)
    generated_content = """
    #アイの歌声を聴かせて 冒頭17分がYouTubeで期間限定公開中！
    Blu-ray&DVD発売、さらにレンタル配信開始する7/27(水)まで公開（今日を含めてあと2日）

    https://twitter.com/ainouta_movie/status/1548502758092931072
    """


class DiskReleaseFestivalContentTestCase(ContentTestCase):
    target_class = DiskReleaseFestivalContent
    generation_date = date(2022, 8, 2)
    generated_content = """
    #アイの歌声を聴かせて Blu-ray&DVD発売（さらにレンタル配信開始）記念の吉浦監督スペシャルトークイベントまであと4日！
    8月3日(水) 23時55分までフォームで質問募集中（今日を含めてあと2日！）

    https://twitter.com/animageplus/status/1552833151877058560
    """


class HappyProjectContentTestCase(ContentTestCase):
    target_class = HappyProjectContent
    generation_date = date(2022, 6, 18)
    generated_content = """
    先日の「みんなでアイうた」スペースで告知がありましたが、
    ヒナタカさんがアイの歌声を聴かせて関連の企画を進めていらっしゃるそうです！

    あと2日で発表予定！（6/20までの残り日数を数えています）
    https://twitter.com/HinatakaJeF/status/1535251286014427137
    """
