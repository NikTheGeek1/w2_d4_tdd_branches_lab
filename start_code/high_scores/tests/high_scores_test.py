import unittest

from src.high_scores import latest, personal_best, personal_top_three, ordered

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [1, 2, 10, 30, 5]
    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(5, latest(self.scores))
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(30, personal_best(self.scores))
    # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual([30, 10, 5], personal_top_three(self.scores))
    # Test ordered from highest tp lowest
    def test_ordered(self):
        self.assertEqual([1, 2, 5, 10, 30], ordered(self.scores))
    # Test top three when there is a tie
    def test_top_three_tie(self):
        self.assertEqual([20, 20, 10], personal_top_three([10, 20, 20]))
    # Test top three when there are less than three
    def test_top_three_less_than_three(self):
        self.assertEqual([2, 1], personal_top_three([1, 2]))
    # Test top three when there is only one
    def test_top_three_when_just_one(self):
        self.assertEqual([1], personal_top_three([1]))
    
