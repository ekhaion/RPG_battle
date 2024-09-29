import random


class Characteristic:
    def __init__(self):
        # randomize Characteristics for both hero and monster
        self.health = random.randint(50, 200)
        self.strength = random.randint(10, 30)
        self.defense = random.randint(5, 15)