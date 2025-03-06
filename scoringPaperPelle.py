# This class implements the scoring logic for the paper pelle game
# The score

class Scoring:
    # Initialization of the Scoring class. The difficulty and previous highscores are imported and the score is set to 0
    def __init__(self, difficulty="medium", previous_highscore=0):
        self.player_score = 0
        self.difficulty = difficulty
        self.player_highscore = previous_highscore

    # the score is increased by one (modifiable) each time the player answers correctly
    # This is the standard way to increase the score
    def add_score(self, amount=1):
        self.player_score += amount
        if self.player_score > self.player_highscore:
            self.player_highscore = self.player_score

    # the score can be reset to 0 if required
    def reset_score(self):
        self.player_score = 0

    # the score can be set to a certain amount if required
    def set_score(self, new_score):
        self.player_score = new_score
        if self.player_score > self.player_highscore:
            self.player_highscore = self.player_score

