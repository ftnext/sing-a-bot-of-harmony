from __future__ import annotations

from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date

from harmonizer_bot.datetime import ScreenDate, ScreenStartTime


@dataclass(frozen=True)
class DayToSlotsSchedule:
    day: ScreenDate
    slots: Sequence[ScreenStartTime]

    def __post_init__(self):
        if len(self.slots) == 0:
            raise ValueError(
                f"Length of slots must be at least 1: {self.slots}"
            )


@dataclass(frozen=True)
class DayToSlotsSchedules(Sequence):
    values: Sequence[DayToSlotsSchedule]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> DayToSlotsSchedule:
        return self.values[key]

    def inverse(
        self, current: date, *, window: int | None = None
    ) -> SlotToDaysSchedules:
        # TODO self.values のソート
        current_and_future = filter(
            lambda schedule: schedule.day >= current, self.values
        )
        current_and_future = (
            list(current_and_future)[:window] if window else current_and_future
        )
        schedules = defaultdict(list)
        for schedule in current_and_future:
            schedules[tuple(schedule.slots)].append(schedule.day)
        return SlotToDaysSchedules(
            [
                SlotToDaysSchedule(slot, days)
                for slot, days in schedules.items()
            ]
        )


@dataclass(frozen=True)
class SlotToDaysSchedule:
    slot: tuple[ScreenStartTime]
    days: Sequence[ScreenDate]

    def __str__(self) -> str:
        start_time_part = " & ".join(f"{st}-" for st in self.slot)
        if len(self.days) >= 2:
            date_part = f"{self.days[0]}-{self.days[-1]}"
        else:
            date_part = f"{self.days[0]}"
        return f"{date_part} {start_time_part}"


@dataclass(frozen=True)
class SlotToDaysSchedules:
    values: Sequence[SlotToDaysSchedule]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> SlotToDaysSchedule:
        return self.values[key]
