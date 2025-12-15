class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
    
    def total(self):
        total = sum(card.value for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.name == "ace")
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1
        return total
    
    def is_bust(self):
        return self.total() > 21
    
    def __iter__(self):
        return iter(self.cards)
