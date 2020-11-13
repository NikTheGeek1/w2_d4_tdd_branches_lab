import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    # Test we get the right result string for a final score dictionary representing -
    def test_get_result(self):
        home_win = {'home_score': 3, 'away_score': 0}
        self.assertEqual('Home win', get_result(home_win))
        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 

    def test_get_results(self):
        home_win = {'home_score': 3, 'away_score': 0}
        away_win = {'home_score': 0, 'away_score': 3}
        draw = {'home_score': 0, 'away_score': 0}
        self.assertEqual(['Home win', 'Away win', 'Draw'], get_results([home_win, away_win, draw]))


if __name__ == "__main__":
    unittest.main()
