import unittest
import random

from CharacterController import CharacterController


class TestAskCharacter(unittest.TestCase):
    def setUp(self):
        self.character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.generator = CharacterController(self.character_list)

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
