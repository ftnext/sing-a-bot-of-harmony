from datetime import date
from urllib.request import urlopen

from bs4 import BeautifulSoup

if __name__ == "__main__":
    today = date.today()
    URL = (
        "https://eigakan.org/theaterpage/schedule.php"
        f"?t=ainouta&d={today:%Y%m%d}"
    )
    with urlopen(URL) as res:
        raw = res.read()

    soup = BeautifulSoup(raw, "html.parser")
    sections = soup.find_all("section", {"class": "theater_list"})
    on_screen_theaters = []
    for section in sections:
        theaters = section.table.find_all("td", {"class": "theater_name"})
        for theater in theaters:
            on_screen_theaters.append(theater.text.strip())

    print(on_screen_theaters)
