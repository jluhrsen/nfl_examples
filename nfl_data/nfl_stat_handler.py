__author__ = 'jamo'

from nfl_data.nfl_team_example_stats import *

class nfl_stat_handler(object):

    stat_info = {}

    def __init__(self, stat_name, stat_value):

        self.stat_info['name'] = stat_name
        # self.stat_info['value'] = stat_value
        self.stat_info['value'] = self.massage_value_as_needed(stat_name, stat_value)

    def massage_value_as_needed(self, name, value):
        if 'TimeOfPossession' == name or \
                'OpponentTimeOfPossession' == name:
            # print('taking a look at ' + str(value) + ' for ' + name)
            value = self.convert_top_to_seconds(value)

        return value

    def convert_top_to_seconds(self, mins_and_secs):
        mins = mins_and_secs.split(":")[0]
        secs = mins_and_secs.split(":")[1]
        total_secs = (int(mins) * 60) + int(secs)
        return str(total_secs)



