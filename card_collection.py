from card import Card


class CardCollection:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
            
    # метод передающий карты в другую кучку       
    def move_last_card(self, destination):
        card = self.cards.pop()
        destination.cards.append(card)