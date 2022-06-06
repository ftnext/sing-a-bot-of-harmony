from datetime import date
from textwrap import dedent
from unittest import TestCase
from unittest.mock import MagicMock, patch

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.birthday import ShionBirthdayContent


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
