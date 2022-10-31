from unittest import TestCase

from harmonizer_bot.datetime import ScreenDate
from harmonizer_bot.schedules import DayToSlotsSchedule


class DayToSlotsScheduleTestCase(TestCase):
    def test_cannot_create_when_slots_are_empty(self):
        with self.assertRaises(ValueError):
            _ = DayToSlotsSchedule(ScreenDate(2022, 10, 31), [])
