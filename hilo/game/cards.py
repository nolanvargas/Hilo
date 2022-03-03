import random

class Cards():
    def __init__(self):
        self.deck = self.new_deck()

    def draw(self):
        if len(self.deck) == 0:
            self.deck = self.new_deck()
        index = random.randint(1, len(self.deck)) - 1
        
        return self.deck.pop(index)

    def new_deck(self):
        cards = []
        for i in range(4):
            for y in range(13):
                cards.append(y+1)
        return cards


