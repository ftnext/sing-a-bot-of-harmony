import locale

from .events import (  # NOQA: F401
    DiskReleaseFestivalContent,
    HappyProjectContent,
)
from .greetings import MorningGreetingContent  # NOQA: F401
from .theaters import (  # NOQA: F401
    AeonCinemaNishiyamatoContent,
    TsukaguchiSunSunTheaterContent,
)

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")
