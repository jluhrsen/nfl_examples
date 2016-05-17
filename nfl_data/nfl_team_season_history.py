from nfl_data.nfl_local_data_handler import *
from nfl_data.nfl_team_example_stats import *

__author__ = 'jamo'


class nfl_team_season_history(object):

    def __init__(self):
        # self.data_handler = nfl_data_server_handler()
        pass

    def get_games_up_to_specific_week(self, team, season, week):
        game_list = []
        season_schedule = nfl_local_data_handler().get_schedule(season)
        for game in season_schedule:
            if self.team_played_game(team, game) and week >= int(game['Week']):
                game_list.append(game)
        return game_list

    @staticmethod
    def team_played_game(team, game):
        """returns True if the given team participated in the given game
           returns False otherwise, including if the team had a BYE"""
        if game['HomeTeam'] == 'BYE' or game['AwayTeam'] == 'BYE':
            return False
        if game['HomeTeam'] == team or game['AwayTeam'] == team:
            return True
        return False

    @staticmethod
    def calculate_averages(team, game_list):
        average_stats = nfl_team_example_stats()
        for game in game_list:
            game_stats = nfl_local_data_handler().get_game(
                game['HomeTeam'], game['AwayTeam'], int(game['Week']), int(game['Season']))
            average_stats.increment_game_count()
            average_stats.include_stats_in_average(team, game_stats)

        return average_stats

    def get_score(self, home_team, away_team, week, season):
        game = nfl_local_data_handler().get_game(home_team, away_team, week, season)

        if game['Week'] == week and game['HomeOrAway'] == 'HOME':
            return {'HOMEscore': game['Score'],
                    'AWAYscore': game['OpponentScore']}
        else:
            return {'HOMEscore': game['OpponentScore'],
                    'AWAYscore': game['Score']}
