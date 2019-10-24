from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])

class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'hearts spades clubs diamonds'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks 
                                        for suit in self.suits]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


cd = CardDeck()

print(len(cd)) # pythonic - users don't need to remember how to get the size of the deck
print(choice(cd)) # take advantage of standard library to pick a random element
print(cd[-1]) # indexing is automatically supported because the class implements __getitem__
top3 = cd[:3] # slicing is automatically supported because the class implements __getitem__

for card in cd: # "in" operator is also supported because __getitem__ was implemented
    print(card)

print(Card('A', 'spades') in cd) # membership testing also works

print('hi')