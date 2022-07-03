from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from enum import Enum, auto


class MainCharacter(Enum):
    SHION = auto()
    AYA = auto()
    GOCCHAN = auto()


@dataclass(frozen=True, order=True)
class Birthday:
    month: int
    day: int

    def to_date(self, year: int) -> date:
        return date(year, self.month, self.day)


@dataclass(frozen=True)
class Birthdays:
    values: Mapping[MainCharacter, Birthday]

    def next_character(self, date_: date) -> tuple[MainCharacter, date]:
        sorted_items = sorted(self.values.items(), key=lambda t: t[1])
        head_date = sorted_items[0][1].to_date(date_.year)
        if date_ <= head_date:
            return sorted_items[0][0], head_date
        tail_date = sorted_items[-1][1].to_date(date_.year)
        if tail_date < date_:
            return sorted_items[0][0], head_date.replace(date_.year + 1)
        for i in range(len(sorted_items) - 1):
            first = sorted_items[i][1].to_date(date_.year)
            second = sorted_items[i + 1][1].to_date(date_.year)
            if first < date_ <= second:
                return sorted_items[i + 1][0], second
