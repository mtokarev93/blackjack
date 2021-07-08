from card import Card


class CardPointsManager:
    #метод подсчета очков
    @staticmethod
    def calculate_points(card: Card):
        if card.rank == 'Ace':
            points = 11
        elif card.rank.isdigit():
            points = int(card.rank)
        else:
            points = 10
        return points


# class HundredOneCardPointsManager(CardPointsManager):
#     @staticmethod
#     def calculate_points(card: Card):
#         if card.rank == 'Ace':
#             points = 5
#         elif card.rank.isdigit():
#             points = int(card.rank)
#         elif 'King'...
#             points = 10
#         elif ....
#         return points


# m1 = CardPointsManager()

card = Card(rank='Jack', suit='H')
# print(m1.calculate_points(card))

# m2 = CardPointsManager()
# print(m2.calculate_points(card))

print(CardPointsManager.calculate_points(card))