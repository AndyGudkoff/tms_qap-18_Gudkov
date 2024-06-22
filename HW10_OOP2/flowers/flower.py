class Flower:
    def __init__(self, name, live_lenght, cost, color, freshness, stem_lenght):
        self.name : str = name
        self.live_lenght: int = live_lenght
        self.cost: int = cost
        self.color: str = color
        self.freshness: int = freshness
        self.stem_lenght: int = stem_lenght
    def flower_info(self):
        return (f" Flower name - {self.name}, \n cost - {self.cost} $,"
                f" \n Color of the flower - {self.color}, \n The lenght of the stem - {self.stem_lenght} cm,"
                f" \n The freshness of the flower - {self.freshness} days"
                f" \n The flower will live ~ {self.live_lenght} days ")