# Paper-Pelle-Logic-Group-4

As one of three Swedish learning games within the program, Paper Pelle enables students to practice clothing and color vocabulary through an interactive experience. Each round presents users with a new set of clothes alongside Swedish words to match. Their selections are recorded and reflected on a scoreboard, reinforcing learning through immediate feedback.

All the unit tests are included in the Test file.

## Features of se01_data_model.py

For the data model, you need to ensure the file se01_data_model.py is accessible
Then you can run TestDataModel.py
It will run 2 routines to test that the datamodel can provide a list of nouns or a list of adjectives to the GUI

-Defines lists of words in different categories (nouns, adjectives, etc.).

-Creates tasks based on these words.

-Combines tasks into exercises and exercises into lessons.

-Provides functions for randomly selecting nouns and adjectives that are not already used.

-Includes a function to verify the correctness of tasks, exercises, and lessons.

## Clothe.py

Represents a piece of clothing with various attributes, including type, color, texture,
and positioning information.

## Position.py

Represents a 2D point with x and y coordinates.

## CharacterController.py

Manages characters, including creation, retrieval, updating, and deletion.

-create_character(name_of_file, clothes): Creates and adds a new character to the list.

-verify_user_input(character_id, user_input): Verifies if the user's input is correct (not implemented).

-ask_character(character_amount): Returns a list of random characters from the character list.

-fetch_characters_from_file(file_path): Loads characters from a JSON file into the character list.

-remove_character(character_id): Removes a character from the list by ID.

-update_character(character_id, attribute_to_change, new_value, clothe_position=0): Updates a character’s attribute (e.g., clothes, position).

-retrieve_nouns(character_id_list): Retrieves 15 nouns, excluding those in the given character ID list (not implemented).

-retrieve_adjectives(character_id_list): Retrieves 20 adjectives, excluding those in the given character ID list (not implemented).

## Character.py

Represents a character with an ID, associated clothes, and a file path.

## scoringPaperPelle.py

Handles the scoring logic for the paper pelle game, including managing the player's score and highscore based on difficulty.

__init__(difficulty="medium", previous_highscore=0):
Initializes the Scoring object with default values for difficulty, player score (set to 0), and player highscore (set to the provided previous highscore).

-add_score(amount=1):
Increases the player's score by the specified amount (default is 1). Updates the highscore if the current score exceeds the previous highscore.

-reset_score():
Resets the player's score to 0.

-set_score(new_score):
Sets the player's score to a specified value (new_score). Updates the highscore if the new score exceeds the previous highscore.
