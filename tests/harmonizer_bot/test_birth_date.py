from datetime import date
from unittest import TestCase

from harmonizer_bot.birth_date import Birthday


class BirthdayTestCase(TestCase):
    def test_to_year(self):
        birthday = Birthday(7, 2)
        actual = birthday.to_date(2022)

        self.assertEqual(actual, date(2022, 7, 2))
