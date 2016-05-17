from nfl_data.nfl_stat_handler import *

__author__ = 'jamo'


class nfl_team_example_stats(object):
    def __init__(self):
        self.games_used = 0
        self.stat_dict = {}
        self.Date = 0.0
        self.Season = 0.0
        self.Week = 0.0
        self.Team = 0.0
        self.Opponent = 0.0
        self.HomeOrAway = 0.0
        self.Score = 0.0
        self.OpponentScore = 0.0
        self.TotalScore = 0.0
        self.Stadium = 0.0
        self.PlayingSurface = 0.0
        self.Temperature = 0.0
        self.Humidity = 0.0
        self.WindSpeed = 0.0
        self.OverUnder = 0.0
        self.PointSpread = 0.0
        self.ScoreQuarter1 = 0.0
        self.ScoreQuarter2 = 0.0
        self.ScoreQuarter3 = 0.0
        self.ScoreQuarter4 = 0.0
        self.ScoreOvertime = 0.0
        self.TimeOfPossessionMinutes = 0.0
        self.TimeOfPossessionSeconds = 0.0
        self.TimeOfPossession = 0.0
        self.FirstDowns = 0.0
        self.FirstDownsByRushing = 0.0
        self.FirstDownsByPassing = 0.0
        self.FirstDownsByPenalty = 0.0
        self.OffensivePlays = 0.0
        self.OffensiveYards = 0.0
        # debug stats if needed
        self.OffensiveYardsPerPlay = 0.0
        self.Touchdowns = 0.0
        self.RushingAttempts = 0.0
        # end of debug stats
        self.RushingYards = 0.0
        self.RushingYardsPerAttempt = 0.0
        self.RushingTouchdowns = 0.0
        self.PassingAttempts = 0.0
        self.PassingCompletions = 0.0
        self.PassingYards = 0.0
        self.PassingTouchdowns = 0.0
        self.PassingInterceptions = 0.0
        self.PassingYardsPerAttempt = 0.0
        self.PassingYardsPerCompletion = 0.0
        self.CompletionPercentage = 0.0
        self.PasserRating = 0.0
        self.ThirdDownAttempts = 0.0
        self.ThirdDownConversions = 0.0
        self.ThirdDownPercentage = 0.0
        self.FourthDownAttempts = 0.0
        self.FourthDownConversions = 0.0
        self.FourthDownPercentage = 0.0
        self.RedZoneAttempts = 0.0
        self.RedZoneConversions = 0.0
        self.GoalToGoAttempts = 0.0
        self.GoalToGoConversions = 0.0
        self.ReturnYards = 0.0
        self.Penalties = 0.0
        self.PenaltyYards = 0.0
        self.Fumbles = 0.0
        self.FumblesLost = 0.0
        self.TimesSacked = 0.0
        self.TimesSackedYards = 0.0
        self.QuarterbackHits = 0.0
        self.TacklesForLoss = 0.0
        self.Safeties = 0.0
        self.Punts = 0.0
        self.PuntYards = 0.0
        self.PuntAverage = 0.0
        self.Giveaways = 0.0
        self.Takeaways = 0.0
        self.TurnoverDifferential = 0.0
        self.OpponentScoreQuarter1 = 0.0
        self.OpponentScoreQuarter2 = 0.0
        self.OpponentScoreQuarter3 = 0.0
        self.OpponentScoreQuarter4 = 0.0
        self.OpponentScoreOvertime = 0.0
        self.OpponentTimeOfPossessionMinutes = 0.0
        self.OpponentTimeOfPossessionSeconds = 0.0
        self.OpponentTimeOfPossession = 0.0
        self.OpponentFirstDowns = 0.0
        self.OpponentFirstDownsByRushing = 0.0
        self.OpponentFirstDownsByPassing = 0.0
        self.OpponentFirstDownsByPenalty = 0.0
        self.OpponentOffensivePlays = 0.0
        self.OpponentOffensiveYards = 0.0
        self.OpponentOffensiveYardsPerPlay = 0.0
        self.OpponentTouchdowns = 0.0
        self.OpponentRushingAttempts = 0.0
        self.OpponentRushingYards = 0.0
        self.OpponentRushingYardsPerAttempt = 0.0
        self.OpponentRushingTouchdowns = 0.0
        self.OpponentPassingAttempts = 0.0
        self.OpponentPassingCompletions = 0.0
        self.OpponentPassingYards = 0.0
        self.OpponentPassingTouchdowns = 0.0
        self.OpponentPassingInterceptions = 0.0
        self.OpponentPassingYardsPerAttempt = 0.0
        self.OpponentPassingYardsPerCompletion = 0.0
        self.OpponentCompletionPercentage = 0.0
        self.OpponentPasserRating = 0.0
        self.OpponentThirdDownAttempts = 0.0
        self.OpponentThirdDownConversions = 0.0
        self.OpponentThirdDownPercentage = 0.0
        self.OpponentFourthDownAttempts = 0.0
        self.OpponentFourthDownConversions = 0.0
        self.OpponentFourthDownPercentage = 0.0
        self.OpponentRedZoneAttempts = 0.0
        self.OpponentRedZoneConversions = 0.0
        self.OpponentGoalToGoAttempts = 0.0
        self.OpponentGoalToGoConversions = 0.0
        self.OpponentReturnYards = 0.0
        self.OpponentPenalties = 0.0
        self.OpponentPenaltyYards = 0.0
        self.OpponentFumbles = 0.0
        self.OpponentFumblesLost = 0.0
        self.OpponentTimesSacked = 0.0
        self.OpponentTimesSackedYards = 0.0
        self.OpponentQuarterbackHits = 0.0
        self.OpponentTacklesForLoss = 0.0
        self.OpponentSafeties = 0.0
        self.OpponentPunts = 0.0
        self.OpponentPuntYards = 0.0
        self.OpponentPuntAverage = 0.0
        self.OpponentGiveaways = 0.0
        self.OpponentTakeaways = 0.0
        self.OpponentTurnoverDifferential = 0.0
        self.stats_to_average = ['ScoreQuarter1', 'ScoreQuarter2',
                                 'ScoreQuarter3', 'ScoreQuarter4', 'ScoreOvertime',
                                 'TimeOfPossessionMinutes', 'TimeOfPossessionSeconds',
                                 'TimeOfPossession', 'FirstDowns', 'FirstDownsByRushing',
                                 'FirstDownsByPassing', 'FirstDownsByPenalty', 'OffensivePlays',
                                 'OffensiveYards', 'OffensiveYardsPerPlay', 'Touchdowns',
                                 'RushingAttempts', 'RushingYards', 'RushingYardsPerAttempt',
                                 'RushingTouchdowns', 'PassingAttempts', 'PassingCompletions',
                                 'PassingYards', 'PassingTouchdowns', 'PassingInterceptions',
                                 'PassingYardsPerAttempt', 'PassingYardsPerCompletion',
                                 'CompletionPercentage', 'PasserRating', 'ThirdDownAttempts',
                                 'ThirdDownConversions', 'ThirdDownPercentage', 'FourthDownAttempts',
                                 'FourthDownConversions', 'FourthDownPercentage', 'RedZoneAttempts',
                                 'RedZoneConversions', 'GoalToGoAttempts', 'GoalToGoConversions',
                                 'ReturnYards', 'Penalties', 'PenaltyYards', 'Fumbles', 'FumblesLost',
                                 'TimesSacked', 'TimesSackedYards', 'QuarterbackHits',
                                 'TacklesForLoss', 'Safeties', 'Punts', 'PuntYards', 'PuntAverage',
                                 'Giveaways', 'Takeaways', 'TurnoverDifferential',
                                 'OpponentScoreQuarter1', 'OpponentScoreQuarter2',
                                 'OpponentScoreQuarter3', 'OpponentScoreQuarter4',
                                 'OpponentScoreOvertime', 'OpponentTimeOfPossessionMinutes',
                                 'OpponentTimeOfPossessionSeconds', 'OpponentTimeOfPossession',
                                 'OpponentFirstDowns', 'OpponentFirstDownsByRushing',
                                 'OpponentFirstDownsByPassing', 'OpponentFirstDownsByPenalty',
                                 'OpponentOffensivePlays', 'OpponentOffensiveYards',
                                 'OpponentOffensiveYardsPerPlay', 'OpponentTouchdowns',
                                 'OpponentRushingAttempts', 'OpponentRushingYards',
                                 'OpponentRushingYardsPerAttempt', 'OpponentRushingTouchdowns',
                                 'OpponentPassingAttempts', 'OpponentPassingCompletions',
                                 'OpponentPassingYards', 'OpponentPassingTouchdowns',
                                 'OpponentPassingInterceptions', 'OpponentPassingYardsPerAttempt',
                                 'OpponentPassingYardsPerCompletion',
                                 'OpponentCompletionPercentage', 'OpponentPasserRating',
                                 'OpponentThirdDownAttempts', 'OpponentThirdDownConversions',
                                 'OpponentThirdDownPercentage', 'OpponentFourthDownAttempts',
                                 'OpponentFourthDownConversions', 'OpponentFourthDownPercentage',
                                 'OpponentRedZoneAttempts', 'OpponentRedZoneConversions',
                                 'OpponentGoalToGoAttempts', 'OpponentGoalToGoConversions',
                                 'OpponentReturnYards', 'OpponentPenalties', 'OpponentPenaltyYards',
                                 'OpponentFumbles', 'OpponentFumblesLost', 'OpponentTimesSacked',
                                 'OpponentTimesSackedYards', 'OpponentQuarterbackHits',
                                 'OpponentTacklesForLoss', 'OpponentSafeties', 'OpponentPunts',
                                 'OpponentPuntYards', 'OpponentPuntAverage', 'OpponentGiveaways',
                                 'OpponentTakeaways', 'OpponentTurnoverDifferential']
        # debug stats list
        # self.stats_to_average = ['OffensiveYardsPerPlay','Touchdowns',
        #                         'RushingAttempts']

    def include_stats_in_average(self, team, game_stats):
        """
        will update this current objects average stat values with the new
        stats given in the game_stats dict.  If the team in question is
        listed as the Opponent in the game_stats, then it will need to
        apply those stats listed as Opponent stats to this objects stats
        that are not Opponent stats...  I hope this makes sense the next
        time you read it, said to self.
        """
        if team == game_stats['Team']:
            self.average_stats_as_team(game_stats)
        elif team == game_stats['Opponent']:
            self.average_stats_as_opponent(game_stats)
        else:
            raise ValueError('team not found in Team or Opponent indexes')

    def average_stats_as_team(self, game_stats):
        """
        Will simple loop through each stat and call the real work.  no tricks.
        :param game_stats:
        :return: None
        """
        for stat in self.stats_to_average:
            stat_string = 'self.' + stat
            self.expand_stat_from_average_and_recalculate(stat_string,
                                                          stat_string,
                                                          game_stats)

    def average_stats_as_opponent(self, game_stats):
        """
        In this case, we want to use the stats with 'Opponent' for this
        team, and without 'Opponent' for the *other* team
        """
        for stat in self.stats_to_average:
            stat_to_apply_to = stat

            if 'Opponent' in stat:
                stat_to_get_value_from = 'self.' + stat.replace('Opponent', '')
            else:
                stat_to_get_value_from = 'self.Opponent' + stat

            self.expand_stat_from_average_and_recalculate(stat_to_apply_to,
                                                          stat_to_get_value_from,
                                                          game_stats)

    def expand_stat_from_average_and_recalculate(self, stat_to_apply_to,
                                                 stat_to_get_value_from,
                                                 game_stats):
        """

        :param stat_to_apply_to: the name of the attribute which the stat
            update will be done
        :param stat_to_get_value_from: the name of the stat where we will get
            the actual value to apply to 'stat_to_apply_to'
        :param game_stats: dict containing all game stats
        :return: None
        """
        # remove the selfie
        stat_apply_string_no_self = stat_to_apply_to.replace("self.", "")
        stat_get_string_no_self = stat_to_get_value_from.replace("self.", "")
        value = game_stats[stat_get_string_no_self]
        stat_handler = nfl_stat_handler(stat_apply_string_no_self, value)

        # need to extract current total from pre-existing average so we can
        # add new value and take new average
        current_total = getattr(self, stat_apply_string_no_self) * (self.games_used - 1)

        # for older games, not all stats are there, so they will show up as
        # None.  For the sake of math, we'll change it to a zero.
        if stat_handler.stat_info['value'] is None or stat_handler.stat_info['value'] == '':
            stat_handler.stat_info['value'] = 0
        new_total = current_total + float(stat_handler.stat_info['value'])

        # bring it back to the new average
        setattr(self, stat_apply_string_no_self, new_total / self.games_used)
        self.update_stats_dict()

    def increment_game_count(self, count=1):
        self.games_used += count

    def update_stats_dict(self):
        for stat in self.stats_to_average:
            # since the stats end up being persisted via csv files, making
            # all the values of type string now will help down the road when
            # reading/writing with csv libs
            self.stat_dict[stat] = str(getattr(self, stat))
