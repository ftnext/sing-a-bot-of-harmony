from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import date, time


class CustomizedBaseDate(date):
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, self.__class__):
            return False
        return super().__eq__(__o)

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    @classmethod
    def from_(cls, date_: date) -> BirthDate:
        return cls(date_.year, date_.month, date_.day)

    def to_date(self) -> date:
        return date(self.year, self.month, self.day)


class BirthDate(CustomizedBaseDate):
    def __str__(self) -> str:
        return f"{self:%-m/%-d}"


class ScreenDate(CustomizedBaseDate):
    def __str__(self) -> str:
        return f"{self:%-m/%-d(%a)}"


class ScreenStartTime(time):
    def __str__(self) -> str:
        return f"{self:%-H:%M}"


@dataclass(frozen=True)
class AscendingScreenDates(Sequence):
    values: Sequence[ScreenDate]

    def __post_init__(self):
        if len(self.values) == 0:
            raise ValueError(
                f"Length of values must be at least 1: {self.values}"
            )

        sorted_values = sorted(self.values)
        if list(self.values) != sorted_values:
            raise ValueError(f"Dates must be sorted ascending: {self.values}")

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(
        self, key: int | slice
    ) -> ScreenDate | AscendingScreenDates:
        if isinstance(key, slice):
            return self.__class__(self.values[key])
        return self.values[key]

    def __str__(self) -> str:
        if len(self) == 1:
            return str(self[0])

        start_date = self[0]
        dates_string = f"{start_date}"
        period_end_date = None
        for day in self[1:]:
            if (day - start_date).days == 1:
                period_end_date = day
                start_date = day
                continue
            if (day - start_date).days > 1:
                if period_end_date:
                    dates_string += f"-{period_end_date}"
                    period_end_date = None
                dates_string += f" & {day}"
                start_date = day
        if period_end_date:
            dates_string += f"-{period_end_date}"
        return dates_string
