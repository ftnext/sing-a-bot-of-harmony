from __future__ import annotations

from datetime import date


class BirthDate(date):
    def __str__(self) -> str:
        return f"{self:%-m/%-d}"

    @classmethod
    def from_(cls, date_: date) -> BirthDate:
        return cls(date_.year, date_.month, date_.day)
