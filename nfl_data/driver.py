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
# 0 - update week, season values accordingly
# 0.1 - get dvoa data
# 1 - go get data file and copy last week's games to all season game data file
# 2 - rename team names with proper abrev (might just be a problem with LARM)
# 3 - run this driver with write_to_file = True
# 4 - take resulting examples file and trim out leading columns and save
# 5 - make sure this same resulting examples file has values for the outputs (home/away score).  0 is fine
#     name this file "trimmed_examples.csv" - raw_data_file variable below
# 6 - run this driver again, can put write_to_file = False if you want
# 7 - remove header from resulting normalized example file.
# 8 - remove AWAYScore and HOMEScore columns from same resulting normalized example file
# 9 - go run your java to process this normalized file with trained nets



examples = []
week = 11
season = 2016
example_creator = nfl_in_season_examples(season, week)
example_creator.write_to_file = False
example_creator.create()

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
# are not needed for any inputs or outputs, so ignoring them here when creating the normalized data which is explicitly
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