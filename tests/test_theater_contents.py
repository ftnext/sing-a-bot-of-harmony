from datetime import date
from textwrap import dedent
from unittest import TestCase

from lambda_function import WasedaShochikuContent


class WasedaShochikuContentTestCase(TestCase):
    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 早稲田松竹さんで5/7から上映開始！（今日を含めてあと4日）

            たたーん🎵 開映時間は
            - 5/7(土)・10(火)・13(金)が 13:00 / 17:45
            - 5/9(月)・12(木)が 12:25 / 16:35 / 20:45
            - 5/8(日)・11(水)は上映なし

            詳しくは http://wasedashochiku.co.jp/archives/schedule/19087#film2 をどうぞ！
            """
        ).rstrip()

        content = WasedaShochikuContent(date(2022, 5, 3))
        actual = content.generate()

        self.assertEqual(actual, expected)
