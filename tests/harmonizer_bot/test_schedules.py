from unittest import TestCase
from unittest.mock import MagicMock

from harmonizer_bot.datetime import (
    ScreenDate,
    ScreenDateCollection,
    ScreenStartTime,
)
from harmonizer_bot.schedules import (
    DateToSlotsSchedule,
    DateToSlotsSchedules,
    SlotToDatesSchedule,
)


class DateToSlotsScheduleTestCase(TestCase):
    def test_cannot_create_when_slots_are_empty(self):
        with self.assertRaises(ValueError):
            _ = DateToSlotsSchedule(ScreenDate(2022, 10, 31), [])


class DateToSlotsSchedulesTestCase(TestCase):
    def test_cannot_create_when_date_are_duplicated(self):
        with self.assertRaises(ValueError):
            _ = DateToSlotsSchedules(
                [
                    DateToSlotsSchedule(
                        ScreenDate(2022, 11, 1),
                        [ScreenStartTime(9, 30), ScreenStartTime(18, 15)],
                    ),
                    DateToSlotsSchedule(
                        ScreenDate(2022, 11, 2), [ScreenStartTime(15, 0)]
                    ),
                    DateToSlotsSchedule(
                        ScreenDate(2022, 11, 1), [ScreenStartTime(12, 45)]
                    ),
                ]
            )


class SlotToDatesScheduleTestCase(TestCase):
    def test_str(self):
        screen_dates = MagicMock(spec=ScreenDateCollection)
        screen_dates_string = screen_dates.__str__.return_value
        schedule = SlotToDatesSchedule(
            (ScreenStartTime(11, 38), ScreenStartTime(23, 38)), screen_dates
        )

        self.assertEqual(
            str(schedule), f"{screen_dates_string} 11:38- & 23:38-"
        )
