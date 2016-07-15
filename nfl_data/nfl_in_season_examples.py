from nfl_data.nfl_example_io import *
from nfl_data.nfl_example_maker import *

__author__ = 'jamo'


class nfl_in_season_examples(object):
    """
           Class to create all examples in a given season and write to a file.
    """

    def __init__(self, season=2014, week=-1):

        self.week = week
        if self.week == -1:
            self.week = "ALL"
        self.season = season
        self.season_examples_file = '../resources/data/' + str(season) + '_weeks_' + str(self.week) + '_examples.csv'
        self.writer = nfl_example_io()

    def create(self):
        # get schedule for season
        # using self.season_stats_file create all examples for the season for
        # as much data as we have available.

        schedule = nfl_local_data_handler()
        season_matchups = schedule.get_schedule(self.season)

        season_examples = []
        for matchup in season_matchups:
            ex = nfl_example_maker(matchup['HomeTeam'], matchup['AwayTeam'], self.season, int(matchup['Week']))
            if self.week != "ALL" and str(self.week) == matchup['Week']:
                print(matchup)
                season_examples.append(ex)
            elif self.week == "ALL":
                print(matchup)
                season_examples.append(ex)
            # TODO: one efficiency would be to break this loop once we know we have found and finished matchups for
            # for the given week.

        # examples created for the first week do not make sense since there are no
        # previous weeks in order to make average stat calcs from.  Because of that
        # the ordered_example_keys of a first week example is not right.  we need
        # to use an example from week 2+
        key_order = []
        for i in range(len(season_examples)):
            if season_examples[i].week >= 2:
                key_order = season_examples[i].ordered_example_keys
                break

        self.writer.create_header(key_order, self.season_examples_file)

        for i in range(len(season_examples)):
            self.writer.write(season_examples[i].example_data_dict, key_order,
                              self.season_examples_file, 'a')
