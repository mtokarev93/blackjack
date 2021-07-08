from card_collection import CardCollection
import random
from const import MESSAGES
from abstract_player import AbstractPlayer


# Класс с игроком

class Player(AbstractPlayer):

    def __init__(self, position, cards=None):
        super().__init__(position)
        self.max_points = random

    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Make your bet: '))
            if value < max_bet and value > min_bet:
                self.bet = value
                break
            print('Your bet is: ', self.bet)

    # игрок автоматически говорит "Нет", если выпало 21
    def ask_card(self, deck):
        if self.full_points == 21:
            return False

        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            return True
        else:
            return False

        # todo : is it needed?




        

        


        
        