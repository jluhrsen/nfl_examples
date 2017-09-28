__author__ = 'jamo'


class nfl_stat_list_from_file(object):
    def __init__(self, stat_list_file):
        self.stat_list_file = stat_list_file
        self.stat_list = read_stat_list_file(self.stat_list_file)

def read_stat_list_file(file_to_read):
    file = open(file_to_read, 'r')
    stat_list = file.read().splitlines()
    return stat_list