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
class ScreenDateCollection(Sequence):
    values: Sequence[ScreenDate]

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, key) -> ScreenStartTime:
        return self.values[key]

    def __str__(self) -> str:
        start_date = self[0]
        dates_string = f"{start_date}"
        period_end_date = None
        for day in self.values[1:]:
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
