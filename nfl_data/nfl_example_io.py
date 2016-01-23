__author__ = 'jamo'

from nfl_data.nfl_team_season_history import *
from nfl_dvoa_stats import *
import collections
import csv

class nfl_example_io(object):

    def __init__(self):
        pass

    def create_header(self, header_keys, file):
        # if we are creating a header, going to assume we want a new file from
        # scratch
        with open(file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header_keys)
            writer.writeheader()

    def write(self, data, data_key_order, file, file_mode):
        if file_mode != 'w' and file_mode != 'a':
            raise ValueError('file_mode: ' + file_mode + ' incorrect')

        with open(file, file_mode) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data_key_order)

            if file_mode == 'w':
                writer.writeheader()

            writer.writerow(data)

    def read(self, data_key_order, file):
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=data_key_order)

            rows = {}
            for index, row in enumerate(reader):
                rows[index] = row

        return rows
