__author__ = 'jamo'

from nfl_data.data_normalizer import *
import csv
import unittest

class TestDataNormalizer(unittest.TestCase):

    csv_data_file = '../resources/data/csvTestFile.csv'
    csv_min_max_file = '../resources/data/csvMinMaxTestFile.csv'
    number_of_csv_lines = 10
    number_of_csv_columns = 7

    def setUp(self):
        self.data_list = []
        with open(self.csv_data_file, "r") as data_file:
            reader = csv.DictReader(data_file)
            for line in reader:
                self.data_list.append(line)

    def test_csv_data_file_row_count(self):
        self.assertEqual(len(self.data_list), self.number_of_csv_lines)

    def test_csv_data_file_column_count(self):
        for line in self.data_list:
            self.assertEqual(len(line), self.number_of_csv_columns)

    def test_get_column_min_value(self):
        normalizer = data_normalizer()

        col_min = normalizer.get_column_min('col1', self.data_list)
        self.assertEqual(1,col_min)

        col_min = normalizer.get_column_min('col3', self.data_list)
        self.assertEqual(12,col_min)

    def test_get_column_max_value(self):
        normalizer = data_normalizer()

        col_max = normalizer.get_column_max('col7', self.data_list)
        self.assertEqual(10,col_max)

        col_max = normalizer.get_column_max('col2', self.data_list)
        self.assertEqual(80,col_max)

    def test_normalize_column(self):
        normalizer = data_normalizer()

        normalized_data = normalizer.normalize_data(self.data_list)

        self.assertAlmostEqual(0.6363636364, normalized_data[0]['col3'])
        self.assertAlmostEqual(0.0, normalized_data[1]['col3'])
        self.assertAlmostEqual(0.2727272727, normalized_data[2]['col3'])
        self.assertAlmostEqual(0.1818181818, normalized_data[3]['col3'])
        self.assertAlmostEqual(0.6363636364, normalized_data[4]['col3'])
        self.assertAlmostEqual(0.4545454545, normalized_data[5]['col3'])
        self.assertAlmostEqual(0.4545454545, normalized_data[6]['col3'])
        self.assertAlmostEqual(1.0, normalized_data[7]['col3'])
        self.assertAlmostEqual(0.6363636364, normalized_data[8]['col3'])
        self.assertAlmostEqual(0.6363636364, normalized_data[9]['col3'])
        self.assertAlmostEqual(0.25, normalized_data[0]['col6'])
        self.assertAlmostEqual(0.25, normalized_data[1]['col6'])
        self.assertAlmostEqual(0.625, normalized_data[2]['col6'])
        self.assertAlmostEqual(0.0, normalized_data[3]['col6'])
        self.assertAlmostEqual(0.75, normalized_data[4]['col6'])
        self.assertAlmostEqual(0.375, normalized_data[5]['col6'])
        self.assertAlmostEqual(1.0, normalized_data[6]['col6'])
        self.assertAlmostEqual(0.625, normalized_data[7]['col6'])
        self.assertAlmostEqual(0.375, normalized_data[8]['col6'])
        self.assertAlmostEqual(1.0, normalized_data[9]['col6'])
        self.assertAlmostEqual(1.0, normalized_data[0]['col7'])
        self.assertAlmostEqual(0.8888888889, normalized_data[1]['col7'])
        self.assertAlmostEqual(0.7777777778, normalized_data[2]['col7'])
        self.assertAlmostEqual(0.6666666667, normalized_data[3]['col7'])
        self.assertAlmostEqual(0.5555555556, normalized_data[4]['col7'])
        self.assertAlmostEqual(0.4444444444, normalized_data[5]['col7'])
        self.assertAlmostEqual(0.3333333333, normalized_data[6]['col7'])
        self.assertAlmostEqual(0.2222222222, normalized_data[7]['col7'])
        self.assertAlmostEqual(0.1111111111, normalized_data[8]['col7'])
        self.assertAlmostEqual(0.0, normalized_data[9]['col7'])

    def test_normalize_with_min_max_file(self):
        normalizer = data_normalizer()

        normalized_data = normalizer.normalize_data_with_min_max_file(self.data_list, self.csv_min_max_file)

        self.assertAlmostEqual(0.0909090909, normalized_data[0]['col1'])
        self.assertAlmostEqual(0.1818181818, normalized_data[1]['col1'])
        self.assertAlmostEqual(0.2727272727, normalized_data[2]['col1'])
        self.assertAlmostEqual(0.3636363636, normalized_data[3]['col1'])
        self.assertAlmostEqual(0.4545454545, normalized_data[4]['col1'])
        self.assertAlmostEqual(0.5454545455, normalized_data[5]['col1'])
        self.assertAlmostEqual(0.6363636364, normalized_data[6]['col1'])
        self.assertAlmostEqual(0.7272727273, normalized_data[7]['col1'])
        self.assertAlmostEqual(0.8181818182, normalized_data[8]['col1'])
        self.assertAlmostEqual(0.9090909091, normalized_data[9]['col1'])
        self.assertAlmostEqual(1.0, normalized_data[0]['col7'])
        self.assertAlmostEqual(0.5714285714, normalized_data[4]['col7'])
        self.assertAlmostEqual(0.0, normalized_data[9]['col7'])
