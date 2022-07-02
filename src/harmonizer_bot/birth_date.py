from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Birthday:
    month: int
    day: int

    def to_date(self, year: int) -> date:
        raise NotImplementedError
