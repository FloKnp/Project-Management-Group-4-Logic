import random
class Character:
    def __init__(self, character_id, name_of_file, clothes):
        self.id = character_id
        self.path_to_file = name_of_file
        self.clothes = clothes

class CharacterController:
    character_list = []
    id = 0  # Static variable for unique character ID

    def create_character(self, name_of_file, clothes):
        """
        Creates a new character and adds it to the character list.

        Args:
            name_of_file (str): The name of the file to get characters image from.
            clothes (list): A list of the clothes associated with the character.

        Returns:
            Character: The created character object.
        """
        CharacterController.id += 1  # Increment the ID counter
        new_character = Character(CharacterController.id, name_of_file, clothes)
        CharacterController.character_list.append(new_character)
        return new_character

    def remove_character(self, character_id):
        """
        Removes a character from the list based on their ID.

        Args:
            character_id (int): The ID of the character to remove.

        Returns:
            bool: True if the character was removed, False if not found.
        """
        for character in CharacterController.character_list:
            if character.id == character_id:
                CharacterController.character_list.remove(character)
                return True
        return False

    def ask_character(self, character_amount):
        """
        Return character_amount random characters taken from the character_list.
    
        Args:
            character_amount (int): Number of characters needed.
    
        Returns:
            list: A list of characters.
        """
        random_characters = random.sample(CharacterController.character_list, character_amount)
        return random_characters
