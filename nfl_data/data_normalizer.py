__author__ = 'jamo'

import csv
import sys

class data_normalizer(object):

    def __init__(self):
        pass

    def get_column_min(self, col_name, data):
        """Finds the minimum value for the column found in data under the given col_name

        Args:
            col_name (string): heading to use in data for searching min
            data (list of float-castable entries): data to search

        Returns:
            float: the smallest value in data set under heading col_name
        """

        min = sys.float_info.max
        for row in data:
            if float(row[col_name]) <= min:
                min = float(row[col_name])

        return min

    def get_column_max(self, col_name, data):
        """Finds the maximum value for the column found in data under the given col_name

        Args:
            col_name (string): heading to use in data for searching max
            data (list of float-castable entries): data to search

        Returns:
            float: the largest value in data set under heading col_name
        """
        max = sys.float_info.min
        for row in data:
            if float(row[col_name]) >= max:
                max = float(row[col_name])

        return max

    def normalize_data(self, data):
        normalized_data = []

        for row in data:
            normalized_row = {}
            for key in row.keys():
                min = self.get_column_min(key, data)
                max = self.get_column_max(key, data)
                key_value = float(row[key])
                normalized_value = (key_value - min) / (max - min)
                normalized_row[key] = normalized_value
            normalized_data.append(normalized_row)

        return normalized_data

    def normalize_data_with_min_max_file(self, data, min_max_file):
        normalized_data = []

        min_dict = {}
        max_dict = {}

        # min_max file should have line 1 as the header.  line 2 contains
        # the min value for that column from the data set used for training
        # and line 3 contains the max.
        with open(min_max_file, "r") as mm_file:
            reader = csv.DictReader(mm_file)
            for line in reader:
                if reader.line_num == 2:
                    min_dict = line
                if reader.line_num == 3:
                    max_dict = line

        for row in data:
            normalized_row = {}
            for key in row.keys():
                key_value = float(row[key])
                min = float(min_dict[key])
                max = float(max_dict[key])
                normalized_value = (key_value - min) / (max - min)
                # this function is probably being used to normalize data that wasn't
                # used to normalize some other data set where the min and max came from.
                # It's possible that some
                # values are above or below the max or min of the original data set
                # which would make their normalized values > 1.0 or < 0.0.  We need
                # to account for that and only allow 1.0 and 0.0 to be the max and min
                if normalized_value > 1.0:
                    normalized_value = 1.0
                if normalized_value < 0.0:
                    normalized_value = 0.0
                normalized_row[key] = normalized_value

            normalized_data.append(normalized_row)

        return normalized_data




