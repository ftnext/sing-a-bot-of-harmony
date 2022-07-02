from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from enum import Enum, auto


class MainCharacter(Enum):
    SHION = auto()
    AYA = auto()


@dataclass(frozen=True, order=True)
class Birthday:
    month: int
    day: int

    def to_date(self, year: int) -> date:
        return date(year, self.month, self.day)


@dataclass(frozen=True)
class Birthdays:
    values: Mapping[MainCharacter, Birthday]

    def next_character(self, date_: date) -> MainCharacter:
        sorted_items = sorted(self.values.items(), key=lambda t: t[1])
        for i in range(len(sorted_items) - 1):
            first = sorted_items[i][1].to_date(date_.year)
            second = sorted_items[i + 1][1].to_date(date_.year)
            if first < date_ <= second:
                return sorted_items[i + 1][0]
