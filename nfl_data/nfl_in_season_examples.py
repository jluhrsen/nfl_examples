from nfl_data.nfl_example_io import *
from nfl_data.nfl_example_maker import *

__author__ = 'jamo'


class nfl_in_season_examples(object):

    def __init__(self, season=2014):

        self.season = season
        # can delete below if things are ok.  moved data file to nfl_local_data_handler class
        # self.season_stats_file = '../resources/data/1985-2015_gameData.csv'
        self.season_examples_file = '../resources/data/' + str(season) + '_examples.csv'
        self.writer = nfl_example_io()

    def create(self):
        # get schedule for season
        # using self.season_stats_file create all examples for the season for
        #   as much data as we have available.

        schedule = nfl_local_data_handler()
        # can delete below if things are ok.  moved data file to nfl_local_data_handler class
        # schedule.data_file = self.season_stats_file

        season_matchups = schedule.get_schedule(self.season)

        season_examples = []
        for matchup in season_matchups:
            print(matchup)
            ex = nfl_example_maker(matchup['HomeTeam'], matchup['AwayTeam'], self.season, int(matchup['Week']))
            season_examples.append(ex)

        # examples created for the first week do not make sense since there are no
        # previous weeks in order to make average stat calcs from.  Because of that
        # the ordered_example_keys of a first week example is not right.  we need
        # to use an example from week 2+
        for i in range(len(season_examples)):
            if season_examples[i].week >= 2:
                key_order = season_examples[i].ordered_example_keys
                break

        self.writer.create_header(key_order, self.season_examples_file)

        for i in range(len(season_examples)):
            self.writer.write(season_examples[i].example_data_dict, key_order,
                              self.season_examples_file, 'a')

        dict_as_read_from_csv_file = \
            self.writer.read(key_order, self.season_examples_file)
