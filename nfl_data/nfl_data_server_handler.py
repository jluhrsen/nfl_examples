import os
import json
import requests
import netrc
from nfl_data.nfl_rest_repsonse_handler import *

__author__ = 'jamo'


class nfl_data_server_handler(object):
    def __init__(self):
        self.base_url = 'https://api.fantasydata.net/v3/nfl/stats'
        self.data_format = 'JSON'
        self.data_resource = ''
        self.query_string = ''
        self.session = requests.Session()
        self.dev_key = None
        self.set_creds()

    def set_creds(self):
        secrets = netrc.netrc()
        user, account, self.dev_key, = secrets.authenticators(self.base_url)

    def get_response(self, resource, query):
        self.data_resource = resource
        self.query_string = query
        resp = self.session.get(self.generate_session_url())
        rest_response_validation(resp)
        return resp

    def generate_session_url(self):
        return self.base_url + '/' + self.data_format + '/' + self.data_resource + '/' + self.query_string

    def get_schedule(self, season):
        resp = self.get_response('Schedules', str(season))
        return json.loads(resp.text)

    def get_game(self, home_team, away_team, week, season):
        resp = self.get_response('TeamGameStats', str(season) + 'REG/' + str(week))
        for game in json.loads(resp.text):
            if game['HomeOrAway'] == 'HOME' and game['Team'] == home_team and game['Opponent'] == away_team:
                return game
        raise LookupError('trouble working on ' + home_team + ' ' + away_team + ' ' + str(week) + ' ' + str(season))

    def get_team_game_stats(self, week, season):
        self.data_resource = 'TeamGameStats'
        self.query_string = str(season) + '/' + str(week)
        headers = {'Ocp-Apim-Subscription-Key': self.dev_key}
        resp = self.session.get(self.generate_session_url(), headers=headers)

        return resp.content