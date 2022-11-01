from unittest import TestCase

from harmonizer_bot.datetime import (
    ScreenDate,
    ScreenDateCollection,
    ScreenStartTime,
)
from harmonizer_bot.schedules import (
    DayToSlotsSchedule,
    DayToSlotsSchedules,
    SlotToDaysSchedule,
)


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


class SlotToDaysScheduleTestCase(TestCase):
    def test_continuous_period_string(self):
        schedule = SlotToDaysSchedule(
            (ScreenStartTime(11, 38),),
            ScreenDateCollection(
                [ScreenDate(2022, 11, 10), ScreenDate(2022, 11, 11)]
            ),
        )

        self.assertEqual(str(schedule), "11/10(木)-11/11(金) 11:38-")

    def test_intermittent_period_string(self):
        schedule = SlotToDaysSchedule(
            (ScreenStartTime(23, 38),),
            ScreenDateCollection(
                [ScreenDate(2022, 11, 9), ScreenDate(2022, 11, 11)]
            ),
        )

        self.assertEqual(str(schedule), "11/9(水) & 11/11(金) 23:38-")
