from datetime import date
from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.events import PlayAllTogetherContent


class PlayAllTogetherContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = PlayAllTogetherContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)
