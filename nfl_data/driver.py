from nfl_data.nfl_in_season_examples import *
from nfl_data.nfl_example_io import *
from nfl_data.data_normalizer import *

__author__ = 'jamo'

for season in range(1998,2015):
    example_creator = nfl_in_season_examples(season)
    example_creator.create()


'''
# examples = []
# week = 17
# examples.append(nfl_example_maker("PIT", "SEA", 2015, week))

csv_file = '../resources/2015_playoff_predictionsOOPS.csv'
key_order = examples[0].ordered_example_keys
nfl_example_io().create_header(key_order, csv_file)


# for i in range(len(examples)):
#     print("working on home team: " + examples[i].example_data_dict['HOMEteam'])
#     print("working on away team: " + examples[i].example_data_dict['AWAYteam'])
#     nfl_example_io().write(examples[i].example_data_dict, key_order, csv_file, 'a')

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