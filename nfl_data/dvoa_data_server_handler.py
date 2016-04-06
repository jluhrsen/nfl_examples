__author__ = 'jamo'

import os
import json
import requests

from bs4 import BeautifulSoup
from nfl_data.nfl_rest_repsonse_handler import *


class dvoa_data_server_handler(object):

    def __init__(self):
        self.base_url = 'http://www.footballoutsiders.com'
        # not sure how these cookie things work.  Took these values from the
        # scrape.php stuff on ll.net in the cookies.txt file.  but it's working
        # at this point (5/26/2015)
        #
        # ok, realized now that these cookies expire at some point and that the
        # scrape.php script is getting a new one when needed.  Need to figure
        # out how to do that here, but for now just run scrape.php and copy
        # those values from cookies.txt over here.
        # FIXME
        cookie_key = 'SESS6eb19ca60f8d07f8010b5d3a4118be7d'
        cookie_value = 'a1vnkfu9kq7bj5g7cs25o7tn26'
        self.cookies = {cookie_key : cookie_value}
        self.login_to_dvoa_site()

    def login_to_dvoa_site(self):

        payload = {'name' : 'jluhrsen',
                   'pass' : 'Tk421',
                   'form_id' : 'user_login',
                   'op' : 'Log in'}

        with requests.Session() as session:
            resp = session.post(self.base_url + '/user', data=payload,
                         cookies=self.cookies)

            assert(resp.status_code == 200), 'trouble logging in to FO. status code : %s' % resp.status_code

    def get_dvoa_by_week_and_year(self, week, year):
        with requests.Session() as session:
            full_url = \
                self.base_url + \
                '/premium/weekTeamSeasonDvoa.php?od=O&team=ARI&week=' + \
                str(week) + '&year=' + str(year)

            dvoa = session.get(full_url, cookies=self.cookies)
            return self.extract_dvoa_dict_from_response(dvoa.text)


    def extract_dvoa_dict_from_response(self, html_response):
        dvoa_dict = {}
        soup = BeautifulSoup(html_response, "html.parser")
        table = soup.find( "table", {"id":"dataTable"} )
        rows = table.find_all('tr')
        headers = []
        header_row = rows[0].find_all('th')
        for index, header in enumerate(header_row):
            if header.string.strip() == 'Rank':
                header = 'Rank' + str(index)
                headers.append(header)
            else:
                headers.append(str(header.string.strip()))
        for row in rows[1::]:
            columns = row.find_all('td')
            team = columns[0].string.strip()
            dvoa_dict[team] = {}
            for index, value in enumerate(columns[1::]):
                v = value.string.strip()
                v = v.replace('%', '')
                dvoa_dict[team][headers[index + 1]] = str(v)

        return dvoa_dict
