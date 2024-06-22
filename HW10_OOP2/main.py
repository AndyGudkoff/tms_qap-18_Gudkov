from flowers.peony import Peony
from flowers.sunflower import Sunflower
from bouquet.bouquet import Bouquet


# Цветочница.
# Определить иерархию и создать несколько цветов. Собрать букет которых могут быть/не быть
# использовать аксессуары с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (пример параметров: свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам.
# Узнать, есть ли цветок в букете.
#
# Создать консольное приложение, удовлетворяющее следующим требованиям:
#
# 1. Использовать возможности ООП: классы, наследование, полиморфизм, инкапсуляция.
# 2. Каждый класс должен иметь исчерпывающее смысл название и информативный состав.
# 3. Наследование должно применяться только тогда, когда это имеет смысл.
# 4. При кодировании должны быть использованы соглашения об оформлении кода.
# 5. Классы должны быть грамотно разложены по пакетам


bouquet = Bouquet()
peony = Peony(10, 5, 30)
sunflower = Sunflower(7, 3, 50)

bouquet.add_flower(peony)
bouquet.add_flower(sunflower)

print(bouquet.contain_flower("Peony"))  # Output: True

# Searching for flowers
search_results = bouquet.search_flowers(color="Pink", max_cost=6)
for flower in search_results:
    print(flower.flower_info())


bouquet = Bouquet()
peony = Peony(10, 5, 30)
sunflower = Sunflower(7, 3, 50)

bouquet.add_flower(peony)
bouquet.add_flower(sunflower)

print(bouquet.contain_flower("Peony"))


search_results = bouquet.search_flowers(color="Pink", max_cost=6)
for flower in search_results:
    print(flower.flower_info())

sort_by_cost = bouquet.sort_flowers('cost')
print(f"Flowers were sorted by cost : {sort_by_cost}")
