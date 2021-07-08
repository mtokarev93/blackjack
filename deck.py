from const import SUITS, RANKS
from itertools import product
from card import Card
from card_collection import CardCollection
from random import shuffle


class Deck(CardCollection):
    def __init__(self, cards=None):
        super().__init__(cards)
        if cards is None:
            self.cards = self._generate_cards()
        shuffle(self.cards) # тасование колоды

# метод генерации колоды
    @staticmethod
    def _generate_cards():
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'Ace':
                points == 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            c = Card(suit=suit, rank=rank, points=points) #создание артибута карты
            cards.append(c) # добавление её в массив всех карт
        return cards
    
# метод который достаёт карту из колоды
    def get_card(self):
        return self.cards.pop()
    
# метод возвращающий длину массива
    def __len__(self):
        return len(self.cards)


