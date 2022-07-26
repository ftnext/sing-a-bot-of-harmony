from datetime import date

from harmonizer_bot.contents.greetings import MorningGreetingContent

from .support import ContentTestCase


class MorningGreetingContentTestCase(ContentTestCase):
    target_class = MorningGreetingContent
    generation_date = date(2022, 7, 28)
    generated_content = """
    7/28は #アイの歌声を聴かせて 公開🎬から273日目、
    Blu-ray&DVDリリース📀&レンタル配信開始から2日目です。

    今日も、元気で、頑張るぞっ、おーっ
    """
