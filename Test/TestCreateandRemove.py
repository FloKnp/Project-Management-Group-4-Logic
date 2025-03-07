import unittest
from CharacterController import CharacterController  # Replace with the actual module name


class TestCharacterController(unittest.TestCase):
    def setUp(self):
        """Set up a fresh CharacterController before each test."""
        self.controller = CharacterController()
        self.controller.character_list = []  # Reset character list
        self.controller.id = 0  # Reset ID counter

    def test_create_character(self):
        """Test if a character is created correctly."""
        character = self.controller.create_character("character1.png", ["hat", "shirt"])
        self.assertEqual(character.id, 1)
        self.assertEqual(character.path_to_file, "character1.png")
        self.assertEqual(character.clothes, ["hat", "shirt"])
        self.assertIn(character, self.controller.character_list)

    def test_remove_character_success(self):
        """Test removing a character that exists."""
        character = self.controller.create_character("character2.png", ["jacket"])
        result = self.controller.remove_character(character.id)
        self.assertTrue(result)
        self.assertNotIn(character, self.controller.character_list)

    def test_remove_character_failure(self):
        """Test removing a character that does not exist."""
        result = self.controller.remove_character(99)  # Non-existent ID
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

