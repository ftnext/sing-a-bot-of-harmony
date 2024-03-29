from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date
from enum import Enum, auto

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.birthday import (
    AyaBirthdayContent,
    GocchanBirthdayContent,
    ShionBirthdayContent,
)
from harmonizer_bot.datetime import BirthDate


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

    def next_character(self, date_: date) -> tuple[MainCharacter, BirthDate]:
        sorted_items = sorted(self.values.items(), key=lambda t: t[1])
        head_date = sorted_items[0][1].to_date(date_.year)
        if date_ <= head_date:
            return sorted_items[0][0], BirthDate.from_(head_date)
        tail_date = sorted_items[-1][1].to_date(date_.year)
        if tail_date < date_:
            next_year_date = head_date.replace(date_.year + 1)
            return sorted_items[0][0], BirthDate.from_(next_year_date)
        for i in range(len(sorted_items) - 1):
            first = sorted_items[i][1].to_date(date_.year)
            second = sorted_items[i + 1][1].to_date(date_.year)
            if first < date_ <= second:
                return sorted_items[i + 1][0], BirthDate.from_(second)


class MainCharacterBirthdayDispatcher:
    def __init__(self):
        self.birthdays = Birthdays(
            {
                MainCharacter.SHION: Birthday(6, 6),
                MainCharacter.AYA: Birthday(7, 8),
                MainCharacter.GOCCHAN: Birthday(11, 20),
            }
        )
        self.contents = {
            MainCharacter.SHION: ShionBirthdayContent,
            MainCharacter.AYA: AyaBirthdayContent,
            MainCharacter.GOCCHAN: GocchanBirthdayContent,
        }

    def dispatch(self, date_: date) -> Content:
        next_character, next_birthday = self.birthdays.next_character(date_)
        content_class = self.contents[next_character]
        return content_class(next_birthday, date_)
