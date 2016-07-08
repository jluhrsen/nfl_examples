import unittest

from nfl_data.dvoa_local_data_handler import dvoa_local_data_handler
from nfl_data.nfl_dvoa_stats import *

__author__ = 'jamo'


class TestDvoaRemote(unittest.TestCase):

    def setUp(self):
        self.data_handler = dvoa_data_server_handler()
        self.dvoa_stat = nfl_dvoa_stats()

    def test_get_dvoa_values01(self):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(8, 2014)
        off_dvoa = week_of_dvoas['CHI']['Offense DVOA']
        def_dvoa = week_of_dvoas['CHI']['Defense DVOA']
        st_dvoa = week_of_dvoas['CHI']['ST DVOA']

        self.assertEqual(off_dvoa, '3.3')
        self.assertEqual(def_dvoa, '5.8')
        self.assertEqual(st_dvoa, '-6.1')

    def test_get_dvoa_values02(self):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(15, 2012)
        off_dvoa = week_of_dvoas['OAK']['Offense DVOA']
        def_dvoa = week_of_dvoas['OAK']['Defense DVOA']
        st_dvoa = week_of_dvoas['OAK']['ST DVOA']
        w_off_dvoa = week_of_dvoas['OAK']['Weighted Offense DVOA']
        w_def_dvoa = week_of_dvoas['OAK']['Weighted Defense DVOA']
        w_st_dvoa = week_of_dvoas['OAK']['Weighted ST DVOA']

        self.assertEqual(off_dvoa, '-8.9')
        self.assertEqual(def_dvoa, '14.5')
        self.assertEqual(st_dvoa, '-4.8')
        self.assertEqual(w_off_dvoa, '-11.8')
        self.assertEqual(w_def_dvoa, '13.8')
        self.assertEqual(w_st_dvoa, '-2.5')
        # TODO: common work to get values and assert them.  put in to a function

    def test_one_off_for_sf_in_2009_week_09(self):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(9, 2009)

        off_dvoa = week_of_dvoas['SF']['Offense DVOA']
        def_dvoa = week_of_dvoas['SF']['Defense DVOA']
        st_dvoa = week_of_dvoas['SF']['ST DVOA']
        w_off_dvoa = week_of_dvoas['SF']['Weighted Offense DVOA']
        w_def_dvoa = week_of_dvoas['SF']['Weighted Defense DVOA']
        w_st_dvoa = week_of_dvoas['SF']['Weighted ST DVOA']

        msg = 'DVOA values not correct'

        self.assertEqual(off_dvoa, '-12.0', msg)
        self.assertEqual(def_dvoa, '-8.4', msg)
        self.assertEqual(st_dvoa, '-1.5', msg)
        self.assertEqual(w_off_dvoa, '-11.0', msg)
        self.assertEqual(w_def_dvoa, '-7.6', msg)
        self.assertEqual(w_st_dvoa, '-1.7', msg)

    def test_team_abbrev_conversion(self):
        team_name = self.dvoa_stat.convert_team_name('NWE', 2015)
        self.assertEqual('NE', team_name)
        team_name = self.dvoa_stat.convert_team_name('DEN', 2015)
        self.assertEqual('DEN', team_name)
        team_name = self.dvoa_stat.convert_team_name('OAK', 1991)
        self.assertEqual('LARD', team_name)


class TestDvoaLocal(unittest.TestCase):

    def setUp(self):
        self.data_handler = dvoa_local_data_handler()
        self.dvoa_stat = nfl_dvoa_stats(local_stats=True)

    def test_get_dvoa_values01(self):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(8, 2014)
        off_dvoa = week_of_dvoas['CHI']['Offense DVOA']
        def_dvoa = week_of_dvoas['CHI']['Defense DVOA']
        st_dvoa = week_of_dvoas['CHI']['ST DVOA']

        self.assertEqual(off_dvoa, '3.3')
        self.assertEqual(def_dvoa, '5.8')
        self.assertEqual(st_dvoa, '-6.1')

    def test_get_dvoa_values02(self):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(15, 2012)
        off_dvoa = week_of_dvoas['OAK']['Offense DVOA']
        def_dvoa = week_of_dvoas['OAK']['Defense DVOA']
        st_dvoa = week_of_dvoas['OAK']['ST DVOA']
        w_off_dvoa = week_of_dvoas['OAK']['Weighted Offense DVOA']
        w_def_dvoa = week_of_dvoas['OAK']['Weighted Defense DVOA']
        w_st_dvoa = week_of_dvoas['OAK']['Weighted ST DVOA']

        self.assertEqual(off_dvoa, '-8.9')
        self.assertEqual(def_dvoa, '14.5')
        self.assertEqual(st_dvoa, '-4.8')
        self.assertEqual(w_off_dvoa, '-11.8')
        self.assertEqual(w_def_dvoa, '13.8')
        self.assertEqual(w_st_dvoa, '-2.5')
        # TODO: common work to get values and assert them. put in to a function

    def test_one_off_for_sf_in_2009_week_09(self):
        week_of_dvoas = self.data_handler.get_dvoa_by_week_and_year(9, 2009)

        off_dvoa = week_of_dvoas['SFO']['Offense DVOA']
        def_dvoa = week_of_dvoas['SFO']['Defense DVOA']
        st_dvoa = week_of_dvoas['SFO']['ST DVOA']
        w_off_dvoa = week_of_dvoas['SFO']['Weighted Offense DVOA']
        w_def_dvoa = week_of_dvoas['SFO']['Weighted Defense DVOA']
        w_st_dvoa = week_of_dvoas['SFO']['Weighted ST DVOA']

        msg = 'DVOA values not correct'

        self.assertEqual(off_dvoa, '-12.0', msg + ": " + off_dvoa)
        self.assertEqual(def_dvoa, '-8.4', msg + ": " + def_dvoa)
        self.assertEqual(st_dvoa, '-1.5', msg + ": " + st_dvoa)
        self.assertEqual(w_off_dvoa, '-11.0', msg + ": " + w_off_dvoa)
        self.assertEqual(w_def_dvoa, '-7.6', msg + ": " + w_def_dvoa)
        self.assertEqual(w_st_dvoa, '-1.7', msg + ": " + w_st_dvoa)

    def test_team_abbrev_conversion(self):
        team_name = self.dvoa_stat.convert_team_name('NWE', 2015)
        self.assertEqual('NE', team_name)
        team_name = self.dvoa_stat.convert_team_name('DEN', 2015)
        self.assertEqual('DEN', team_name)
        team_name = self.dvoa_stat.convert_team_name('OAK', 1991)
        self.assertEqual('LARD', team_name)
        team_name = self.dvoa_stat.convert_team_name('SFO', 2009)
        self.assertEqual('SF', team_name)
