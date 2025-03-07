import unittest
import scoringPaperPelle


class TestScoring(unittest.TestCase):
    def test_set_score(self):
        scoring = scoringPaperPelle.Scoring()
        scoring.set_score(10)
        self.assertEqual(scoring.player_score, 10)

    def test_add_score(self):
        scoring = scoringPaperPelle.Scoring()
        scoring.add_score(1)
        self.assertEqual(scoring.player_score, 1)

    def test_reset_score(self):
        scoring = scoringPaperPelle.Scoring()
        scoring.set_score(10)
        scoring.reset_score()
        self.assertEqual(scoring.player_score, 0)


if __name__ == '__main__':
    unittest.main()
