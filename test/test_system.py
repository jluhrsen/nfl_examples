from nfl_data.nfl_in_season_examples import *
import unittest

__author__ = 'jamo'


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.csv_output_file = '/tmp/examples.csv'
        self.week = 17
        self.season = 2016
        self.examples = []
        self.schedule = nfl_local_data_handler().get_schedule(self.season)

    def tearDown(self):
        pass

    # TODO: fix this asap
    @unittest.skip("FIX THIS. test seems to be using too many games. it might be"
                   "iterating over the playoff matchups where I match every team"
                   "against every team. IMPORTANT TO FIX!")
    def test_real_averages_in_examples(self):

        # idea of this test is to really check well the actual average values of an example and make sure
        # the HOME/AWAY and Opponent stats are in the right places and with the right values.  This is to
        # help ease the constant worry that something is getting switched so that Home gets switched with
        # away, or opponent is actually the team instead, etc.

        example_creator = nfl_in_season_examples(2016, 17)
        example_creator.create()

        with open(example_creator.season_examples_file, "r") as example_file:
            reader = csv.DictReader(example_file)
            for line in reader:
                if line['HOMEteam'] == "DEN":
                    stats = [
                        {'name': 'AWAYOffensiveYards', 'value': '383.2'},
                        {'name': 'AWAYOpponentOffensiveYards', 'value': '376.8666666666667'},
                        {'name': 'AWAYPassingCompletions', 'value': '23.866666666666667'},
                        {'name': 'AWAYOpponentPassingCompletions', 'value': '20.733333333333334'},
                        {'name': 'AWAYPassingAttempts', 'value': '37.53333333333333'},
                        {'name': 'AWAYOpponentPassingAttempts', 'value': '34.266666666666666'},
                        {'name': 'AWAYPenalties', 'value': '8.933333333333334'},
                        {'name': 'AWAYOpponentPenalties', 'value': '7.33333'},
                        {'name': 'AWAYPenaltyYards', 'value': '74.8'},
                        {'name': 'AWAYOpponentPenaltyYards', 'value': '67.2'}, # 67.933 from profootballreference research
                        {'name': 'AWAYFirstDownsByPenalty', 'value': '2.333'},
                        {'name': 'AWAYFirstDownsByRushing', 'value': '6.4'},
                        {'name': 'AWAYOpponentFirstDownsByPenalty', 'value': '2.067'},
                        {'name': 'AWAYOpponentFirstDownsByRushing', 'value': '5.933'},
                        {'name': 'HOMEOffensiveYards', 'value': '321.333333333333'},
                        {'name': 'HOMEOpponentOffensiveYards', 'value': '322.4'},
                        {'name': 'HOMEPassingCompletions', 'value': '21.4666666666667'},
                        {'name': 'HOMEOpponentPassingCompletions', 'value': '19.0666666666667'},
                        {'name': 'HOMEPassingAttempts', 'value': '36.2'},
                        {'name': 'HOMEOpponentPassingAttempts', 'value': '34.6666666666667'},
                        {'name': 'HOMEPenalties', 'value': '7.6'}, # 7.5 from profootballreference research
                        {'name': 'HOMEOpponentPenalties', 'value': '6.467'},
                        {'name': 'HOMEPenaltyYards', 'value': '62.8'},
                        {'name': 'HOMEOpponentPenaltyYards', 'value': '57.667'},
                    ]
                    for stat in stats:
                        self.assertAlmostEqual(float(line[stat['name']]), float(stat['value']), places=3,
                                               msg=stat['name'] + ' not correct')
                    continue

    @unittest.skip("skipping because THIS TAKES FOREVER!")
    def test_examples_for_one_week_in_one_season(self):

        # loop through each game a of particular week and
        # create example for each game and write to csv

        # TODO: this test case seems to do a lot of work, but I don't see any real validations being checked

        for game in self.schedule:
            if game['Week'] == str(self.week):
                home_team = game['HomeTeam']
                away_team = game['AwayTeam']
                if home_team != 'BYE' and away_team != 'BYE':
                    example = \
                       nfl_example_maker(home_team, away_team, self.season, self.week)
                    self.examples.append(example)

        key_order = self.examples[0].ordered_example_keys

        writer = nfl_example_io()
        writer.create_header(key_order, self.csv_output_file)

        for i in range(len(self.examples)):
            writer.write(self.examples[i].example_data_dict, key_order,
                         self.csv_output_file, 'a')
