from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date

from harmonizer_bot.datetime import (
    AscendingScreenDates,
    ScreenDate,
    ScreenStartTime,
)


@dataclass(frozen=True)
class DateToSlotsSchedule:
    date: ScreenDate
    slots: Sequence[ScreenStartTime]

    def __post_init__(self):
        if len(self.slots) == 0:
            raise ValueError(
                f"Length of slots must be at least 1: {self.slots}"
            )


@dataclass(frozen=True)
class DateToSlotsSchedules(Sequence):
    values: Sequence[DateToSlotsSchedule]

    def __post_init__(self):
        seen_dates = set()
        for schedule in self.values:
            if str(schedule.date) in seen_dates:
                raise ValueError(
                    f"Each date must be unique. {schedule.date} is "
                    f"duplicated: {schedule}"
                )
            seen_dates.add(str(schedule.date))

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(
        self, key: int | slice
    ) -> DateToSlotsSchedule | DateToSlotsSchedules:
        if isinstance(key, slice):
            return self.__class__(self.values[key])
        return self.values[key]

    def sort(self):
        sorted_values = sorted(self.values, key=lambda schedule: schedule.date)
        return self.__class__(sorted_values)

    def select_on_and_after(
        self, date: date
    ) -> OnAndAfterTodayDateToSlotsSchedules:
        sorted_schedules = self.sort()
        current_and_future = filter(
            lambda schedule: schedule.date >= date, sorted_schedules
        )
        return OnAndAfterTodayDateToSlotsSchedules(list(current_and_future))

    def transpose(self) -> SlotToDatesSchedules:
        schedules = defaultdict(list)
        for schedule in self:
            schedules[tuple(schedule.slots)].append(schedule.date)
        return SlotToDatesSchedules(
            [
                SlotToDatesSchedule(slot, AscendingScreenDates(days))
                for slot, days in schedules.items()
            ]
        )


@dataclass(frozen=True)
class OnAndAfterTodayDateToSlotsSchedules(DateToSlotsSchedules):
    values: Sequence[DateToSlotsSchedule]

    def __post_init__(self):
        sorted_values = sorted(self.values, key=lambda v: v.date)
        if list(self.values) != sorted_values:
            raise ValueError(f"Dates must be sorted ascending: {self.values}")


@dataclass(frozen=True)
class SlotToDatesSchedule:
    slot: tuple[ScreenStartTime]
    dates: AscendingScreenDates

    def __str__(self) -> str:
        start_time_part = " & ".join(f"{st}" for st in self.slot)
        dates_part = f"{self.dates}"
        return f"{dates_part} {start_time_part}"


@dataclass(frozen=True)
class SlotToDatesSchedules:
    values: Sequence[SlotToDatesSchedule]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> SlotToDatesSchedule:
        return self.values[key]
