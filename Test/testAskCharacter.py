import unittest
import random

class CharacterGenerator:
    def __init__(self, character_list):
        self.character_list = character_list

    def ask_character(self, character_amount):
        """
        Return character_amount random characters taken from the character_list.

        Args:
            character_amount (int): Number of characters needed.

        Returns:
            list: A list of characters.
        """
        if character_amount< len(self.character_list):
            return random.sample(self.character_list, character_amount)
        else :
            return self.character_list

class TestAskCharacter(unittest.TestCase):
    def setUp(self):
        self.character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.generator = CharacterGenerator(self.character_list)

    def test_ask_character_length(self):
        result = self.generator.ask_character(3)
        self.assertEqual(len(result), 3)

    def test_ask_character_elements(self):
        result = self.generator.ask_character(5)
        for char in result:
            self.assertIn(char, self.character_list)

    def test_ask_character_no_duplicates(self):
        result = self.generator.ask_character(4)
        self.assertEqual(len(result), len(set(result)))  # Ensures no duplicates

if __name__ == '__main__':
    unittest.main()