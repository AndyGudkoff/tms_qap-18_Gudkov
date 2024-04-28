# 1 Привести к целому типу - 1.6, 2.99
def to_int(arr):
    whole = int(arr)
    return whole


print(to_int(1.6))
print(to_int(2.99))

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
str_my_site = "www.my_site.com#about"


def replace_sharp_by_slash(site):
    return site.replace('#', '/')


print(replace_sharp_by_slash(str_my_site))

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’


def str_plus_ing(string):
    return string + "ing"


print(str_plus_ing('zxcv'))

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
str_ivanou_ivan = 'Ivanou Ivan'


def replace_name_and_surname_place(name_surname):
    str_to_list = (name_surname.split())
    name_surname = str_to_list[1] + ' ' + str_to_list[0]
    return name_surname


print(replace_name_and_surname_place(str_ivanou_ivan))

# 5 Напишите программу которая удаляет пробел в начале, в конце строки
str_with_space = "   qwerty     "


def delete_empty_spaces_inside_list (list):
    return list.strip(' ')

print(delete_empty_spaces_inside_list(str_with_space))

# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся
# в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

school = {"1a": 15, "1б": 11, "1в": 4, "2a": 9, "2б": 12, "2в": 1, "2г": 18, "3а": 24, "3б": 27,
          "4а": 22, "4в": 21, "4г": 30}

# 7 Создайте список и извлеките из него списка второй элемент.
list_to_grab_second_element = [5, 2, 15, 19, 18]


def take_second_el_from_list(list):
    return list[1]


print(take_second_el_from_list(list_to_grab_second_element))

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
stroka_to_compare_first = 'employ'
stroka_to_compare_second = 'employment'


def if_str1_in_str2(str1, str2):
    return str1 in str2


print(if_str1_in_str2(stroka_to_compare_first,stroka_to_compare_second))