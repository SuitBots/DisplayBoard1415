"""
Functions for calculating round-by-round OPR based on match data
"""

class Match(object):
    def __init__(self, red1, red2, blue1, blue2, red_score, blue_score):
        self.red1, self.red2 = red1, red2
        self.red_score = red_score
        self.blue1, self.blue2 = blue1, blue2
        self.blue_score = blue_score

class TeamStats(object):
    def __init__(self, number, name, qp, rp, opr):
        self.number = number
        self.name = name
        self.qp = qp
        self.rp = rp
        self.opr = opr

def generate_opr(team_names, matches):
    """
    Given a list of matches, produce round-by-round OPR
    input:
      team_names: team number -> team name (i.e., { 4628 : 'Suit Bots' })
      matches: a list of Match objects, in order
    output:
      a list of lists of TeamStats objects. For each match round,
      there should be a TeamStats object for each team. It should
      have their current QP, RP and OPR. If the team hasn't played
      in any matches yet, QP, RP and OPR should be zero.
    """
    pass

