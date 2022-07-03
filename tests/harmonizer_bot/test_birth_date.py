from datetime import date
from unittest import TestCase

from harmonizer_bot.birth_date import Birthday, Birthdays, MainCharacter


class BirthdayTestCase(TestCase):
    def test_to_year(self):
        birthday = Birthday(7, 2)
        actual = birthday.to_date(2022)

        self.assertEqual(actual, date(2022, 7, 2))


class BirthdaysTestCase(TestCase):
    def setUp(self):
        self.birthdays = {
            MainCharacter.SHION: Birthday(6, 6),
            MainCharacter.AYA: Birthday(7, 8),
        }

    def test_next_character(self):
        sut = Birthdays(self.birthdays)
        actual = sut.next_character(date(2022, 6, 7))

        self.assertEqual(actual, MainCharacter.AYA)
