from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from harmonizer_bot.blocks import NEW_LINE, Sentence, Sentences
from harmonizer_bot.contents.base import Content
from harmonizer_bot.fetchers import ShowingTheatersFetcher


class ShowingTheatersContent(Content):
    def __init__(self, date_: date) -> None:
        self._date = date_
        self._time = datetime.now(ZoneInfo("Asia/Tokyo")).time()

    def fetch_theaters(self):
        fetcher = ShowingTheatersFetcher()
        return fetcher.fetch(self._date + timedelta(days=1))

    def generate(self) -> str:
        theaters = self.fetch_theaters()
        sentences = Sentences(
            Sentence(
                f"アイの歌声を聴かせては以下の劇場で上映中または上映予定！"
                f"（{self._date:%-m/%-d} {self._time:%H:%M}時点に取得した情報です）"
            ),
            *[Sentence(f"🌕{theater}") for theater in theaters],
            NEW_LINE,
            Sentence("https://eigakan.org/theaterpage/schedule.php?t=ainouta"),
        )
        return sentences.format()
