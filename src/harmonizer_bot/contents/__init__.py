import locale

from .events import HappyProjectContent  # NOQA: F401
from .greetings import MorningGreetingContent  # NOQA: F401
from .resources import ShowingTheatersContent  # NOQA: F401
from .theaters import (  # NOQA: F401
    CinemaCityContent,
    ShinjukuPiccadillyContent,
    WowowBroadCastContent,
)

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")
