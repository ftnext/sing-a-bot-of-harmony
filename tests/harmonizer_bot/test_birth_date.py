from datetime import date
from unittest import TestCase

from harmonizer_bot.birth_date import Birthday, Birthdays, MainCharacter
from harmonizer_bot.date import BirthDate


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
            (date(2022, 6, 7), (MainCharacter.AYA, BirthDate(2022, 7, 8))),
            (date(2022, 7, 8), (MainCharacter.AYA, BirthDate(2022, 7, 8))),
            # Before all dates
            (date(2022, 6, 1), (MainCharacter.SHION, BirthDate(2022, 6, 6))),
            (date(2022, 6, 6), (MainCharacter.SHION, BirthDate(2022, 6, 6))),
            # After all dates
            (date(2022, 7, 22), (MainCharacter.SHION, BirthDate(2023, 6, 6))),
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

        self.assertEqual(actual, (MainCharacter.AYA, BirthDate(2022, 7, 8)))

    def test_next_character_added(self):
        sut = Birthdays(
            {**self.birthdays, MainCharacter.GOCCHAN: Birthday(11, 20)}
        )
        actual = sut.next_character(date(2022, 7, 22))

        self.assertEqual(
            actual, (MainCharacter.GOCCHAN, BirthDate(2022, 11, 20))
        )
