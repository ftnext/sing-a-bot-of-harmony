from datetime import date
from unittest import TestCase

from harmonizer_bot.date import BirthDate


class BirthDateTestCase(TestCase):
    def test_can_create(self):
        self.assertIsInstance(BirthDate(2022, 6, 6), date)

    def test_format_month_and_day(self):
        birth_date = BirthDate(2022, 4, 10)
        self.assertEqual(f"{birth_date}", "4/10")

    def test_convert_from_date(self):
        date_ = date(2022, 11, 20)
        self.assertEqual(BirthDate.from_(date_), BirthDate(2022, 11, 20))
