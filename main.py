from const import MESSAGES
from deck import Deck
from game import Game
from bots import Bot


if __name__ == '__main__':  # хранится имя файла, с которого получен доступ к файлу
    g = Game()
    g.start()
    
    # anothoper = Game()
    # another.start(another)

    print(g.player.money)

    for pl in g.players:
        if isinstance(pl, Bot):
            pl.print_cards()
            print('Max points: ', pl.max_points)
            print('********')

    # for pl in g.players:
    #     pl.print_cards()
    #     if isinstance(pl, Bot):
    #         print('Max points: ', pl.max_points)
    #     print('********')

    # print('DONE')

    # print(g.player_pos)
    # print(g.players)
    # d = Deck()

    # print(len(d))
    # card = d.get_card()
    # print(card)
    # print(len(d))



# MVP - Minimal Valuable Product
# Q = 10
# J = 10
# player1 = [Q, J]
# tuple (кортеж)
#! В отличие от массивов неизменяем (иммутабелен)
# (1, 2, 3...)

# player1 = ['Q', '6']

# Раздача

#TODO: 1. Подготовить колоду
# deck = [ 
#     'A', 'K', 'Q', 'J',
#     # '10', '9','8', 
# ]
# deck += [str(i) for i in range(10, 1, -1)]
# print(deck)

#TODO: 2. Тасовка
# Написать тасовку.
# Перенести все в ООП модель.

#TODO: 3. Раздать карты всем игрокам последовательно
# def dealing_to_player(source, count, position):
    #TODO: 3.1 Взять count последних карт
    # last_cards = source[-count:]
    
    #TODO: 3.2 Добавить их в конец списка игрока
    # position += last_cards
    
    #TODO: 3.3 Удалить из source эти карты
    # del source[-count:]
    

# players = [player1, player2, player3]

# dealing_to_player(deck, 2, player1)
# dealing_to_player(deck, 2, player2)
# dealing_to_player(deck, 2, player3)

# print('Deck: ', deck)

# print('Player1: ', player1)
# print('Player2: ', player2)
# print('Player3: ', player3)