from const import SUITS, RANKS


class Card:
    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points
        
    # метод показывающий как красиво отрисовать карты
    def __str__(self):
        message = '\nPoints: ' + str(self.points)
        return message