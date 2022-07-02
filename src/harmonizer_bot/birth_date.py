from dataclasses import dataclass


@dataclass(frozen=True)
class Birthday:
    month: int
    day: int
