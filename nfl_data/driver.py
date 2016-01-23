import time

__author__ = 'jamo'

from nfl_in_season_examples import *
from nfl_data.nfl_team_season_history import *
from nfl_data.nfl_example_io import *

'''
for season in range(1998,2015):
    example_creator = nfl_in_season_examples(season)
    example_creator.create()
'''

# example_creator = nfl_in_season_examples(2015)
# example_creator.create()

afc_playoff_teams = ['DEN', 'NE', 'CIN', 'HOU', 'KC', 'PIT']
nfc_playoff_teams = ['CAR', 'ARI', 'MIN', 'WAS', 'GB', 'SEA']

examples = []
week = 17
'''
examples.append(nfl_example_maker("DEN","NE", 2015, week))
examples.append(nfl_example_maker("DEN","CIN", 2015, week))
examples.append(nfl_example_maker("DEN","HOU", 2015, week))
examples.append(nfl_example_maker("DEN","KC", 2015, week))
examples.append(nfl_example_maker("DEN","PIT", 2015, week))

examples.append(nfl_example_maker("NE","CIN", 2015, week))
examples.append(nfl_example_maker("NE","HOU", 2015, week))
examples.append(nfl_example_maker("NE","KC", 2015, week))
examples.append(nfl_example_maker("NE","PIT", 2015, week))

examples.append(nfl_example_maker("CIN","HOU", 2015, week))
examples.append(nfl_example_maker("CIN","KC", 2015, week))
examples.append(nfl_example_maker("CIN","PIT", 2015, week))

examples.append(nfl_example_maker("HOU","KC", 2015, week))

examples.append(nfl_example_maker("CAR","ARI", 2015, week))
examples.append(nfl_example_maker("CAR","MIN", 2015, week))
examples.append(nfl_example_maker("CAR","WAS", 2015, week))
examples.append(nfl_example_maker("CAR","GB", 2015, week))
examples.append(nfl_example_maker("CAR","SEA", 2015, week))

examples.append(nfl_example_maker("ARI","MIN", 2015, week))
examples.append(nfl_example_maker("ARI","WAS", 2015, week))
examples.append(nfl_example_maker("ARI","GB", 2015, week))
examples.append(nfl_example_maker("ARI","SEA", 2015, week))

examples.append(nfl_example_maker("MIN","WAS", 2015, week))
examples.append(nfl_example_maker("MIN","GB", 2015, week))
examples.append(nfl_example_maker("MIN","SEA", 2015, week))

examples.append(nfl_example_maker("WAS","GB", 2015, week))

examples.append(nfl_example_maker('CAR','DEN', 2015, week ))
examples.append(nfl_example_maker('ARI','DEN', 2015, week ))
examples.append(nfl_example_maker('MIN','DEN', 2015, week ))
examples.append(nfl_example_maker('WAS','DEN', 2015, week ))
examples.append(nfl_example_maker('GB','DEN', 2015, week ))
examples.append(nfl_example_maker('SEA','DEN', 2015, week ))
examples.append(nfl_example_maker('CAR','NE', 2015, week ))
examples.append(nfl_example_maker('ARI','NE', 2015, week ))
examples.append(nfl_example_maker('MIN','NE', 2015, week ))
examples.append(nfl_example_maker('WAS','NE', 2015, week ))
examples.append(nfl_example_maker('GB','NE', 2015, week ))
examples.append(nfl_example_maker('SEA','NE', 2015, week ))
examples.append(nfl_example_maker('CAR','CIN', 2015, week ))
examples.append(nfl_example_maker('ARI','CIN', 2015, week ))
examples.append(nfl_example_maker('MIN','CIN', 2015, week ))
examples.append(nfl_example_maker('WAS','CIN', 2015, week ))
examples.append(nfl_example_maker('GB','CIN', 2015, week ))
examples.append(nfl_example_maker('SEA','CIN', 2015, week ))
examples.append(nfl_example_maker('CAR','HOU', 2015, week ))
examples.append(nfl_example_maker('ARI','HOU', 2015, week ))
examples.append(nfl_example_maker('MIN','HOU', 2015, week ))
examples.append(nfl_example_maker('WAS','HOU', 2015, week ))
examples.append(nfl_example_maker('GB','HOU', 2015, week ))
examples.append(nfl_example_maker('SEA','HOU', 2015, week ))
examples.append(nfl_example_maker('CAR','KC', 2015, week ))
examples.append(nfl_example_maker('ARI','KC', 2015, week ))
examples.append(nfl_example_maker('MIN','KC', 2015, week ))
examples.append(nfl_example_maker('WAS','KC', 2015, week ))
examples.append(nfl_example_maker('GB','KC', 2015, week ))
examples.append(nfl_example_maker('SEA','KC', 2015, week ))
examples.append(nfl_example_maker('CAR','PIT', 2015, week ))
examples.append(nfl_example_maker('ARI','PIT', 2015, week ))
examples.append(nfl_example_maker('MIN','PIT', 2015, week ))
examples.append(nfl_example_maker('WAS','PIT', 2015, week ))
examples.append(nfl_example_maker('GB','PIT', 2015, week ))
examples.append(nfl_example_maker('SEA','PIT', 2015, week ))

examples.append(nfl_example_maker("DEN","CAR", 2015, week ))
examples.append(nfl_example_maker("NE","CAR", 2015, week ))
examples.append(nfl_example_maker("CIN","CAR", 2015, week ))
examples.append(nfl_example_maker("HOU","CAR", 2015, week ))
examples.append(nfl_example_maker("KC","CAR", 2015, week ))
examples.append(nfl_example_maker("PIT","CAR", 2015, week ))
examples.append(nfl_example_maker("DEN","ARI", 2015, week ))
examples.append(nfl_example_maker("NE","ARI", 2015, week ))
examples.append(nfl_example_maker("CIN","ARI", 2015, week ))
examples.append(nfl_example_maker("HOU","ARI", 2015, week ))
examples.append(nfl_example_maker("KC","ARI", 2015, week ))
examples.append(nfl_example_maker("PIT","ARI", 2015, week ))
examples.append(nfl_example_maker("DEN","MIN", 2015, week ))
examples.append(nfl_example_maker("NE","MIN", 2015, week ))
examples.append(nfl_example_maker("CIN","MIN", 2015, week ))
examples.append(nfl_example_maker("HOU","MIN", 2015, week ))
examples.append(nfl_example_maker("KC","MIN", 2015, week ))
examples.append(nfl_example_maker("PIT","MIN", 2015, week ))
examples.append(nfl_example_maker("DEN","WAS", 2015, week ))
examples.append(nfl_example_maker("NE","WAS", 2015, week ))
examples.append(nfl_example_maker("CIN","WAS", 2015, week ))
examples.append(nfl_example_maker("HOU","WAS", 2015, week ))
examples.append(nfl_example_maker("KC","WAS", 2015, week ))
examples.append(nfl_example_maker("PIT","WAS", 2015, week ))
examples.append(nfl_example_maker("DEN","GB", 2015, week ))
examples.append(nfl_example_maker("NE","GB", 2015, week ))
examples.append(nfl_example_maker("CIN","GB", 2015, week ))
examples.append(nfl_example_maker("HOU","GB", 2015, week ))
examples.append(nfl_example_maker("KC","GB", 2015, week ))
examples.append(nfl_example_maker("PIT","GB", 2015, week ))
examples.append(nfl_example_maker("DEN","SEA", 2015, week ))
examples.append(nfl_example_maker("NE","SEA", 2015, week ))
examples.append(nfl_example_maker("CIN","SEA", 2015, week ))
examples.append(nfl_example_maker("HOU","SEA", 2015, week ))
examples.append(nfl_example_maker("KC","SEA", 2015, week ))
'''
examples.append(nfl_example_maker("PIT","SEA", 2015, week ))

csv_file = '../resources/2015_playoff_predictionsOOPS.csv'
key_order = examples[0].ordered_example_keys
nfl_example_io().create_header(key_order, csv_file)
'''
for i in range(len(examples)):
    print("working on home team: " + examples[i].example_data_dict['HOMEteam'])
    print("working on away team: " + examples[i].example_data_dict['AWAYteam'])
    nfl_example_io().write(examples[i].example_data_dict, key_order, csv_file, 'a')
'''

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

'''
mins = {}
maxs = {}

for header in data_list[0].keys():
    mins[header] = normalizer.get_column_min(header, data_list)
    maxs[header] = normalizer.get_column_max(header, data_list)
    if 'AWAYscore' == header or 'HOMEscore' == header:
        print(header + str(mins[header]))
        print(header + str(maxs[header]))
'''


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

## TODO: get back to the java side of things to create predictions with simbrain
