from datetime import date
from unittest import TestCase

from harmonizer_bot.contents.mixins import ScheduleBuildableMixin
from harmonizer_bot.datetime import ScreenDate, ScreenStartTime
from harmonizer_bot.schedules import DateToSlotsSchedule, DateToSlotsSchedules


class ScheduleBuildableMixinTestCase(TestCase):
    def test_subclass_can_build_schedule(self):
        class ScheduleBuildableUnderTest(ScheduleBuildableMixin):
            SCHEDULES = DateToSlotsSchedules(
                [
                    DateToSlotsSchedule(
                        ScreenDate(2022, 11, 2), [ScreenStartTime(20, 0)]
                    ),
                    DateToSlotsSchedule(
                        ScreenDate(2022, 11, 3), [ScreenStartTime(15, 0)]
                    ),
                    DateToSlotsSchedule(
                        ScreenDate(2022, 11, 1), [ScreenStartTime(9, 0)]
                    ),
                ]
            )

            def __init__(self, date: date) -> None:
                self._date = date

        sut = ScheduleBuildableUnderTest(date(2022, 11, 2))

        actual = sut.build_schedule()

        self.assertEqual(actual, ["11/2(水) 20:00-", "11/3(木) 15:00-"])
