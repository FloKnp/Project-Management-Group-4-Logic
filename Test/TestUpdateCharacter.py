import unittest

from CharacterController import CharacterController


class TestAskCharacter(unittest.TestCase):

    def test_update_character(self):
        characterController = CharacterController()
        character = characterController.create_character("A", ['shirt', 'blue', 'tissue', (10, 10), (20, 20)])
        characterController.update_character(character.id, 'path_to_file', 'B')
        character = characterController.get_character(character.id)
        self.assertEqual(character.path_to_file, 'B')
        characterController.update_character(character.id, 'clothes', ['pant','red','jeans'],0)
        character = characterController.get_character(character.id)
        self.assertEqual(character.clothes[0], ['pant','red','jeans'])


if __name__ == '__main__':
    unittest.main()
