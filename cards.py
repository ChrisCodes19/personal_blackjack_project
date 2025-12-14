import random


class Card():
    CARD_VALUES = {
            "ace": 11, 
            "king": 10,
            "queen": 10,
            "jack": 10,
            "ten": 10,
            "nine": 9,
            "eight": 8,
            "seven": 7,
            "six": 6,
            "five": 5,
            "four": 4,
            "three": 3,
            "two": 2
        }
    def __init__(self, name):
        self.name = name
        self.value = self.CARD_VALUES[name]
        
def random_card():
    names = list(Card.CARD_VALUES.keys())
    name = random.choice(names)
    return Card(name)
        