import os
import json
import requests
from nfl_data.nfl_rest_repsonse_handler import *

__author__ = 'jamo'


class nfl_data_server_handler(object):
    def __init__(self):
        self.base_url = 'http://api.nfldata.apiphany.com/developer'
        self.data_format = 'json'
        self.data_resource = ''
        self.query_string = ''
        self.dev_key = os.environ['NFL_DATA_DEVELOPER_KEY']
        self.session = requests.Session()

    def get_response(self, resource, query):
        self.data_resource = resource
        self.query_string = query
        self.generate_session_url()
        resp = self.session.get(self.session.url)
        rest_response_validation(resp)
        return resp

    def generate_session_url(self):
        self.session.url = self.base_url + '/' + self.data_format + '/' + self.data_resource + '/' + self.query_string \
                           + '?key=' + self.dev_key

    def get_schedule(self, season):
        resp = self.get_response('Schedules', str(season))
        return json.loads(resp.text)

    def get_game(self, home_team, away_team, week, season):
        resp = self.get_response('TeamGameStats', str(season) + 'REG/' + str(week))
        for game in json.loads(resp.text):
            if game['HomeOrAway'] == 'HOME' and game['Team'] == home_team and game['Opponent'] == away_team:
                return game
        raise LookupError('trouble working on ' + home_team + ' ' + away_team + ' ' + str(week) + ' ' + str(season))
