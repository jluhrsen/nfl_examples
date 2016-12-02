import os

from nfl_data.nfl_in_season_examples import *
from nfl_data.nfl_example_io import *
from nfl_data.data_normalizer import *

__author__ = 'jamo'

'''
# this loop can create examples in bulk.
for season in range(2016, 2017):
    example_creator = nfl_in_season_examples(season)
    example_creator.create()
'''

#STEPS:
# 0 - update week variable accordingly
# 1 - go get data file and copy last week's games to all season game data file
# 2 - get dvoa data
# 3 - ensure team abrev. are consistent with the rest of the data file
# 4 - go run your java to process this normalized file with trained nets


def pop_or_remove_unwanted_keys(list_or_dict):
    """
    will remove the elements from the list (by name) pop the entire KV from a dict
    """

    if isinstance(list_or_dict, dict):
        list_or_dict.pop('HOMEteam')
        list_or_dict.pop('AWAYteam')
        list_or_dict.pop('Season')
        list_or_dict.pop('Week')
        list_or_dict.pop('HOMEscore')
        list_or_dict.pop('AWAYscore')
    elif isinstance(list_or_dict, list):
        list_or_dict.remove('HOMEteam')
        list_or_dict.remove('AWAYteam')
        list_or_dict.remove('Season')
        list_or_dict.remove('Week')
        list_or_dict.remove('HOMEscore')
        list_or_dict.remove('AWAYscore')
    else:
        raise Exception

    return list_or_dict

examples = []
week = 13
season = 2016
example_creator = nfl_in_season_examples(season, week)
example_creator.create()

# the normal example file uses season, week, home, away as column headers but those are only for readability.  They
# are not needed for any inputs or outputs, so ignoring them here when creating the normalized data which is explicitly
# used for input/output.
key_order = example_creator.season_examples[0].ordered_example_keys
key_order = example_creator.rearrange_keys(key_order)
key_order = pop_or_remove_unwanted_keys(key_order)

raw_data_file = '../resources/data/trimmed_examples.csv'
try:
    os.remove(raw_data_file)
except OSError:
    pass

writer = nfl_example_io()
data_list = []

with open(example_creator.season_examples_file, "r") as example_file:
    reader = csv.DictReader(example_file)
    for line in reader:
        # we don't want certain KVs here (e.g. HOMEteam, AWAYscore, etc)
        line = pop_or_remove_unwanted_keys(line)
        writer.write(line, key_order, raw_data_file, 'a')
        data_list.append(line)

# TODO: need to recreate this file using existing data so as to not miss any new max or min values that may
# have come in 2015 or 2016, since it was created only using data up to 2014
min_max_file = '../resources/data/all_examples_with_dvoa_no_teams_normalized_min_max.csv'

# this will churn through all the data and create a normalized data set
normalizer = data_normalizer()
normalized_data = normalizer.normalize_data_with_min_max_file(data_list, min_max_file)

normalized_data_file = '../resources/2016_examples_normalized.csv'

writer = nfl_example_io()
writer.create_header(key_order, normalized_data_file)

for i in range(len(normalized_data)):
    writer.write(normalized_data[i], key_order, normalized_data_file, 'a')



