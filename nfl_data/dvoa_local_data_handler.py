import csv

__author__ = 'jamo'


class dvoa_local_data_handler(object):

    def __init__(self, dvoa_file='../resources/data/all_dvoa_stats.csv'):
        self.dvoa_csv_file = dvoa_file
        self.dvoa_headers, self.full_dvoa_set = self.read_dvoa_csv_file(self.dvoa_csv_file)

    def get_dvoa_by_week_and_year(self, week, year):
        dvoa_dict = {}
        for dvoa in self.full_dvoa_set:
            if dvoa['Week'] == str(week) and dvoa['Year'] == str(year):
                dvoa_dict[dvoa['Team']] = {}
                for header in self.dvoa_headers:
                    # dvoas probably come in format nn.nn0% so need to strip those trailing 0s and %
                    value = dvoa[header].rstrip("%")
                    value = value.rstrip("0")
                    # but if we stripped off a '0' when it was the only character after the '.' we need it back
                    if value[-1] == '.':
                        value += '0'
                    dvoa_dict[dvoa['Team']][header] = value

        return dvoa_dict

    @staticmethod
    def read_dvoa_csv_file(dvoa_file):
        dvoa_data_list = []
        with open(dvoa_file, "r") as data_file:
            reader = csv.DictReader(data_file)
            dvoa_headers = reader.fieldnames
            for line in reader:
                dvoa_data_list.append(line)

        return dvoa_headers, dvoa_data_list

