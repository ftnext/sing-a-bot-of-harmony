from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from enum import Enum, auto


class MainCharacter(Enum):
    SHION = auto()
    AYA = auto()


@dataclass(frozen=True)
class Birthday:
    month: int
    day: int

    def to_date(self, year: int) -> date:
        return date(year, self.month, self.day)


@dataclass(frozen=True)
class Birthdays:
    values: Mapping[MainCharacter, Birthday]

    def next_from(self, date_: date):
        raise NotImplementedError
