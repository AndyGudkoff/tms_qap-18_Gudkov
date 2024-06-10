# 1 Напишите функцию is_year_leap, которая принимает число (год) и
# возвращает true, если год високосный false если нет.

def find_number_of_days_in_a_year(year) -> bool:
    """
    :param year : int
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print(find_number_of_days_in_a_year(2020))


# 2 Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список, состоящий из кубов первых
# n натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3]. Обязательно использование генераторов списков.


def generate_natural_cubes(n) -> list:
    """
    :param : int
    """
    return [i ** 3 for i in range(1, n+1)]


natural_cubes = generate_natural_cubes(10)
print(natural_cubes)


# 3 Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*args) -> list:
    """
    :param args : int
    """
    return [i ** 2 for i in args]


squares_of_list = generate_squares(1, 5, 6, 1, 5, 6)
print(squares_of_list)


# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

def get_longest_word(striing) -> str:

    """
    :param striing : str
    """
    str_to_array = striing.split()
    longest_word = ""
    for i in str_to_array:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word

print(get_longest_word("Francisco is one of John Galt's two closest friends and an indispensable ally in the strike"))


