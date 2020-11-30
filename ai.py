import random


class AI():
    def __init__(self, game):
        self.game = game

    def choose_action(self):
        available_actions = list(self.game.get_available_actions())
        return random.choice(available_actions)
