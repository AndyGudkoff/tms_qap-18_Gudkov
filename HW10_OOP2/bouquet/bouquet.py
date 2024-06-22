class Bouquet:
    def __init__(self, flowers=None, accessories=None):
        self.flowers = []
        self.accessories = []

    def add_flower(self,flower):
        self.flowers.append(flower)
    def remove_flower(self,flower):
        self.flowers.remove(flower)

    def add_accessory(self,accessory):
        self.accessories.append(flower)
    def remove_accessory(self, accessory):
        self.accessories.remove(flower)

    def bouquet_cost(self):
        bouquet_cost = sum (flower.cost for flower in self.flowers) + (accessory.cost for accessory in self.accessories)
        return bouquet_cost

    def fading_time(self, flowers):
        total_live_lenght = (sum (flower.live_lenght for flower in self.flowers) )
        avg_lifetime = total_live_lenght / len (self.flowers)
        return avg_lifetime

    def sort_flowers(self, key):
        sorted_flowers = sorted(self.flowers, key=lambda flower: getattr(flower, key))
        return [flower.name for flower in sorted_flowers]

    def contain_flower(self, flower_to_find):
        flower = False
        return any(flower_to_find == flower_to_find for flower in self.flowers)

    def search_flowers(self, name=None, color=None, max_cost=None, min_freshness=None, min_stem_length=None):
        results = self.flowers
        if name:
            results = [flower for flower in results if flower.name == name]
        if color:
            results = [flower for flower in results if flower.color == color]
        if max_cost is not None:
            results = [flower for flower in results if flower.cost <= max_cost]
        if min_freshness is not None:
            results = [flower for flower in results if flower.freshness >= min_freshness]
        if min_stem_length is not None:
            results = [flower for flower in results if flower.stem_length >= min_stem_length]
        return results