from nfl_data.nfl_team_season_history import *
import unittest

__author__ = 'jamo'


class TestTeamHistory(unittest.TestCase):

    def setUp(self):
        self.team_history = nfl_team_season_history()

    def tearDown(self):
        del self.team_history

    def test_number_of_games_when_no_bye(self):
        """packers in 2012 had bye in week 10"""
        game_list = \
            self.team_history.get_games_up_to_specific_week('GB', 2012, 9)
        self.assertEqual(len(game_list), 9)

    def test_number_of_games_with_bye(self):
        """jets in 2011 had bye in week 8"""
        game_list = \
            self.team_history.get_games_up_to_specific_week('NYJ', 2011, 11)
        self.assertEqual(len(game_list), 10)

    def test_average_stat_calculation(self):
        team = 'OAK'
        game_list = \
            self.team_history.get_games_up_to_specific_week(team, 2001, 4)
        average_stats = \
            self.team_history.calculate_averages(team, game_list)
        self.assertEqual(average_stats.ScoreQuarter1, 5.75)
        self.assertEqual(average_stats.PassingCompletions, 22.0)
        self.assertEqual(average_stats.OpponentPassingCompletions, 18.0)
        self.assertEqual(average_stats.FirstDowns, 18.75)
        self.assertEqual(average_stats.OpponentFirstDowns, 18.25)
        self.assertEqual(average_stats.Takeaways, 2.0)
        self.assertEqual(average_stats.OpponentTakeaways, 1.5)

    def test_average_stat_calculation_with_bad_team_name(self):
        team = 'OAK'
        game_list = \
            self.team_history.get_games_up_to_specific_week(team, 2001, 4)
        team = 'NOTOAK'
        with self.assertRaises(ValueError):
            self.team_history.calculate_averages(team, game_list)
