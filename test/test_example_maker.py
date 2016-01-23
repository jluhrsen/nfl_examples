__author__ = 'jamo'

from nfl_data.nfl_example_maker import *
from nfl_data.nfl_team_example_stats import *
from nfl_data.nfl_dvoa_stats import *
import unittest

class TestExampleMaker(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example_has_right_data_size(self):
        '''
        example should be the size of both teams history + two for the
        score + any more for other items (e.g. DVOA, line, OU, weather...
        '''

        stats_for_example = nfl_team_example_stats()

        number_of_dvoa_stats = nfl_dvoa_stats.num_dvoa_stats

        number_of_stats_expected = \
            len(stats_for_example.stats_to_average) * 2
        number_of_stats_expected += number_of_dvoa_stats * 2
        number_of_stats_expected += 2 # for expected score
        number_of_stats_expected += 2 # for home and away team

        example = nfl_example_maker('SF', 'SEA', 2014, 13)
        # print example.example
        number_of_stats_found = len(example.example_data_dict)

        self.assertEqual(number_of_stats_expected, number_of_stats_found)

    def test_time_of_possession(self):
        example = nfl_example_maker('NYG', 'ATL', 1998, 6)

        expected_home_top = '1660.0'
        expected_home_opp_top = '1940.0'
        expected_away_top = '1976.25'
        expected_away_opp_top = '1623.75'
        actual_home_top = example.example_data_dict['HOMETimeOfPossession']
        self.assertEquals(expected_home_top, actual_home_top)
        actual_home_opp_top = example.example_data_dict['HOMEOpponentTimeOfPossession']
        self.assertEquals(expected_home_opp_top, actual_home_opp_top)
        actual_away_opp_top = example.example_data_dict['AWAYOpponentTimeOfPossession']
        self.assertEquals(expected_away_opp_top, actual_away_opp_top)
        actual_away_top = example.example_data_dict['AWAYTimeOfPossession']
        self.assertEquals(expected_away_top, actual_away_top)

    def test_examples_with_missing_stats(self):
        example = nfl_example_maker('NYG', 'ATL', 1998, 6)
        if 'None' in example.example_data_dict.values() or \
            None in example.example_data_dict.values():
            self.fail('found a none in here man!')

    def test_verify_dvoa_stats_in_example(self):
        example = nfl_example_maker('CHI', 'BUF', 2006, 5)

        h_def = example.example_data_dict['HOMEdef_dvoa']
        h_st = example.example_data_dict['HOMEst_dvoa']
        h_off = example.example_data_dict['HOMEoff_dvoa']
        a_def = example.example_data_dict['AWAYdef_dvoa']
        a_st = example.example_data_dict['AWAYst_dvoa']
        a_off = example.example_data_dict['AWAYoff_dvoa']

        self.assertEqual(h_def, '-30.2')
        self.assertEqual(h_st, '10.8')
        self.assertEqual(h_off, '15.3')
        self.assertEqual(a_def, '6.2')
        self.assertEqual(a_st, '0.0')
        self.assertEqual(a_off, '-9.0')

    def test_team_names_in_csv_line(self):
        example = nfl_example_maker('TAM', 'MIA', 1988, 9)

        self.assertEqual('TAM', example.example_data_dict['HOMEteam'])
        self.assertEqual('MIA', example.example_data_dict['AWAYteam'])

    def test_final_score_in_example(self):
        example = nfl_example_maker('OAK', 'DEN', 1985, 12)

        self.assertEqual('31', example.example_data_dict['HOMEscore'])
        self.assertEqual('28', example.example_data_dict['AWAYscore'])
