import random
from abstract_player import AbstractPlayer


class Bot(AbstractPlayer):

    def __init__(self, position):
        super().__init__(position)
        self.max_points = random.randint(17, 20)

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self, 'give: ', self.bet)

    def ask_card(self, deck):
        if self.full_points < self.max_points:
            return True
        else:
            return False