from player import Player
from deck import Deck
from const import MESSAGES
from dealer import Dealer
import random
from bots import Bot
from card_collection import CardCollection


class Game:
    max_pl_count = 4

    def __init__(self):
        self.players = []  # список игроков
        self.player = None  # атрибут, где лежит игрок
        self.player_pos = None
        self.dealer = Dealer(position=0)
        self.all_players_count = 1  #
        self.deck = Deck()  # наша колода
        self.max_bet = 20
        self.min_bet = 0

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True

    def _launching(self):
        while True:
            bots_count = int(input('Hello, write bots count '))
            if bots_count <= self.max_pl_count - 1:
                break
        self.all_players_count = bots_count + 1

        for i in range(bots_count):
            # todo: should be random pas
            b = Bot(position=i+1)
            self.players.append(b)
            print(b, ' is created')

        # todo: should be random pas
        self.player = Player(bots_count+1)
        self.player_pos = random.randint(0, self.all_players_count)
        print('Your position is:', self.player_pos)
        self.players.insert(self.player_pos, self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    # метод, отвечающий за первую раздачу карт
    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                # card = self.deck.get_card()
                # player.take_card(card)
                self.deck.move_last_card(player, 2)
                # player.move_last_cards(table, len(player.cards))
                # table.move_last_cards(player)
        card = self.deck.get_card()

# метод проверяющий раздачу на 21 и останавливающий игру
    def check_stop(self, player):
        points = player.fuull_points
        if points >= 21:
            player.print_cards()
            return True
        return False

        # метод удаления игрока
    def remove_player(self, player):
        player.print_cards()
        if isinstance(player, Player):
            print(player, 'are fall!')
        elif isinstance(player, Bot):
            print(player, 'are fall!')

        self.players.remove(player)

    #спрашиваем карты в игре
    def ask_cards(self):
        for player in self.players:  # проходим по игрокам
            while player.ask.card():
                card = self.deck.get_card()
                player.take_card(card)

                if self.check_stop(player):
                   if player.full_points > 21 or isinstance(player, Player):
                       self.remove_player(player)
                
                elif isinstance(player, Player):
                    player.print_cards()
                elif self.check_stop(player):
                    break
            # player.ask_card(self.deck)

    def presente_winners(self, winner_list):
        for winner in winner_list:
            winner.money += winner.bet * 2

    #метод проверки победителя
    def check_winner(self):
        if self.dealer.full_points > 21:
            print('Dealer are fall! All players in game are win!')
            for winner in self.players:
                winner.money += winner.bet * 2
        else:
            for player in self.players:
                if player.full_points == self.dealer.full_points:
                    player.money += player.bet

                    print(MESSAGES.get('eq').format(player=player,
                                                    points=player.full_points))
                # 1 * 1
                elif player.full_points > self.dealer.full_points:
                    player.money += player.bet * 2
                    if isinstance(player, Bot):
                        print(MESSAGES.get('win').format(player))
                    elif isinstance(player, Player):
                        print('You are win')

                else:
                    if isinstance(player, Bot):
                        print(MESSAGES.get('lose').format(player))
                    elif isinstance(player, Player):
                        print('You are lose')

    def play_with_dealer(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    # главный метод с которого начинается игра
    def start(self):
        message = MESSAGES.get('ask_start')  # получаем сообщение о старте

        # и отправляем на старт
        if not self._ask_starting(message=message):
            exit(1)

        # generating data for starting
        self._launching()

        while True:

            # ask about bet
            self.ask_bet()

            # give first cards to the players
            self.first_descr()

            # print player after first
            self.player.print_cards()

            # ask player about card
            self.ask_cards()

            self.play_with_dealer()

            self.check_winner()

            if not self._ask_starting(MESSAGES.get('rerun')):
                break

        # todo: change players position
        # todo: check all players for money


Game.asd = 10

