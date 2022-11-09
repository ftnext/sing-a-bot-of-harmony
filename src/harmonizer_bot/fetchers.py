from datetime import date
from urllib.parse import urlencode
from urllib.request import urlopen

from bs4 import BeautifulSoup

TheaterName = str


class ShowingTheatersFetcher:
    BASE_URL = "https://eigakan.org/theaterpage/schedule.php"

    def fetch(self, date_: date) -> list[TheaterName]:
        url = self.build_url(date_)
        raw = self.read(url)
        return self.parse(raw)

    def build_url(self, date_: date) -> str:
        query = urlencode({"t": "ainouta", "d": f"{date_:%Y%m%d}"})
        return f"{self.BASE_URL}?{query}"

    def read(self, url: str) -> str:
        with urlopen(url) as res:
            return res.read()

    def parse(self, raw_html: str) -> list[TheaterName]:
        soup = BeautifulSoup(raw_html, "html.parser")
        sections = soup.find_all("section", {"class": "theater_list"})
        screening_theaters = []
        for section in sections:
            theaters = section.table.find_all("td", {"class": "theater_name"})
            for theater in theaters:
                screening_theaters.append(theater.text.strip())
        return screening_theaters
