from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch

from lambda_function import (
    generate_information_text,
    generate_text,
    generate_time_signal_text,
)


class GenerateTextTestCase(TestCase):
    def test_greeting(self):
        expected = dedent(
            """\
            5/30は #アイの歌声を聴かせて 公開🎬から214日目です。
            Blu-ray&DVDリリース📀まで今日を含めてあと58日です(7/27発売。現在予約期間)。

            今日も、元気で、頑張るぞっ、おーっ
            """
        ).rstrip()

        actual = generate_text(date(2022, 5, 30))

        self.assertEqual(actual, expected)


class GenerateInformationTextTestCase(TestCase):
    def test_information(self):
        expected = dedent(
            """\
            アイの歌声を聴かせて 劇場で上映中！🎬 https://eigakan.org/theaterpage/schedule.php?t=ainouta
            期間限定配信🎥は今日を含めてあと13日です(6/10まで)。

            今夜はきれいなお月さまでしょうか？
            """
        ).rstrip()

        actual = generate_information_text(date(2022, 5, 29))

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

            アイの歌声を聴かせて 非公式Botが10/30の午後2時をお伝えします🌈
            """
        ).rstrip()

        actual = generate_time_signal_text(date(2021, 10, 30))

        self.assertEqual(actual, expected)
        randint.assert_called_once_with(-6, -1)
