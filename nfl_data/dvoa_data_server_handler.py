import netrc
import requests
from bs4 import BeautifulSoup

__author__ = 'jamo'


class dvoa_data_server_handler(object):
    def __init__(self):
        self.base_url = 'http://www.footballoutsiders.com'
        cookie_key = ''
        cookie_value = ''
        self.cookies = {cookie_key: cookie_value}
        self.username = ''
        self.password = ''
        self.set_creds()
        self.login_to_dvoa_site()

    def set_creds(self):
        secrets = netrc.netrc()
        self.username, account, self.password = secrets.authenticators(self.base_url)

    def login_to_dvoa_site(self):

        payload = {'name': self.username,
                   'pass': self.password,
                   'form_id': 'user_login',
                   'op': 'Log in'}

        with requests.Session() as session:
            session.get(self.base_url + '/user')
            resp = session.post(self.base_url + '/user', data=payload)
            self.cookies = session.cookies.get_dict()

            assert (resp.status_code == 200), 'trouble logging in to FO. status code : %s' % resp.status_code

    def get_dvoa_by_week_and_year(self, week, year):
        with requests.Session() as session:
            full_url = self.base_url + '/premium/weekTeamSeasonDvoa.php?od=O&team=ARI&week=' + \
                            str(week) + '&year=' + str(year)
            dvoa = session.get(full_url, cookies=self.cookies)
            # backup URL to at least get DVOA data for the team that occurred in the previous week.  Not as good
            # as the better URL that gives us the cumulative DVOA for the season UP to that week.
            # full_url = self.base_url + '/premium/oneWeek.php?od=O&year=' + str(year) + '&team=ARI&week=' + str(week)
            return self.extract_dvoa_dict_from_response(dvoa.text)

        # TODO: need a method that pulls all the dvoas and saves them locally, currently still using
        # scrape.php tool manually and pasting data in to dvoa .csv file

    @staticmethod
    def extract_dvoa_dict_from_response(html_response):
        dvoa_dict = {}
        soup = BeautifulSoup(html_response, "html.parser")
        table = soup.find("table", {"id": "dataTable"})
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
