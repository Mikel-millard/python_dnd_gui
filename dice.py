# Imports
import random


# Creates a dice object for rolling
class Dice:
    # Defines what a dice should look like
    def __init__(self, sides):
        self.sides = sides

    # Allows the rolling of a die
    def roll(self):
        return random.randint(1, self.sides)