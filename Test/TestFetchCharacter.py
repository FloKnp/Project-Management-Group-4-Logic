import unittest
import os
import json
import tempfile
from unittest.mock import patch, mock_open
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Position import Position
from Clothe import Clothe
from Character import Character
from CharacterController import CharacterController


class TestCharacterController(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment before each test."""
        self.controller = CharacterController()
        
        # Create a temporary directory for test files
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_json_path = os.path.join(self.test_dir.name, "test.json")
        
        # Sample test data
        self.test_data = [
            {
            "id": 1,
            "clothes": [
                {
                "type": "skjorta",
                "color": "blå",
                "texture": "slät",
                "center_position": {"x": 100, "y": 150},
                "word_position": {"x": 110, "y": 160}
                },
                {
                "type": "byxor",
                "color": "svart",
                "texture": "denim",
                "center_position": {"x": 100, "y": 250},
                "word_position": {"x": 110, "y": 260}
                }
            ],
            "path_to_file": "character1.png",
            "word_position": {"x": 105, "y": 200},
            "center_position": {"x": 100, "y": 200}
            },
            {
            "id": 2,
            "clothes": [
                {
                "type": "hatt",
                "color": "röd",
                "texture": "ull",
                "center_position": {"x": 100, "y": 50},
                "word_position": {"x": 110, "y": 60}
                },
                {
                "type": "skjorta",
                "color": "grön",
                "texture": "bomull",
                "center_position": {"x": 100, "y": 150},
                "word_position": {"x": 110, "y": 160}
                },
                {
                "type": "byxor",
                "color": "brun",
                "texture": "läder",
                "center_position": {"x": 100, "y": 250},
                "word_position": {"x": 110, "y": 260}
                }
            ],
            "path_to_file": "character2.png",
            "word_position": {"x": 105, "y": 200},
            "center_position": {"x": 100, "y": 200}
            },
            {
            "id": 3,
            "clothes": [],
            "path_to_file": "character3.png"
            }
        ]

        
        # Write test data to the test file
        with open(self.test_json_path, 'w') as f:
            json.dump(self.test_data, f)
    
    def tearDown(self):
        """Clean up after each test."""
        self.test_dir.cleanup()
        CharacterController.character_list = []
    
    def test_fetch_characters_from_file_success(self):
        """Test successful character loading from file."""
        # Execute the method
        result = self.controller.fetch_characters_from_file(self.test_json_path)
        
        # Assert the result
        self.assertTrue(result)
        self.assertEqual(len(self.controller.character_list), 3)
        
        # Check first character
        char1 = self.controller.character_list[0]
        self.assertEqual(char1.id, 1)
        self.assertEqual(char1.path_to_file, "character1.png")
        self.assertEqual(len(char1.clothes), 2)
        
        # Check second character
        char2 = self.controller.character_list[1]
        self.assertEqual(char2.id, 2)
        self.assertEqual(char2.path_to_file, "character2.png")
        self.assertEqual(len(char2.clothes), 3)
    
    def test_fetch_characters_from_nonexistent_file(self):
        """Test loading from a file that doesn't exist."""
        result = self.controller.fetch_characters_from_file("nonexistent_file.json")
        self.assertFalse(result)
        self.assertEqual(len(self.controller.character_list), 0)
    
    def test_fetch_characters_from_invalid_json(self):
        """Test loading from a file with invalid JSON."""
        with open(self.test_json_path, 'w') as f:
            f.write("This is not valid JSON")
        
        result = self.controller.fetch_characters_from_file(self.test_json_path)
        self.assertFalse(result)
        self.assertEqual(len(self.controller.character_list), 0)
    
    def test_fetch_characters_with_missing_fields(self):
        """Test loading characters with missing required fields."""
        invalid_data = [
            {"id": 3},  # Missing clothes and path_to_file
            {"clothes": [], "path_to_file": "character4.png"}  # Missing id
        ]
        
        with open(self.test_json_path, 'w') as f:
            json.dump(invalid_data, f)
        
        result = self.controller.fetch_characters_from_file(self.test_json_path)
        self.assertTrue(result)  # The method should still return True even if some characters are skipped
        self.assertEqual(len(self.controller.character_list), 0)  # But no characters should be loaded
    
    def test_fetch_characters_clears_existing_list(self):
        """Test that the method clears existing characters before loading new ones."""
        # First load some characters
        self.controller.fetch_characters_from_file(self.test_json_path)
        self.assertEqual(len(self.controller.character_list), 3)
        
        # Create a new file with different characters
        new_data = [
            {
                "id": 3,
                "clothes": [],
                "path_to_file": "character3.png"
            }
        ]
        
        new_path = os.path.join(self.test_dir.name, "new_test.json")
        with open(new_path, 'w') as f:
            json.dump(new_data, f)
        
        # Load the new characters
        result = self.controller.fetch_characters_from_file(new_path)
        
        # Verify that the old characters were cleared
        self.assertTrue(result)
        self.assertEqual(len(self.controller.character_list), 1)
        self.assertEqual(self.controller.character_list[0].id, 3)


if __name__ == '__main__':
    unittest.main()