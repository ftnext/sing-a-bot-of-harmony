from datetime import date, time
from unittest import TestCase

from harmonizer_bot.datetime import (
    BirthDate,
    CustomizedBaseDate,
    ScreenDate,
    ScreenDateCollection,
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


class ScreenDateCollectionTestCase(TestCase):
    def test_single_date_string(self):
        screen_dates = ScreenDateCollection([ScreenDate(2022, 6, 6)])

        self.assertEqual(str(screen_dates), "6/6(月)")

    def test_continuous_period_string_with_start_and_end_dates(self):
        screen_dates = ScreenDateCollection(
            [ScreenDate(2022, 11, 10), ScreenDate(2022, 11, 11)]
        )
        self.assertEqual(str(screen_dates), "11/10(木)-11/11(金)")

        screen_dates2 = ScreenDateCollection(
            [
                ScreenDate(2022, 11, 10),
                ScreenDate(2022, 11, 11),
                ScreenDate(2022, 11, 12),
            ]
        )
        self.assertEqual(str(screen_dates2), "11/10(木)-11/12(土)")

    def test_intermittent_period_string(self):
        screen_dates = ScreenDateCollection(
            [ScreenDate(2022, 11, 9), ScreenDate(2022, 11, 11)]
        )

        self.assertEqual(str(screen_dates), "11/9(水) & 11/11(金)")
