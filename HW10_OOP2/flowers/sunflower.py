from .flower import Flower

class Sunflower(Flower):
    def __init__(self, freshness, cost, stem_lenght, live_lenght = 20, color = "Yellow"):
        super().__init__('Sunflowers', live_lenght, cost, color, freshness, stem_lenght)