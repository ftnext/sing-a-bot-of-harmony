from datetime import date, time
from unittest import TestCase

from harmonizer_bot.datetime import (
    AscendingScreenDates,
    BirthDate,
    CustomizedBaseDate,
    ScreenDate,
    ScreenStartTime,
)


class CustomizedBaseDateTestCase(TestCase):
    def test_can_create(self):
        self.assertIsInstance(CustomizedBaseDate(2022, 6, 6), date)

    def test_convert_from_date(self):
        date_ = date(2022, 11, 20)
        self.assertEqual(
            CustomizedBaseDate.from_(date_), CustomizedBaseDate(2022, 11, 20)
        )

    def test_equal(self):
        self.assertTrue(
            CustomizedBaseDate(2022, 12, 31)
            == CustomizedBaseDate(2022, 12, 31)
        )
        self.assertNotEqual(
            CustomizedBaseDate(2022, 12, 31), date(2022, 12, 31)
        )
        self.assertNotEqual(
            date(2022, 12, 31), CustomizedBaseDate(2022, 12, 31)
        )


class BirthDateTestCase(TestCase):
    def test_can_create(self):
        self.assertIsInstance(BirthDate(2022, 6, 6), CustomizedBaseDate)

    def test_format_month_and_day(self):
        birth_date = BirthDate(2022, 4, 10)
        self.assertEqual(f"{birth_date}", "4/10")

    def test_convert_from_date(self):
        date_ = date(2022, 11, 20)
        self.assertEqual(BirthDate.from_(date_), BirthDate(2022, 11, 20))

    def test_equal(self):
        self.assertTrue(BirthDate(2022, 12, 31) == BirthDate(2022, 12, 31))
        self.assertNotEqual(BirthDate(2022, 12, 31), date(2022, 12, 31))
        self.assertNotEqual(date(2022, 12, 31), BirthDate(2022, 12, 31))


class ScreenDateTestCase(TestCase):
    def test_can_create(self):
        self.assertIsInstance(ScreenDate(2022, 6, 6), CustomizedBaseDate)

    def test_format_month__day__day_of_the_week(self):
        screen_date = ScreenDate(2022, 4, 10)
        self.assertEqual(f"{screen_date}", "4/10(日)")


class ScreenStartTimeTestCase(TestCase):
    def test_can_create(self):
        self.assertIsInstance(ScreenStartTime(18, 0), time)

    def test_format_hour_and_minute(self):
        start_time = ScreenStartTime(15, 5)
        self.assertEqual(f"{start_time}", "15:05")

        start_time2 = ScreenStartTime(5, 15)
        self.assertEqual(f"{start_time2}", "5:15")


class AscendingScreenDatesTestCase(TestCase):
    def test_cannot_create_when_dates_are_empty(self):
        with self.assertRaises(ValueError):
            _ = AscendingScreenDates([])

    def test_cannot_create_from_not_ascending_dates(self):
        dates = [
            ScreenDate(2022, 11, 2),
            ScreenDate(2022, 11, 1),
            ScreenDate(2022, 11, 3),
        ]
        with self.assertRaises(ValueError):
            _ = AscendingScreenDates(dates)

    def test_get_single_date(self):
        screen_date_0 = ScreenDate(2022, 10, 30)
        screen_date_1 = ScreenDate(2022, 10, 31)
        screen_dates = AscendingScreenDates([screen_date_0, screen_date_1])

        self.assertEqual(screen_dates[1], screen_date_1)

    def test_get_multiple_dates_with_slice(self):
        screen_date_0 = ScreenDate(2022, 11, 1)
        screen_date_1 = ScreenDate(2022, 11, 2)
        screen_date_2 = ScreenDate(2022, 11, 3)
        screen_dates = AscendingScreenDates(
            [screen_date_0, screen_date_1, screen_date_2]
        )

        expected_head2 = AscendingScreenDates([screen_date_0, screen_date_1])
        self.assertEqual(screen_dates[:2], expected_head2)

        expected_tail2 = AscendingScreenDates([screen_date_1, screen_date_2])
        self.assertEqual(screen_dates[1:], expected_tail2)

    def test_single_date_string(self):
        screen_dates = AscendingScreenDates([ScreenDate(2022, 6, 6)])

        self.assertEqual(str(screen_dates), "6/6(月)")

    def test_continuous_period_string_with_start_and_end_dates(self):
        screen_dates = AscendingScreenDates(
            [ScreenDate(2022, 11, 10), ScreenDate(2022, 11, 11)]
        )
        self.assertEqual(str(screen_dates), "11/10(木)-11/11(金)")

        screen_dates2 = AscendingScreenDates(
            [
                ScreenDate(2022, 11, 10),
                ScreenDate(2022, 11, 11),
                ScreenDate(2022, 11, 12),
            ]
        )
        self.assertEqual(str(screen_dates2), "11/10(木)-11/12(土)")

    def test_intermittent_period_string(self):
        screen_dates = AscendingScreenDates(
            [ScreenDate(2022, 11, 9), ScreenDate(2022, 11, 11)]
        )

        self.assertEqual(str(screen_dates), "11/9(水) & 11/11(金)")

    def test_continuous_and_intermittent_mixed_string(self):
        screen_dates = AscendingScreenDates(
            [
                ScreenDate(2022, 11, 4),
                ScreenDate(2022, 11, 7),
                ScreenDate(2022, 11, 8),
                ScreenDate(2022, 11, 10),
            ]
        )

        expected = "11/4(金) & 11/7(月)-11/8(火) & 11/10(木)"
        self.assertEqual(str(screen_dates), expected)
