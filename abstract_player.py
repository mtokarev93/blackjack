from card_collection import CardCollection
from const import MESSAGES


# Класс с игроком. Его абстрактный метод
class AbstractPlayer(CardCollection):
    def __init__(self, position, cards=None):
        super().__init__(cards)
        # self.cards = []  # метод конструктор, принимающий карты игрока
        # self.position = position # позиция на игральном столе
        self.bet = 0  # ставка
        self.full_points = 0  # кол-во очков игрока
        self.money = 100
        self.position = position

    # метод пересчитывания кол-ва очков
    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    #! скорее всего лишний метод
    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    # метод где мы берем карты из колоды #! Тоже самое, что и move_last_card?
    def take_cards_from_deck(self, deck, card_count):
        for _ in range(card_count):
            card = deck.get_card()
            self.cards.append(card)
        self.change_points()
        return True

    # метод изменения ставки
    # @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    # печать карт
    def print_cards(self):
        print(self, "'bot data")
        for card in self.cards:
            print(card)
        print(self.full_points)

    # @abc.abstractmethod
    def ask_card(self, deck):
        pass

    # def print_cards(self, deck):


# Класс с игроком