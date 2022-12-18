from datetime import date

from sparkling_counter import DayCountDown, XthDayCount
from sparkling_counter.core import (
    ArrivingTheDayException,
    IllegalDayCountError,
)

from harmonizer_bot.blocks import NEW_LINE, Sentence, Sentences
from harmonizer_bot.contents.mixins import ScheduleBuildableMixin
from harmonizer_bot.datetime import ScreenDate, ScreenStartTime
from harmonizer_bot.schedules import DateToSlotsSchedule, DateToSlotsSchedules

from .base import Content


class WasedaShochikuContent(Content):
    LAST_DAY = date(2022, 5, 13)
    COUNT_DOWN = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            f"#アイの歌声を聴かせて 早稲田松竹さんで{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.COUNT_DOWN(self._date)}日）\n"
            "竜そば・サイコトと日替わり2️⃣本立て\n\n"
        )
        text += (
            "開映時間は\n"
            "- 5/7(土)・10(火)・13(金) 13:00 / 17:45\n"
            "- 5/9(月)・12(木) 12:25 / 16:35 / 20:45\n"
            "- 5/8(日)・11(水) 上映なし\n\n"
        )
        text += "詳しくは http://wasedashochiku.co.jp/archives/schedule/19087 をどうぞ"
        return text


class CinemaNekoContent(Content):
    START_DAY = date(2022, 4, 22)
    LAST_DAY = date(2022, 5, 15)
    END_COUNT = DayCountDown(LAST_DAY, include=True)
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 16), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 17), [ScreenStartTime(16, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 18), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 19), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 21), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 22), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 23), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 24), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 25), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 26), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 28), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 29), [ScreenStartTime(14, 30)]
            ),
        ]
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 青梅のシネマネコさんで"
            f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.END_COUNT(self._date)}日）\n\n"
        )
        text += "たたーん🎵 上映時間は、毎日 15:40〜 （5/10(火)は定休日）\n"
        text += "詳しくは https://cinema-neko.com/movie_detail.php?id=94c58c03-e4b1-484d-8a0f-bc9bb885493c をどうぞ！\n\n"  # NOQA: E501
        text += "シネマネコさんのラッキープレイスはー、カフェ！☕️"
        return text


class SumotoOrionContent(Content):
    START_DAY = date(2022, 4, 29)
    LAST_DAY = date(2022, 5, 12)
    END_COUNT = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        text = (
            "#アイの歌声を聴かせて 淡路島の洲本オリオンさんで"
            f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで上映中！"
            f"（今日を含めて残り{self.END_COUNT(self._date)}日）\n\n"
        )
        text += "たたーん🎵 上映時間は、毎日 15:30〜\n"
        text += "詳しくは https://www.sumoto-orion.com/?p=895 をどうぞ！"
        if self._add_yelling():
            text += "\n\n"
            text += "さらに水曜日・日曜日は 18:00〜 無発声応援上映追加！🤗"
        return text

    def _add_yelling(self):
        # 水曜(2)・日曜(6)と前日は無発生応援上映を追加する
        return self._date.weekday() in (1, 2, 5, 6)


class Nagoya109CinemasContent(Content):
    RUN_1ST = date(2022, 5, 28)
    UNTIL_RUN_1ST = DayCountDown(RUN_1ST, include=False)
    RUN_2ND = date(2022, 5, 31)
    UNTIL_RUN_2ND = DayCountDown(RUN_2ND, include=False)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        try:
            days_to_1st_run = self.UNTIL_RUN_1ST(self._date)
        except IllegalDayCountError:
            rest_to_1st_run = ""
        else:
            rest_to_1st_run = f" （あと{days_to_1st_run}日！）"

        rest_to_2nd_run = (
            f" （あと{self.UNTIL_RUN_2ND(self._date)}日"
            f"{'' if rest_to_1st_run else '！'}）"
        )

        text = "#アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！\n\n"
        text += f"- {self.RUN_1ST:%-m/%-d(%a)} 16:30〜{rest_to_1st_run}\n"
        text += f"- {self.RUN_2ND:%-m/%-d(%a)} 16:35〜{rest_to_2nd_run}\n\n"
        text += "チケット発売中！🎫\n"
        text += "詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！"
        return text


class CinePipiaContent(Content):
    START_DAY = date(2022, 7, 22)
    LAST_DAY = date(2022, 7, 28)
    END_COUNT_DOWN = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence(
                "#アイの歌声を聴かせて 兵庫（宝塚市）のシネ・ピピアさんで"
                f"{self.START_DAY:%-m/%-d(%a)}から{self.LAST_DAY:%-m/%-d(%a)}まで"
                f"上映中🌻（今日を含めてあと{self.END_COUNT_DOWN(self._date)}日！）"
            ),
            NEW_LINE,
            Sentence("たたーん🎵 上映時間は、毎日 14:10〜"),
            Sentence("詳しくは http://www.cinepipia.com/schedule.htm をどうぞ！"),
            Sentence("予約は上映7日前から、つまりどの日も予約できます！"),
            NEW_LINE,
            Sentence("この夏、アイうたは西が熱い！"),
        )
        return sentences.format()


class AeonCinemaNishiyamatoContent(Content):
    START_DAY = date(2022, 8, 5)
    LAST_DAY = date(2022, 8, 21)
    END_COUNT_DOWN = DayCountDown(LAST_DAY, include=True)
    AWESOME_TWEETS = (
        "https://twitter.com/ac_nishiyamato/status/1457939683955011586",
        "https://twitter.com/ac_nishiyamato/status/1463045853497606147",
        "https://twitter.com/ac_nishiyamato/status/1467773350407995393",
        "https://twitter.com/ac_nishiyamato/status/1555437288129064960",
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        count = self.END_COUNT_DOWN(self._date)
        sentences = Sentences(
            Sentence(
                "#アイの歌声を聴かせて 奈良のイオンシネマ西大和さんで"
                f"{self.START_DAY:%-m/%-d(%a)}から"
                f"閉館日の{self.LAST_DAY:%-m/%-d(%a)}まで上映中😭"
                f"（今日を含めてあと{count}日！）",
            ),
            NEW_LINE,
            Sentence("たたーん🎵 上映時間は 8/15(月)〜8/20(土) 18:00〜、8/21(日) 15:40〜"),
            Sentence(
                "https://www.aeoncinema.com/cinema2/nishiyamato/"
                "movie/88652/index.html"
            ),
            NEW_LINE,
            Sentence("アイうた愛あふれる映画館なのです！"),
            Sentence(self.AWESOME_TWEETS[count % len(self.AWESOME_TWEETS)]),
        )
        return sentences.format()


class TsukaguchiSunSunTheaterContent(Content):
    START_DAY = date(2022, 8, 19)
    LAST_DAY = date(2022, 8, 25)
    END_COUNT_DOWN = DayCountDown(LAST_DAY, include=True)

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence(
                "#アイの歌声を聴かせて 兵庫 尼崎の塚口サンサン劇場さんで"
                f"{self.START_DAY:%-m/%-d(%a)}から"
                f"{self.LAST_DAY:%-m/%-d(%a)}まで上映中"
                f"（今日を含めてあと{self.END_COUNT_DOWN(self._date)}日！）"
            ),
            NEW_LINE,
            Sentence("たたーん🎵 上映時間は毎日 19:30〜"),
            NEW_LINE,
            Sentence("「あの歓喜の歌声が最高の音響で帰ってくる！」 これはもう、最高なのです！"),
            Sentence(
                "https://twitter.com/sunsuntheater/status/1559821528174235648"
            ),
        )
        return sentences.format()


class CinemaCityContent(Content, ScheduleBuildableMixin):
    START_DAY = ScreenDate(2022, 10, 29)
    LAST_DAY = ScreenDate(2022, 11, 10)
    FROM_START_COUNT_DOWN = XthDayCount(START_DAY)
    END_COUNT_DOWN = DayCountDown(LAST_DAY, include=True)
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 10, 29), [ScreenStartTime(18, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 10, 30),
                [ScreenStartTime(15, 55), ScreenStartTime(21, 15)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 10, 31), [ScreenStartTime(20, 15)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 1), [ScreenStartTime(20, 15)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 2), [ScreenStartTime(20, 15)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 3),
                [ScreenStartTime(16, 0), ScreenStartTime(20, 50)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 4),
                [ScreenStartTime(18, 25), ScreenStartTime(21, 0)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 5),
                [ScreenStartTime(18, 15), ScreenStartTime(20, 55)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 6),
                [ScreenStartTime(18, 15), ScreenStartTime(20, 55)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 7),
                [ScreenStartTime(18, 15), ScreenStartTime(20, 50)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 8),
                [ScreenStartTime(18, 15), ScreenStartTime(20, 50)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 9),
                [ScreenStartTime(18, 15), ScreenStartTime(20, 50)],
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 10),
                [ScreenStartTime(18, 15), ScreenStartTime(20, 50)],
            ),
        ]
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence(
                "#アイの歌声を聴かせて 立川のシネマシティさんで"
                f"{self.START_DAY}から{self.LAST_DAY}まで公開一周年記念上映中！"
            ),
            Sentence(
                f"今日は{self.FROM_START_COUNT_DOWN(self._date)}日目"
                f"（あと{self.END_COUNT_DOWN(self._date)}日！）📡"
            ),
            NEW_LINE,
            *[Sentence(line) for line in self.build_schedule(window=5)],
            NEW_LINE,
            Sentence("🌕MV上映付き！"),
            Sentence(
                "https://twitter.com/cinemacity_jp/status/1586504366231814144"
            ),
        )
        return sentences.format()


class ShinjukuPiccadillyContent(Content, ScheduleBuildableMixin):
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 5), [ScreenStartTime(9, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 7), [ScreenStartTime(13, 50)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 8), [ScreenStartTime(15, 45)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 9), [ScreenStartTime(21, 0)]
            ),
        ]
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        on_and_after_schedules = self.SCHEDULES.select_on_and_after(self._date)
        count_down = DayCountDown(
            on_and_after_schedules[0].date, include=False
        )
        try:
            day_part = f"次回は{count_down(self._date)}日後！"
        except ArrivingTheDayException:
            day_part = "本日です！🎦"

        sentences = Sentences(
            Sentence(f"#アイの歌声を聴かせて 新宿ピカデリーさんのライブ音響上映で4回上映！（{day_part}）"),
            NEW_LINE,
            *[Sentence(line) for line in self.build_schedule()],
            NEW_LINE,
            Sentence(
                "https://twitter.com/liveaudio_fes/status/1587248058500259846"
            ),
            NEW_LINE,
            Sentence("気をつけてー、予告編がないってことにー🎵"),
        )
        return sentences.format()


class TollywoodContent(Content, ScheduleBuildableMixin):
    START_DAY = ScreenDate(2022, 11, 12)
    LAST_DAY = ScreenDate(2022, 11, 18)
    FROM_START_COUNT_DOWN = XthDayCount(START_DAY)
    END_COUNT_DOWN = DayCountDown(LAST_DAY, include=True)
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 12), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 13), [ScreenStartTime(14, 30)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 14), [ScreenStartTime(17, 20)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 16), [ScreenStartTime(17, 20)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 17), [ScreenStartTime(17, 20)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 18), [ScreenStartTime(17, 20)]
            ),
        ]
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        sentences = Sentences(
            Sentence("#アイの歌声を聴かせて 下北沢のトリウッドさんにて1週間限定で再上映中！"),
            Sentence(
                f"今日は{self.FROM_START_COUNT_DOWN(self._date)}日目"
                f"（あと{self.END_COUNT_DOWN(self._date)}日！）🎶"
            ),
            NEW_LINE,
            *[Sentence(line) for line in self.build_schedule()],
            NEW_LINE,
            Sentence(
                "https://twitter.com/tollywooder/status/1591024766441619457"
            ),
            NEW_LINE,
            Sentence("インディーアニメ・インシネマで吉浦監督の『ペイル・コクーン』も上映！"),
        )
        return sentences.format()


class CinemaChupkiContent(Content, ScheduleBuildableMixin):
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 1), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 2), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 3), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 4), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 5), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 6), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 8), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 9), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 10), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 11), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 12), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 13), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 15), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 16), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 18), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 19), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 20), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 22), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 23), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 24), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 25), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 26), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 27), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 29), [ScreenStartTime(19, 10)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 30), [ScreenStartTime(19, 10)]
            ),
        ]
    )

    def generate(self) -> str:
        raise NotImplementedError


class WowowBroadCastContent(Content, ScheduleBuildableMixin):
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 4), [ScreenStartTime(21, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 7), [ScreenStartTime(17, 0)]
            ),
            DateToSlotsSchedule(
                ScreenDate(2022, 11, 14), [ScreenStartTime(17, 0)]
            ),
        ]
    )

    def __init__(self, date_: date) -> None:
        self._date = date_

    def generate(self) -> str:
        on_and_after_schedules = self.SCHEDULES.select_on_and_after(self._date)
        count_down = DayCountDown(
            on_and_after_schedules[0].date, include=False
        )
        try:
            day_part = f"次回は{count_down(self._date)}日後！"
        except ArrivingTheDayException:
            day_part = "本日です！🎉"

        sentences = Sentences(
            Sentence(f"#アイの歌声を聴かせて この11月、WOWOWで放送！（{day_part}）"),
            NEW_LINE,
            *[Sentence(line) for line in self.build_schedule()],
            NEW_LINE,
            Sentence(
                "https://twitter.com/wowow_movie/status/1587738821684187137"
            ),
            NEW_LINE,
            Sentence("WOWOW加入されている方はぜひ！"),
        )
        return sentences.format()


class CineCittaContent:
    SCHEDULES = DateToSlotsSchedules(
        [
            DateToSlotsSchedule(
                ScreenDate(2022, 12, 31), [ScreenStartTime(18, 30)]
            )
        ]
    )
