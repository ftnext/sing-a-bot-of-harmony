from collections.abc import Sequence
from dataclasses import dataclass

from harmonizer_bot.datetime import ScreenDate, ScreenStartTime


@dataclass(frozen=True)
class DayToSlotsSchedule:
    day: ScreenDate
    slots: Sequence[ScreenStartTime]


@dataclass(frozen=True)
class DayToSlotsSchedules(Sequence):
    values: Sequence[DayToSlotsSchedule]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> DayToSlotsSchedule:
        return self.values[key]

    def inverse(self):
        raise NotImplementedError
