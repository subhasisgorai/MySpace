import unittest
from algo.tournament_can_a_beat_b import MatchResult
from algo.tournament_can_a_beat_b import can_team_a_beat_team_b 


class TournamentTest(unittest.TestCase):

    def test_1(self):
        matches = [MatchResult('A', 'B'), MatchResult('B', 'C'),
                        MatchResult('B', 'D'), MatchResult('D', 'E')]
        self.assertEqual(can_team_a_beat_team_b(matches, 'A', 'E'), True)
        
    def test_cycle(self):
        matches = [MatchResult('A', 'B'), MatchResult('B', 'C'), MatchResult('B', 'D')]
        self.assertEqual(can_team_a_beat_team_b(matches, 'A', 'E'), False)
