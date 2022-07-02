from datetime import date
from unittest import TestCase

from harmonizer_bot.birth_date import Birthday, Birthdays, MainCharacter


class BirthdayTestCase(TestCase):
    def test_to_year(self):
        birthday = Birthday(7, 2)
        actual = birthday.to_date(2022)

        self.assertEqual(actual, date(2022, 7, 2))


class BirthdaysTestCase(TestCase):
    def test_next_birthday(self):
        birthdays = Birthdays(
            {
                MainCharacter.SHION: Birthday(6, 6),
                MainCharacter.AYA: Birthday(7, 8),
            }
        )
        actual = birthdays.next_from(date(2022, 6, 7))

        self.assertEqual(actual, MainCharacter.AYA)
