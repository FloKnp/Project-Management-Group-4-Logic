import unittest
import random
import DataModel

class TestDataModel(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of DataModel before each test."""
        self.model = DataModel.DataModel()

    def test_get_nouns(self):
        """Test if get_nouns returns the correct amount of nouns."""
        nouns = self.model.get_nouns(3)
        self.assertEqual(len(nouns), 3)
        for noun in nouns:
            self.assertIn(noun, self.model.noun_list)

    def test_get_adjectives(self):
        """Test if get_adjectives returns the correct amount of adjectives."""
        adjectives = self.model.get_adjectives(2)
        self.assertEqual(len(adjectives), 2)
        for adj in adjectives:
            self.assertIn(adj, self.model.adjective_list)

    def test_get_tasks(self):
        """Test if get_tasks returns correct noun-adjective pairs."""
        tasks = self.model.get_tasks(2)
        self.assertEqual(len(tasks), 2)
        for noun, adjective in tasks:
            self.assertIn(noun, self.model.noun_list)
            self.assertIn(adjective, self.model.adjective_list)

    def test_get_nouns_except(self):
        """Test if get_nouns_except excludes specified nouns."""
        excluded = ["t-shirt", "blus"]
        nouns = self.model.get_nouns_except(excluded, 2)
        self.assertEqual(len(nouns), 2)
        for noun in nouns:
            self.assertNotIn(noun, excluded)

    def test_get_adjectives_except(self):
        """Test if get_adjectives_except excludes specified adjectives."""
        excluded = ["gul", "röd"]
        adjectives = self.model.get_adjectives_except(excluded, 2)
        self.assertEqual(len(adjectives), 2)
        for adj in adjectives:
            self.assertNotIn(adj, excluded)

    def test_add_noun(self):
        """Test adding a single noun and a list of nouns."""
        self.assertTrue(self.model.add_noun("hatt"))
        self.assertIn("hatt", self.model.noun_list)

        self.assertTrue(self.model.add_noun(["mössa", "keps"]))
        self.assertIn("mössa", self.model.noun_list)
        self.assertIn("keps", self.model.noun_list)

    def test_add_adjective(self):
        """Test adding a single adjective and a list of adjectives."""
        self.assertTrue(self.model.add_adjective("blå"))
        self.assertIn("blå", self.model.adjective_list)

        self.assertTrue(self.model.add_adjective(["grön", "lila"]))
        self.assertIn("grön", self.model.adjective_list)
        self.assertIn("lila", self.model.adjective_list)

if __name__ == '__main__':
    unittest.main()
