from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.birthday import (
    AyaBirthdayContent,
    GocchanBirthdayContent,
    ShionBirthdayContent,
)
from harmonizer_bot.datetime import BirthDate


class ShionBirthdayContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = ShionBirthdayContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    @patch("harmonizer_bot.contents.birthday.random")
    def test_generate(self, random):
        random.choice.side_effect = (
            "私が幸せにしてあげる！",
            "https://twitter.com/ainouta_movie/status/1459355340886085634",
        )

        expected = dedent(
            """\
            #アイの歌声を聴かせて のキャラクターで次に誕生日を迎えるのは、シオン！
            6/6まであと1日

            ／
             私が幸せにしてあげる！
            ＼
            https://twitter.com/ainouta_movie/status/1459355340886085634
            """
        ).rstrip()

        content = ShionBirthdayContent(date(2022, 6, 5))
        actual = content.generate()

        self.assertEqual(actual, expected)
        # TODO: random.choice.assert_has_calls


class AyaBirthdayContentTestCase(TestCase):
    def test_init(self):
        birthday = MagicMock(spec=BirthDate)
        date_ = MagicMock(spec=date)

        actual = AyaBirthdayContent(birthday, date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._birthday, birthday)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて のキャラクターで次に誕生日を迎えるのは、アヤ！
            7/8まであと7日

            https://twitter.com/ainouta_movie/status/1442413708462858244
            """
        ).rstrip()

        content = AyaBirthdayContent(BirthDate(2022, 7, 8), date(2022, 7, 1))
        actual = content.generate()

        self.assertEqual(actual, expected)

    def test_generate_the_day(self):
        expected = dedent(
            """\
            本日7/8は #アイの歌声を聴かせて のキャラクター アヤの誕生日！
            たんじょうびー、おめでとう🎶

            さらに、本日22時より #吉浦康裕スペース 🎉
            https://twitter.com/yoshiura_rikka/status/1545029267758542848
            """
        ).rstrip()

        content = AyaBirthdayContent(BirthDate(2022, 7, 8), date(2022, 7, 8))
        actual = content.generate()

        self.assertEqual(actual, expected)


class GocchanBirthdayContentTestCase(TestCase):
    def test_init(self):
        birthday = MagicMock(spec=BirthDate)
        date_ = MagicMock(spec=date)

        actual = GocchanBirthdayContent(birthday, date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._birthday, birthday)
        self.assertEqual(actual._date, date_)

    @patch("harmonizer_bot.contents.birthday.random")
    def test_generate(self, random):
        random.choice.side_effect = (
            "すっげー自己紹介。おもしれーじゃん👏",
            "https://twitter.com/ainouta_movie/status/1442051320035172360",
        )
        expected = dedent(
            """\
            #アイの歌声を聴かせて のキャラクターで次に誕生日を迎えるのは、ゴッちゃん！
            11/20まであと3日

            ／
             すっげー自己紹介。おもしれーじゃん👏
            ＼
            https://twitter.com/ainouta_movie/status/1442051320035172360
            """
        ).rstrip()

        content = GocchanBirthdayContent(
            BirthDate(2022, 11, 20), date(2022, 11, 17)
        )
        actual = content.generate()

        self.assertEqual(actual, expected)
        random.choice.assert_has_calls(
            [
                call(GocchanBirthdayContent.LINES),
                call(GocchanBirthdayContent.PROFILE_LINKS),
            ]
        )
