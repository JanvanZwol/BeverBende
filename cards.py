class Card():
    pass

class Point_card(Card):
    def __init__(self, points):
        self.points = points

    def __str__(self):
        return str(self.points)

class Power_card(Card):
    def __init__(self, power):
        self.power = power