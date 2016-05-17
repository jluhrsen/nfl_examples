from nfl_data.nfl_local_data_handler import *
import unittest

__author__ = 'jamo'


class TestGetAPI(unittest.TestCase):

    # data_handler = nfl_data_server_handler()
    data_handler = nfl_local_data_handler()

    @unittest.skip("skipping because no access to NFLDATA API and because of length")
    def test_get_schedules(self):
        for season in range(1985, 2015):
            schedule = self.data_handler.get_schedule(season)
            for i in schedule:
                self.assertEqual(i['Season'], season)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_schedule_for_bad_year(self):
        with self.assertRaises(Warning):
            self.data_handler.get_schedule(1980)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_schedule_with_bad_format(self):
        with self.assertRaises(ValueError):
            self.data_handler.get_schedule('shouldNotWork')

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_single_game(self):
        game = self.data_handler.get_game('OAK', 'SD', 6, 2014)
        self.assertEqual(game['Team'], 'OAK')
        self.assertEquals(game['HomeOrAway'], 'HOME')
        self.assertEquals(game['OpponentCompletionPercentage'], 64.1)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_game_wrong_week(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('OAK', 'SD', 7, 2014)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_game_wrong_year(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('OAK', 'SD', 7, 2013)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_game_wrong_away_team(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('OAK', 'SDG', 7, 2014)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_game_wrong_home_team(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('SAC', 'SD', 7, 2014)

    @unittest.skip("skipping because no access to NFLDATA API")
    def test_get_game_with_bad_format(self):
        with self.assertRaises(Warning):
            self.data_handler.get_game('XXX', 'YYY', 25, 'a975')
