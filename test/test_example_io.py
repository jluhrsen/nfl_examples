from nfl_data.nfl_example_io import *
from nfl_data.nfl_example_maker import *
import unittest

__author__ = 'jamo'


class TestExampleIO(unittest.TestCase):
    def setUp(self):
        self.csv_file = '/tmp/csv_test_file.csv'
        self.maxDiff = None
        self.writer = nfl_example_io()

    def tearDown(self):
        pass

    def test_write_dict_as_csv(self):

        sample_dict_key_order = ["name", "coolnessfactor"]
        sample_dict = {sample_dict_key_order[0]: "jamo", sample_dict_key_order[1]: "100"}

        self.writer.write(sample_dict, sample_dict_key_order, self.csv_file, 'w')

        dict_as_read_from_csv_file = \
            self.writer.read(sample_dict_key_order, self.csv_file)[1]

        self.assertDictEqual(sample_dict, dict_as_read_from_csv_file)

    def test_one_off_for_specific_game(self):
        example = nfl_example_maker('ATL', 'WAS', 2009, 9)
        key_order = example.ordered_example_keys
        self.writer.create_header(key_order, self.csv_file)
        self.writer.write(example.example_data_dict, key_order, self.csv_file, 'a')

        self.assertDictEqual(example.example_data_dict, self.writer.read(key_order, self.csv_file)[1])

    def test_write_multiple_examples_as_csv(self):
        examples = [nfl_example_maker('NYJ', 'BAL', 2004, 10),
                    nfl_example_maker('PHI', 'DAL', 2001, 3),
                    nfl_example_maker('NYG', 'ATL', 1998, 6),
                    nfl_example_maker('DET', 'KC',  2007, 16)]

        key_order = examples[0].ordered_example_keys

        self.writer.create_header(key_order, self.csv_file)

        for i in range(len(examples)):
            self.writer.write(examples[i].example_data_dict, key_order, self.csv_file, 'a')

        dict_as_read_from_csv_file = \
            self.writer.read(key_order, self.csv_file)

        for i in range(len(examples)):
            # have to add one to the csv_file_dict because the first line is hdr
            self.assertDictEqual(examples[i].example_data_dict, dict_as_read_from_csv_file[i + 1])

    def test_write_file_with_wrong_mode(self):

        header_order = ['tim', 'buk', 'tu']

        matching_dict = {'tim': 'sweeny', 'buk': 'tooth', 'tu': 'pac'}

        with self.assertRaises(ValueError):
            self.writer.write(matching_dict, header_order, self.csv_file, 'j')
