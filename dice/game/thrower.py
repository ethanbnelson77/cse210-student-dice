import random

# TODO: Define the Thrower class here.
""" 
    A Thrower is the player in the game.
    Their role is to role the dice and to choose
    whether or not to continue playing after a successful turn

    Attributes:
        dice (list of numbers): keeps track of the numbers rolled during a turn
        num_throws (number): the number of turns taken
"""


class Thrower:
    

    def __init__(self):
        self.dice = []
        self.num_throws = 0

    
    def can_throw(self):
        if self.dice.count(5) > 0 or self.dice.count(1) > 0:
            return True
        else:
            return False


    def get_points(self):
        return self.dice.count(5) * 50 + self.dice.count(1) * 100


    def throw_dice(self):
        self.dice.clear()
        for x in range(5):
            x = random.randint(1,6)
            self.dice.append(x)
        self.num_throws += 1