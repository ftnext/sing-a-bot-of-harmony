from __future__ import annotations

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


class ScreenDateCollection:
    ...
