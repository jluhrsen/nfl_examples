import csv

__author__ = 'jamo'


class nfl_local_data_handler(object):

    def __init__(self, data_file='../resources/data/1985-2015_gameData.csv'):
        self.data_file = data_file
        self.game_list = []

    def read_data_file_to_json(self):
        with open(self.data_file, "r") as csvDataFile:
            reader = csv.DictReader(csvDataFile)
            for game in reader:
                self.game_list.append(game)

        return self.game_list

    def get_schedule(self, season):

        if type(season) is not int:
            raise ValueError("expecting int for season argument: " + season)

        full_game_list = self.read_data_file_to_json()
        season_game_list = []
        for game in full_game_list:
            if game['Season'] == str(season):
                season_game_list.append(self.extract_schedule_details_from_full_game_info(game))

        if len(season_game_list) == 0:
            raise Warning("schedule list empty for season: " + str(season))

        return season_game_list

    def get_game(self, home_team, away_team, week, season):
        season_game_list = self.get_schedule(season)
        for game in season_game_list:
            if game['HomeOrAway'] == 'AWAY' and \
                                            game['Team'] == away_team and \
                                            game['Week'] == str(week) and \
                                            game['Opponent'] == home_team:
                return game

        raise LookupError('trouble working on ' + home_team + ' ' + away_team + ' ' + str(week) + ' ' + str(season))

    @staticmethod
    def extract_schedule_details_from_full_game_info(game):
        # need to just get the basic details and make keys easier to read.
        modified_game = game
        if game['HomeOrAway'] == 'AWAY':
            modified_game['AwayTeam'] = game['Team']
            modified_game['AwayScore'] = game['Score']
            modified_game['HomeTeam'] = game['Opponent']
            modified_game['HomeScore'] = game['OpponentScore']
        elif game['HomeOrAway'] == 'HOME':
            modified_game['AwayTeam'] = game['Opponent']
            modified_game['AwayScore'] = game['OpponentScore']
            modified_game['HomeTeam'] = game['Team']
            modified_game['HomeScore'] = game['Score']
        else:
            assert('trouble reading game ' + game)

        return modified_game
