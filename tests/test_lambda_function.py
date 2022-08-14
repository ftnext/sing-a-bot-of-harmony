from datetime import date
from textwrap import dedent
from unittest import TestCase, skip
from unittest.mock import patch

from lambda_function import generate_text, generate_time_signal_text


class GenerateTextTestCase(TestCase):
    @skip("WIP implementing...")
    def test_greeting(self):
        expected = dedent(
            """\
            5/30は #アイの歌声を聴かせて 公開🎬から214日目です。
            Blu-ray&DVDリリース📀そしてレンタル配信開始まで、今日を含めてあと58日です(7/27発売。現在予約期間)。

            今日も、元気で、頑張るぞっ、おーっ
            """
        ).rstrip()

        actual = generate_text(date(2022, 5, 30))

        self.assertEqual(actual, expected)


class GenerateTimeSignalTextTestCase(TestCase):
    @patch("lambda_function.randint", return_value=-5)
    def test_time_signal(self, randint):
        expected = dedent(
            """\
            👩🏻‍🔬「悟美」
            👩🏻‍🔬「さーとーみ」
            👧🏻「... 😳」
            👧🏻「えっ、いま何時？」
            👩🏻‍🔬「にぃじ」

            アイの歌声を聴かせて 非公式Botが2021/10/30(土)の午後2時をお伝えします🌈
            """
        ).rstrip()

        actual = generate_time_signal_text(date(2021, 10, 30))

        self.assertEqual(actual, expected)
        randint.assert_called_once_with(-6, -1)
