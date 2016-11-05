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


examples = []
week = 9
season = 2016
example_creator = nfl_in_season_examples(season, week)
example_creator.write_to_file = False
example_creator.create()

# TODO: need to remove non-input columns from csv_output_file.  manual step for now to turn it in to this:
raw_data_file = '../resources/data/trimmed_examples.csv'

normalized_data_file = '../resources/2016_examples_normalized.csv'

# TODO: need to recreate this file using existing data so as to not miss any new max or min values that may
# have come in 2015 or 2016, since it was created only using data up to 2014
min_max_file = '../resources/data/all_examples_with_dvoa_no_teams_normalized_min_max.csv'

data_list = []

with open(raw_data_file, "r") as data_file:
    reader = csv.DictReader(data_file)
    for line in reader:
        data_list.append(line)

# this will churn through all the data and create a normalized data set
# normalized_data = normalizer.normalize_data(data_list)
normalizer = data_normalizer()
normalized_data = normalizer.normalize_data_with_min_max_file(data_list, min_max_file)

# the normal example file uses season, week, home, away as column headers but those are only for readability.  They
# are not needed for any iYputs or outputs, so ignoring them here when creating the normalized data which is explicitly
# used for input/output.
key_order = example_creator.season_examples[0].ordered_example_keys
key_order.remove('HOMEteam')
key_order.remove('AWAYteam')
key_order.remove('Season')
key_order.remove('Week')

writer = nfl_example_io()
writer.create_header(key_order, normalized_data_file)

for i in range(len(normalized_data)):
    writer.write(normalized_data[i], key_order, normalized_data_file, 'a')

# TODO: another manual step here is to remove the HOMEscore and AWAYscore columns from this new normalized
# file because the current nets don't expect it.

'''
# examples.append(nfl_example_maker("PIT", "SEA", 2015, week))

csv_output_file = '../resources/2015_playoff_predictionsOOPS.csv'
key_order = examples[0].ordered_example_keys
nfl_example_io().create_header(key_order, csv_output_file)


# for i in range(len(examples)):

#     nfl_example_io().write(examples[i].example_data_dict, key_order, csv_output_file, 'a')

raw_data_file = '../resources/2015_playoff_predictions.csv'
normalized_data_file = '../resources/2015_playoff_predictions_normalized.csv'
min_max_file = '../resources/data/all_examples_with_dvoa_no_teams_normalized_min_max.csv'

data_list = []

with open(raw_data_file, "r") as data_file:
    reader = csv.DictReader(data_file)
    for line in reader:
        data_list.append(line)

normalizer = data_normalizer()

# this will churn through all the data and create a normalized data set
# normalized_data = normalizer.normalize_data(data_list)

normalized_data = normalizer.normalize_data_with_min_max_file(data_list, min_max_file)

# mins = {}
# maxs = {}
#
# for header in data_list[0].keys():
#     mins[header] = normalizer.get_column_min(header, data_list)
#     maxs[header] = normalizer.get_column_max(header, data_list)
#     if 'AWAYscore' == header or 'HOMEscore' == header:
#         print(header + str(mins[header]))
#         print(header + str(maxs[header]))

# get known good example so I can know the keys and can write the normalized
# data to it's file in that same order
example = nfl_example_maker('ATL', 'WAS', 2009, 9)
key_order = example.ordered_example_keys

writer = nfl_example_io()

writer.create_header(key_order, normalized_data_file)

for i in range(len(normalized_data)):
    writer.write(normalized_data[i], key_order, normalized_data_file, 'a')

# to create min max file automatically
# writer.create_header(key_order, min_max_file)
# writer.write(mins, key_order, min_max_file, 'a')
# writer.write(maxs, key_order, min_max_file, 'a')

'''