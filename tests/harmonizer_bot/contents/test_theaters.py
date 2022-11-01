from datetime import date
from textwrap import dedent
from unittest import TestCase, skip
from unittest.mock import MagicMock

from harmonizer_bot.contents.base import Content
from harmonizer_bot.contents.theaters import (
    AeonCinemaNishiyamatoContent,
    CinemaCityContent,
    CinemaNekoContent,
    CinePipiaContent,
    Nagoya109CinemasContent,
    ShinjukuPiccadillyContent,
    SumotoOrionContent,
    TsukaguchiSunSunTheaterContent,
    WasedaShochikuContent,
)

from .support import ContentTestCase


class WasedaShochikuContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = WasedaShochikuContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 早稲田松竹さんで5/13(金)まで上映中！（今日を含めて残り7日）
            竜そば・サイコトと日替わり2️⃣本立て

            開映時間は
            - 5/7(土)・10(火)・13(金) 13:00 / 17:45
            - 5/9(月)・12(木) 12:25 / 16:35 / 20:45
            - 5/8(日)・11(水) 上映なし

            詳しくは http://wasedashochiku.co.jp/archives/schedule/19087 をどうぞ
            """
        ).rstrip()

        content = WasedaShochikuContent(date(2022, 5, 7))
        actual = content.generate()

        self.assertEqual(actual, expected)


class CinemaNekoContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = CinemaNekoContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 青梅のシネマネコさんで4/22(金)から5/15(日)まで上映中！（今日を含めて残り12日）

            たたーん🎵 上映時間は、毎日 15:40〜 （5/10(火)は定休日）
            詳しくは https://cinema-neko.com/movie_detail.php?id=94c58c03-e4b1-484d-8a0f-bc9bb885493c をどうぞ！

            シネマネコさんのラッキープレイスはー、カフェ！☕️
            """
        ).rstrip()

        content = CinemaNekoContent(date(2022, 5, 4))
        actual = content.generate()

        self.assertEqual(actual, expected)


class SumotoOrionContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = SumotoOrionContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate_no_yelling(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 淡路島の洲本オリオンさんで4/29(金)から5/12(木)まで上映中！（今日を含めて残り8日）

            たたーん🎵 上映時間は、毎日 15:30〜
            詳しくは https://www.sumoto-orion.com/?p=895 をどうぞ！
            """
        ).rstrip()

        content = SumotoOrionContent(date(2022, 5, 5))
        actual = content.generate()

        self.assertEqual(actual, expected)

    def test_generate_yelling(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 淡路島の洲本オリオンさんで4/29(金)から5/12(木)まで上映中！（今日を含めて残り9日）

            たたーん🎵 上映時間は、毎日 15:30〜
            詳しくは https://www.sumoto-orion.com/?p=895 をどうぞ！

            さらに水曜日・日曜日は 18:00〜 無発声応援上映追加！🤗
            """
        ).rstrip()

        content = SumotoOrionContent(date(2022, 5, 4))
        actual = content.generate()

        self.assertEqual(actual, expected)


class Nagoya109CinemasContentTestCase(TestCase):
    def test_init(self):
        date_ = MagicMock(spec=date)

        actual = Nagoya109CinemasContent(date_)

        self.assertIsInstance(actual, Content)
        self.assertEqual(actual._date, date_)

    def test_generate(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！

            - 5/28(土) 16:30〜 （あと1日！）
            - 5/31(火) 16:35〜 （あと4日）

            チケット発売中！🎫
            詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！
            """
        ).rstrip()

        content = Nagoya109CinemasContent(date(2022, 5, 27))
        actual = content.generate()

        self.assertEqual(actual, expected)

    @skip("WIP: handling ArrivingTheDayException")
    def test_generate_31th_only(self):
        expected = dedent(
            """\
            #アイの歌声を聴かせて 愛知の109シネマズ名古屋さんの映画祭でライブ音響上映！！

            - 5/28(土) 16:30〜
            - 5/31(火) 16:35〜 （あと3日！）

            チケット発売中！🎫
            詳しくは https://109cinemas.net/events/liveonkyo_nagoya/ をどうぞ！
            """
        ).rstrip()

        content = Nagoya109CinemasContent(date(2022, 5, 28))
        actual = content.generate()

        self.assertEqual(actual, expected)


class CinePipiaContentTestCase(ContentTestCase):
    target_class = CinePipiaContent
    generation_date = date(2022, 7, 26)
    generated_content = """
    #アイの歌声を聴かせて 兵庫（宝塚市）のシネ・ピピアさんで7/22(金)から7/28(木)まで上映中🌻（今日を含めてあと3日！）

    たたーん🎵 上映時間は、毎日 14:10〜
    詳しくは http://www.cinepipia.com/schedule.htm をどうぞ！
    予約は上映7日前から、つまりどの日も予約できます！

    この夏、アイうたは西が熱い！
    """


class AeonCinemaNishiyamatoContentTestCase(ContentTestCase):
    target_class = AeonCinemaNishiyamatoContent
    generation_date = date(2022, 8, 18)
    generated_content = """
    #アイの歌声を聴かせて 奈良のイオンシネマ西大和さんで8/5(金)から閉館日の8/21(日)まで上映中😭（今日を含めてあと4日！）

    たたーん🎵 上映時間は 8/15(月)〜8/20(土) 18:00〜、8/21(日) 15:40〜
    https://www.aeoncinema.com/cinema2/nishiyamato/movie/88652/index.html

    アイうた愛あふれる映画館なのです！
    https://twitter.com/ac_nishiyamato/status/1457939683955011586
    """


class TsukaguchiSunSunTheaterContentTestCase(ContentTestCase):
    target_class = TsukaguchiSunSunTheaterContent
    generation_date = date(2022, 8, 24)
    generated_content = """
    #アイの歌声を聴かせて 兵庫 尼崎の塚口サンサン劇場さんで8/19(金)から8/25(木)まで上映中（今日を含めてあと2日！）

    たたーん🎵 上映時間は毎日 19:30〜

    「あの歓喜の歌声が最高の音響で帰ってくる！」 これはもう、最高なのです！
    https://twitter.com/sunsuntheater/status/1559821528174235648
    """


class CinemaCityContentTestCase(ContentTestCase):
    target_class = CinemaCityContent
    generation_date = date(2022, 10, 30)
    generated_content = """
    #アイの歌声を聴かせて 立川のシネマシティさんで10/29(土)から11/10(木)まで公開一周年記念上映中！
    今日を含めてあと12日📡

    10/30(日) 15:55- & 21:15-
    10/31(月)-11/2(水) 20:15-
    11/3(木) 16:00- & 20:50-

    https://twitter.com/cinemacity_jp/status/1580848214365700097
    """

    def test_build_schedule(self):
        expected = [
            "10/29(土) 18:30-",
            "10/30(日) 15:55- & 21:15-",
            "10/31(月)-11/2(水) 20:15-",
        ]
        content = self.target_class(date(2022, 10, 29))

        actual = content.build_schedule()

        self.assertEqual(actual, expected)


class ShinjukuPiccadillyContentTestCase(ContentTestCase):
    target_class = ShinjukuPiccadillyContent
    generation_date = date(2022, 11, 1)
    generated_content = """
    #アイの歌声を聴かせて 新宿ピカデリーさんのライブ音響上映で4回上映！（4日後から！）

    11/5(土) 9:00-
    11/7(月) 13:50-
    11/8(火) 15:45-
    11/9(水) 21:00-

    https://twitter.com/liveaudio_fes/status/1587248058500259846

    気をつけてー、予告編がないってことにー🎵
    """
