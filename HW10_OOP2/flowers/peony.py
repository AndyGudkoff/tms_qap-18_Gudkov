from .flower import Flower
class Peony(Flower):
    def __init__(self, freshness, cost, stem_lenght, live_lenght = 15, color = "Pink"):
        super().__init__('Peony', live_lenght, cost, color, freshness, stem_lenght)