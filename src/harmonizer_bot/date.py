from datetime import date


class BirthDate(date):
    def __str__(self) -> str:
        return f"{self:%-m/%-d}"
