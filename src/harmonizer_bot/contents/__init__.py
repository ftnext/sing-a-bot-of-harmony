import locale

from .events import (  # NOQA: F401
    HappyProjectContent,
    PublishingLimitedTimeContent,
)
from .greetings import MorningGreetingContent  # NOQA: F401
from .theaters import CinePipiaContent  # NOQA: F401

locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")
