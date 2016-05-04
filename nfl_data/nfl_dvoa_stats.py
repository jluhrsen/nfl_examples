from nfl_data.dvoa_data_server_handler import *

__author__ = 'jamo'


class nfl_dvoa_stats(object):

    num_dvoa_stats = 3

    def __init__(self):
        self.off_dvoa = '0.0'
        self.def_dvoa = '0.0'
        self.st_dvoa = '0.0'
        self.data_handler = dvoa_data_server_handler()

    def get_dvoa_stat_dict(self, team, year, week):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(week, year)

        # dvoa data is not there for older games, so if it's not empty we'll
        # populate it, otherwise we can just take the zeros from __init__
        if bool(week_of_dvoas):
            self.off_dvoa = week_of_dvoas[team]['Offense DVOA']
            self.def_dvoa = week_of_dvoas[team]['Defense DVOA']
            self.st_dvoa = week_of_dvoas[team]['ST DVOA']

        return {'off_dvoa': self.off_dvoa, 'def_dvoa': self.def_dvoa,
                'st_dvoa': self.st_dvoa}

    def convert_team_name(self, team_name, year):
        if team_name == 'JAX':
            return 'JAC'
        if team_name == 'KAN':
            return 'KC'
        if team_name == 'NOR':
            return 'NO'
        if team_name == 'TAM':
            return 'TB'
        if team_name == 'GNB':
            return 'GB'
        if team_name == 'SDG':
            return 'SD'
        if team_name == 'NWE':
            return 'NE'
        if team_name == 'SFO':
            return 'SF'

        if 1991 <= year <= 1997:
            if team_name == 'HOU':
                return 'HOIL'
            if team_name == 'CLE':
                return 'CLE1'

        if 1991 <= year <= 1994:
            if team_name == 'OAK':
                return 'LARD'
            if team_name == 'STL':
                return 'LARM'

        return team_name
