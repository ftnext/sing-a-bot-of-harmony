from unittest import TestCase

from harmonizer_bot.datetime import ScreenDate, ScreenStartTime
from harmonizer_bot.schedules import DayToSlotsSchedule, DayToSlotsSchedules


class DayToSlotsScheduleTestCase(TestCase):
    def test_cannot_create_when_slots_are_empty(self):
        with self.assertRaises(ValueError):
            _ = DayToSlotsSchedule(ScreenDate(2022, 10, 31), [])


class DayToSlotsSchedulesTestCase(TestCase):
    def test_cannot_create_when_date_are_duplicated(self):
        with self.assertRaises(ValueError):
            _ = DayToSlotsSchedules(
                [
                    DayToSlotsSchedule(
                        ScreenDate(2022, 11, 1),
                        [ScreenStartTime(9, 30), ScreenStartTime(18, 15)],
                    ),
                    DayToSlotsSchedule(
                        ScreenDate(2022, 11, 2), [ScreenStartTime(15, 0)]
                    ),
                    DayToSlotsSchedule(
                        ScreenDate(2022, 11, 1), [ScreenStartTime(12, 45)]
                    ),
                ]
            )
