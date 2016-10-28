import time

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
        self.season_examples_file = '../resources/data/' + str(season) + '_week_' + str(self.week) + '_examples.csv'
        self.writer = nfl_example_io()
        self.ordered_columns = ['Season', 'Week', 'HOMEteam', 'AWAYteam', 'HOMEscore', 'AWAYscore']

    def create(self):
    # TODO: there is no test for this function
        # get schedule for season
        # using self.season_stats_file create all examples for the season for
        # as much data as we have available.

        schedule = nfl_local_data_handler()
        season_matchups = schedule.get_schedule(self.season)

        season_examples = []
        for matchup in season_matchups:
            if (self.week != "ALL" and str(self.week) == matchup['Week']) or self.week == "ALL":
                ex = nfl_example_maker(matchup['HomeTeam'], matchup['AwayTeam'], self.season, int(matchup['Week']))
                print(matchup)
                season_examples.append(ex)

        # examples created for the first week do not make sense since there are no
        # previous weeks in order to make average stat calcs from.  Because of that
        # the ordered_example_keys of a first week example is not right.  we need
        # to use an example from week 2+
        key_order = []
        for i in range(len(season_examples)):
            if season_examples[i].week >= 2:
                key_order = season_examples[i].ordered_example_keys
                break

        key_order = self.rearrange_keys(key_order)

        # TODO: shouldn't we break out the writing of the data to file as a new function?
        self.writer.create_header(key_order, self.season_examples_file)

        for i in range(len(season_examples)):
            self.writer.write(season_examples[i].example_data_dict, key_order,
                              self.season_examples_file, 'a')

    def rearrange_keys(self, key_order):
        # rearranges the columns such that the order in self.ordered_columns comes first.  nothing else changes.
        new_key_order = self.ordered_columns
        for e in key_order:
            if e not in self.ordered_columns:
                new_key_order.append(e)

        return new_key_order

