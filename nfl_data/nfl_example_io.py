import csv

__author__ = 'jamo'


class nfl_example_io(object):

    def __init__(self):
        pass

    @staticmethod
    def create_header(header_keys, file):
        # if we are creating a header, going to assume we want a new file from
        # scratch
        with open(file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header_keys)
            writer.writeheader()

    @staticmethod
    def write(data, data_key_order, file, file_mode):
        if file_mode != 'w' and file_mode != 'a':
            raise ValueError('file_mode: ' + file_mode + ' incorrect')

        with open(file, file_mode) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data_key_order)

            if file_mode == 'w':
                writer.writeheader()

            writer.writerow(data)

    @staticmethod
    def read(data_key_order, file):
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=data_key_order)

            rows = {}
            for index, row in enumerate(reader):
                rows[index] = row

        return rows
