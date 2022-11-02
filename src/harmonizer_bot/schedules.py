from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date

from harmonizer_bot.datetime import (
    ScreenDate,
    ScreenDateCollection,
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
                    f"Each date must be unique. {schedule.date} is duplicated: "
                    f"{schedule}"
                )
            seen_dates.add(str(schedule.date))

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> DateToSlotsSchedule:
        return self.values[key]

    def inverse(
        self, current: date, *, window: int | None = None
    ) -> SlotToDatesSchedules:
        # TODO self.values のソート
        current_and_future = filter(
            lambda schedule: schedule.date >= current, self.values
        )
        current_and_future = (
            list(current_and_future)[:window] if window else current_and_future
        )
        schedules = defaultdict(list)
        for schedule in current_and_future:
            schedules[tuple(schedule.slots)].append(schedule.date)
        return SlotToDatesSchedules(
            [
                SlotToDatesSchedule(slot, ScreenDateCollection(days))
                for slot, days in schedules.items()
            ]
        )


@dataclass(frozen=True)
class SlotToDatesSchedule:
    slot: tuple[ScreenStartTime]
    dates: ScreenDateCollection

    def __str__(self) -> str:
        start_time_part = " & ".join(f"{st}-" for st in self.slot)
        dates_part = f"{self.dates}"
        return f"{dates_part} {start_time_part}"


@dataclass(frozen=True)
class SlotToDatesSchedules:
    values: Sequence[SlotToDatesSchedule]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> SlotToDatesSchedule:
        return self.values[key]
