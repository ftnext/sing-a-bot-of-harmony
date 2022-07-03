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
        parameters = [
            (date(2022, 6, 7), (MainCharacter.AYA, date(2022, 7, 8))),
            (date(2022, 7, 8), (MainCharacter.AYA, date(2022, 7, 8))),
            # Before all dates
            (date(2022, 6, 1), (MainCharacter.SHION, date(2022, 6, 6))),
            (date(2022, 6, 6), (MainCharacter.SHION, date(2022, 6, 6))),
            # After all dates
            (date(2022, 7, 22), (MainCharacter.SHION, date(2023, 6, 6))),
        ]
        sut = Birthdays(self.birthdays)
        for date_, expected in parameters:
            with self.subTest(date_=date_, expected=expected):
                actual = sut.next_character(date_)

                self.assertEqual(actual, expected)

    def test_next_character_unsorted(self):
        sut = Birthdays(
            {
                MainCharacter.AYA: Birthday(7, 8),
                MainCharacter.SHION: Birthday(6, 6),
            }
        )
        actual = sut.next_character(date(2022, 6, 7))

        self.assertEqual(actual, (MainCharacter.AYA, date(2022, 7, 8)))
