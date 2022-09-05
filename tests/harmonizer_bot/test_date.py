from datetime import date
from unittest import TestCase

from harmonizer_bot.date import BirthDate


class BirthDateTestCase(TestCase):
    def test_can_create(self):
        self.assertIsInstance(BirthDate(2022, 6, 6), date)
