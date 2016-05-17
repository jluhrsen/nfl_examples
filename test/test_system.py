from nfl_data.nfl_example_io import *
from nfl_data.nfl_example_maker import *
import unittest

__author__ = 'jamo'


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.csv_file = '/tmp/csv_test_file.csv'
        self.week_num = 9
        self.season = 2009
        self.examples = []
        self.schedule = nfl_local_data_handler().get_schedule(self.season)

    def tearDown(self):
        pass

    # @unittest.skip("skipping because THIS TAKES FOREVER!")
    def test_examples_for_one_week_in_one_season(self):

        # loop through each game a of particular week and
        # create example for each game and write to csv

        for game in self.schedule:
            if game['Week'] == str(self.week_num):
                home_team = game['HomeTeam']
                away_team = game['AwayTeam']
                if home_team != 'BYE' and away_team != 'BYE':
                    example = \
                       nfl_example_maker(home_team, away_team, self.season, self.week_num)
                    self.examples.append(example)

        key_order = self.examples[0].ordered_example_keys

        writer = nfl_example_io()
        writer.create_header(key_order, self.csv_file)

        for i in range(len(self.examples)):
            writer.write(self.examples[i].example_data_dict, key_order,
                         self.csv_file, 'a')
