from abstract_player import AbstractPlayer


class Dealer(AbstractPlayer):

    max_points = 17

    def change_bet(self, max_bet, min_bet):
        """
        NOTE: This type is Dealer so it has no bets
        """
        raise Exception('This type is Dealer so it has no bets')

    def ask_card(self, deck):
        if self.full_points < self.max_points:
            return True
        else:
            return False