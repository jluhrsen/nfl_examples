from nfl_data.nfl_team_season_history import *
from nfl_data.nfl_dvoa_stats import *
import collections

__author__ = 'jamo'


class nfl_example_maker(object):
    def __init__(self, home_team, away_team, season, week, stat_list_file=None):
        # the week passed in constructor is the week we are making the example
        # for so we do not include that week in the calculations for averages
        # etc.
        #
        # this also applies for retrieving dvoa values.  If the example we are
        # making is in week 8, then we want the dvoa values from week 7.
        #
        # WARNING:  there will be trouble making examples if team abrevs in
        # the data set are not consistent.  So, if NWE is used, it cannot be
        # sometimes used as NE.  another example would be KAN and KC.
        self.home_team = home_team
        self.away_team = away_team
        self.dvoa_home_team = nfl_dvoa_stats().convert_team_name(home_team, season)
        self.dvoa_away_team = nfl_dvoa_stats().convert_team_name(away_team, season)
        self.season = season
        self.week = week
        self.home_team_history = nfl_team_season_history()
        self.away_team_history = nfl_team_season_history()
        self.dvoa_stat_handler = nfl_dvoa_stats(local_stats=True)
        self.stat_list_file = stat_list_file

        # reminder, we don't want to include self.week's games, just "up to" that week.
        self.home_team_game_list = self.home_team_history.get_games_up_to_specific_week(home_team, season, week - 1)

        self.home_team_average_stats = self.home_team_history.calculate_averages(home_team, self.home_team_game_list,
                                                                                 stat_list_file)
        self.home_team_average_stats = self.append_string_to_dictionary_keys('HOME',
                                                                             self.home_team_average_stats.stat_dict)

        self.home_team_dvoa_stats = self.dvoa_stat_handler.get_dvoa_stat_dict(self.dvoa_home_team, season, week - 1)
        self.home_team_dvoa_stats = self.append_string_to_dictionary_keys('HOME',
                                                                          self.home_team_dvoa_stats)

        # reminder, we don't want to include self.week's games, just "up to" that week.
        self.away_team_game_list = self.away_team_history.get_games_up_to_specific_week(away_team, season, week - 1)

        self.away_team_average_stats = self.away_team_history.calculate_averages(away_team, self.away_team_game_list,
                                                                                 stat_list_file)
        self.away_team_average_stats = self.append_string_to_dictionary_keys('AWAY',
                                                                             self.away_team_average_stats.stat_dict)

        self.away_team_dvoa_stats = self.dvoa_stat_handler.get_dvoa_stat_dict(self.dvoa_away_team, season, week - 1)
        self.away_team_dvoa_stats = self.append_string_to_dictionary_keys('AWAY', self.away_team_dvoa_stats)

        self.example_data_dict = self.home_team_average_stats.copy()
        self.example_data_dict.update(self.home_team_dvoa_stats)
        self.example_data_dict.update(self.away_team_average_stats)
        self.example_data_dict.update(self.away_team_dvoa_stats)

        self.example_data_dict['HOMEteam'] = home_team
        self.example_data_dict['AWAYteam'] = away_team

        scores = self.home_team_history.get_score(home_team, away_team,
                                                  week, season)

        # storing scores as strings like everything else should be
        self.example_data_dict['HOMEscore'] = str(scores['HOMEscore'])
        self.example_data_dict['AWAYscore'] = str(scores['AWAYscore'])

        # will probably be nice to know week and season in each example
        self.example_data_dict['Week'] = str(self.week)
        self.example_data_dict['Season'] = str(self.season)

        self.example = collections.OrderedDict(sorted(self.example_data_dict.items()))

        self.ordered_example_keys = list(self.example.keys())

        # print('Example:\n\n' + str(self.example))

    @staticmethod
    def append_string_to_dictionary_keys(string, original_dict):
        """
        this actually will return a new dictionary with the same KV pair
        only prepending the given string to the key.
        :param string: string to prepend to key
        :param original_dict: dictionary to rework
        :return: new dictionary with modified key
        """
        new_dict = {}
        for k in original_dict.keys():
            new_dict[string + k] = original_dict[k]

        return new_dict

def pop_or_remove_unwanted_keys(list_or_dict):
    """
    will remove the elements from the list (by name) pop the entire KV from a dict
    """

    # TODO: need a unittest for this function

    if isinstance(list_or_dict, dict):
        list_or_dict.pop('HOMEteam')
        list_or_dict.pop('AWAYteam')
        list_or_dict.pop('Season')
        list_or_dict.pop('Week')
        list_or_dict.pop('HOMEscore')
        list_or_dict.pop('AWAYscore')
    elif isinstance(list_or_dict, list):
        list_or_dict.remove('HOMEteam')
        list_or_dict.remove('AWAYteam')
        list_or_dict.remove('Season')
        list_or_dict.remove('Week')
        list_or_dict.remove('HOMEscore')
        list_or_dict.remove('AWAYscore')
    else:
        raise Exception

    return list_or_dict