import random


class Card():
    CARD_VALUES = {
            "a": 11, 
            "k": 10,
            "q": 10,
            "j": 10,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }
    def __init__(self, name):
        self.name = name
        self.value = self.CARD_VALUES[name]
        
def random_card():
    names = list(Card.CARD_VALUES.keys())
    name = random.choice(names)
    return Card(name)
        