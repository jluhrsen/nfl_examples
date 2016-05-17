from nfl_data.nfl_local_data_handler import *
import unittest

__author__ = 'jamo'


class TestLocalDataHandler(unittest.TestCase):

    data_handler = nfl_local_data_handler()

    def test_get_local_data(self):
        game_list = self.data_handler.read_data_file_to_json()
        print(game_list[1])
        self.assertIn("PassingCompletions", game_list[0], 'did not contain PassingCompletions ')

    def test_get_schedules(self):
        for season in range(1985, 2015):
            schedule = self.data_handler.get_schedule(season)
            self.assertNotEqual([], schedule, 'schedule is empty')
            for i in schedule:
                self.assertEqual(i['Season'], str(season))

    def test_get_schedule_for_bad_year(self):
        with self.assertRaises(Warning):
            self.data_handler.get_schedule(1984)

    def test_get_schedule_with_bad_format(self):
        with self.assertRaises(ValueError):
            self.data_handler.get_schedule('shouldNotWork')

    def test_get_single_game(self):
        game = self.data_handler.get_game('OAK', 'SD', 6, 2014)
        self.assertEqual(game['Team'], 'SD')
        self.assertEqual(game['Opponent'], 'OAK')
        self.assertEquals(game['HomeOrAway'], 'AWAY')
        self.assertEquals(game['OpponentCompletionPercentage'], '52.9')
        self.assertEquals(game['CompletionPercentage'], '62.9')

    def test_get_game_wrong_week(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('OAK', 'SD', 7, 2014)

    def test_get_game_wrong_year(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('OAK', 'SD', 7, 2013)

    def test_get_game_wrong_away_team(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('OAK', 'SDG', 7, 2014)

    def test_get_game_wrong_home_team(self):
        with self.assertRaises(LookupError):
            self.data_handler.get_game('SAC', 'SD', 7, 2014)

'''
# TODO: in order to make this test work we need a class to verify team abrevs
    def test_get_game_with_bad_format(self):
        with self.assertRaises(Warning):
            self.data_handler.get_game('XXX', 'YYY', 25, 'a975')
'''