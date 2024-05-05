import re


from collections import Counter


# Работа с переменными:
# 1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No". 2. Измените значение,
# хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int.

var_int = 10
var_float = 8.4
var_str = "No"
big_int = var_int * 3.5

# 2. Измените значение, хранимое в переменной var_float, уменьшив его на единицу, результат свяжите с той же переменной.
var_float -= 1

# 3. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни
# к каким переменным.
print(var_int/var_float)
print(big_int/var_float)

# 4. Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения используйте
# операции конкатенации (+) и повторения строки (*). 6. Выведите значения всех переменных.

var_str = var_str * 2 + "YesYesYes"
print(var_int, var_str, var_float, big_int)

# Строки:
# # 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# # Извлеките из строки первый символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
stroka = "EightSymbols"

# # 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
str_15_symbols = "Programming"
print(str_15_symbols[0:8])
print(str_15_symbols[4:8])
print(str_15_symbols[0:11:3])
print(str_15_symbols[-1:-12:-1])

# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
my_name_string = "my name is Andrei"
print(my_name_string)

# 4. Есть строка: test_tring = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”

test_tring = "Hello world!"
print(test_tring.find('w'))
print(test_tring.count('l'))
print((test_tring[0:5]) == 'Hello')
print((test_tring[9:12]) == 'qwe')


# Списки:
# 1. Создайте два любых списка и свяжите их с переменными.
listochek = [1, 5, 9, 10]
listochek1 = [2, 10, 15, 20]

# 2. Извлеките из первого списка второй элемент.
print(listochek[0])

# 3. Измените во втором списке последний элемент. Выведите список на экран.
print(listochek1[len(listochek1) - 1])  # Output of the Current last element
listochek1[len(listochek1) - 1] = 44
print(listochek1[len(listochek1) - 1])  # Output of the last element after change.

# 4. Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран.
concat_of_two_lists = listochek + listochek1
print(concat_of_two_lists)

# 5. "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части обоих первых списков.
# Срез свяжите с очередной новой переменной. Выведите значение этой переменной.
new_list_with_parts_of_two_lists = concat_of_two_lists[2:6]
print(new_list_with_parts_of_two_lists)

# 6. Добавьте в список два новых элемента и снова выведите его.
concat_of_two_lists += 2, 10
print(concat_of_two_lists)

# 7. Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков. -- !не использовать циклы
first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result_with_common_element_of_first_and_second_lists = list(set(first_list) & set(second_list))
print(result_with_common_element_of_first_and_second_lists)

# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные значения.
# !не использовать циклы
list_with_non_unique_values = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(list_with_non_unique_values)))

# Логические операции:
# 1. Присвойте двум переменным любые числовые значения.
int1 = 15
int2 = 2

# 2. Составьте четыре сложных логических выражения с помощью оператора and, два из которых должны давать истину,
# а два других - ложь.
print(int1 == 15 and int2 > 1)
print(int2 != 5 and int1 < 100)
print(int1 != 15 and int2 < 100)
print(int2 != 5 and type[int1] == list)


# 3. Аналогично выполните п. 2, но уже используя оператор or.
print(int1 != 15 or int2 > 1)
print(int2 == 4 or int1 == 10)
print(int1 != 15 or int2 < 100)
print(type[int2] == bool or type[int1] == list)


# 4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа.
str_for_complex_expression_one = "Python"
str_for_complex_expression_two = "nohtyP"
print(str_for_complex_expression_one == str_for_complex_expression_two)
print(str_for_complex_expression_one != str_for_complex_expression_two)
print(type(str_for_complex_expression_one) == str and type(str_for_complex_expression_two) == set)
print(str_for_complex_expression_one.isnumeric() or str_for_complex_expression_two.upper().isupper())


# Словари:
# 1. Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a": 24, "1b": 19, "1c": 5, "2a": 17, "2b": 14, "3a": 30, "3b": 32, "3v": 12, "4a": 18, "4b": 36}

# 2. Узнайте сколько человек в каком-нибудь классе.
print(school["3b"])

# 3. Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;
# ◦ в школе появилось два новых класса;
# ◦ в школе расформировали один из классов.
print(school["1b"], school["3v"], school["4b"])  # Output before quantity of class members changed.
school["1b"] = 44    # Change number of members of 1b class to 44
school["3v"] = 35    # Change number of members of 3v class to 35
school["4b"] = 11    # Change number of members of 4b class to 11
print(school["1b"], school["3v"], school["4b"])   # Output after quantity of class members changed.

school["5a"] = 40   # Adding new class
school["5b"] = 41   # Adding new class
print(school["5a"], school["5b"])  # Output of new classes

del school["1a"]    # Deleting 1a class

# 4. Выведите содержимое словаря на экран.
print(school)


# Преобразование типов
# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
robin_singh = "Robin Singh"
arr_robin_singh = robin_singh.split(' ')
print(arr_robin_singh)

love_array = "I love arrays they are my favorite"
arr_love_array = love_array.split(' ')
print(arr_love_array)

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
list_ivan_ivanou = ["Ivan", "Ivanou"]
lovely_city = "Minsk"
lovely_country = "Belarus"
print(f'Привет, {list_ivan_ivanou[0]} {list_ivan_ivanou[1]}! Добро пожаловать в {lovely_city} {lovely_country}')

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list_i_love_arrays = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(list_i_love_arrays))

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
list_with_10_elements = [1, 5, 15, 25, 30, 35, 40, 45, 50, 55]
list_with_10_elements[2] = 20
del list_with_10_elements[6]
print(list_with_10_elements)

# 5. Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3} b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список,# если у одного словаря есть ключ "а",
# а у другого нету, то поставить значение None на соответствующую
# # позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
list_of_keys = list(a) + list(b)
print(list_of_keys)
ab = {}
keys = set(a.keys()).union(b.keys())
for key in keys:
    values = [a.get(key), b.get(key)]
    ab[key] = values

print(ab)

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
arr_with_non_unique_values = [1, 5, 2, 9, 2, 9, 1]


def find_unique_element_in_list (listxczvvz):
    for el in listxczvvz:
        if listxczvvz.count(el) < 2:
            return el
    print('No unique element was founded')
find_unique_element_in_list(arr_with_non_unique_values)


# *2) Дан текст, который содержит различные английские буквы и знаки препинания.
# Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте,
# что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква,
# которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
# "a-z" == "a"
# "Hello World!" == "l"
# "How do you do?" == "o" "One" == "e"
# "Oops!" == "o"
# "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"

zxcv = "a" * 9000 + "b" * 1000


def most_common_letter(textzcxvzx):
    # Преобразовать текст в нижний регистр
    textzcxvzx = textzcxvzx.lower()
    # Отфильтровать только буквы
    letters = re.findall('[a-z]', textzcxvzx)
    # Подсчитать частоту каждой буквы
    letter_counts = Counter(letters)
    # Найти наиболее частую букву
    most_common = max(letter_counts, key=letter_counts.get)
    most_common = min(most_common)

    return most_common

print(most_common_letter(zxcv))

# Условия
# 1. Дано целое число. Если оно является положительным, то прибавить к нему 1;
# в противном случае не изменять его. Вывести полученное число.


def check_if_number_pos_or_negative (number) -> int:
    if(number>0):
        number += 1
        return number
    else:
        return number
print(check_if_number_pos_or_negative(-1))

# 2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
first = -1
second = -1
third = -5
counter = 0
listfromnumbers = [first, second, third]

for el in listfromnumbers:
    if el > 0:
        counter += 1
print(counter)


# 3. Дан номер года (положительное целое число). Определить количество дней в этом году, учитывая,
# что обычный год насчитывает 365 дней, а високосный — 366 дней. Високосным считается год,
# делящийся на 4, за исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 являются).


def find_number_of_days_in_a_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        number_of_days_in_year = 366
        return number_of_days_in_year
    else:
        number_of_days_in_year = 365
        return number_of_days_in_year


print(find_number_of_days_in_a_year(1200))

# 4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).


def find_day_name (number):
    if number == 1:
        return "понедельник"
    elif number == 2:
        return "вторник"
    elif number == 3:
        return "среда"
    elif number == 4:
        return "четверг"
    elif number == 5:
        return "пятница"
    elif number == 6:
        return "суббота"
    elif number == 7:
        return "воскресенье"
    else:
        return "Некорректный день"


print(find_day_name(7))

# 5. Единицы массы пронумерованы следующим образом:
# 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
# Дан номер едини- цы массы (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное число).
# Найти массу тела в килограммах.


def mass_converter(unit, mass):
    if unit == 1:
        return mass
    elif unit == 2:
        return mass / 1000000
    elif unit == 3:
        return mass / 1000
    elif unit == 4:
        return mass * 1000
    elif unit == 5:
        return mass * 100


unit = 3
mass = 10

print(mass_converter(unit, mass))

# Цикл for
# 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.


def find_sum_if_two_number(A, B):
    summa_elementos = 0
    for el in range(A, B + 1):
        summa_elementos += el
    return summa_elementos


print(find_sum_if_two_number(1, 10))

# 2. Найти сумму всех натуральных чисел в от A до B


def find_sum_of_all_integers_in_range(A, B):
    summ_of_integer = 0
    if A > B:
        A,B = B, A
    if A <= 0:
        A = 1
    if B <= 0:
        return 0
    for el in range(A, B+1):
        summ_of_integer = B - A + 1
        return summ_of_integer


print(find_sum_of_all_integers_in_range(-5,10))



# 3. Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.


def count_positive_and_negative():
    positive_product = 1
    negative_sum = 0
    negative_count = 0

    for el in range(10):
        num = int(input("Enter Integer: "))
        if num > 0:
            positive_product *= num
        elif num < 0:
            negative_sum += num
            negative_count += 1

    return positive_product, negative_sum, negative_count

print(count_positive_and_negative())


# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12 Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17

dict_with_swimmers = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12,
                      "Давидович Татьяна": 30, "Дешук Дмитрий": 24.01, "Казак Анна": 28.17}

best_result = float(100000000000)

for swimmer, result in dict_with_swimmers.items():
    if result < best_result:
        best_result = result

print(best_result)

# 5.   Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5. Напишите программу, которая будет выводить уникальное число
# massiv = [1, 5, 2, 9, 2, 9, 1,]


def find_lonely_el(listochek):
    for el in listochek:
        if listochek.count(el) < 2:
            print(el)
            return el
    print("No lonely Element")


find_lonely_el(massiv)


# Цикл while
# 1. Дано число N. Найти произведение всех чисел от 0 до N.

def proizvidenie_chisel(N):
    i = 1
    result_proizv = 1
    while i <= N:
        result_proizv *= i
        i += 1
    return result_proizv


print(proizvidenie_chisel(5))


# 2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта увеличивается втрое.
# Через сколько лет площадь первых сортов будет составлять меньше 10% от площади вторых сортов.


def calculate_years(S1, S2):

    years = 0
    while S1 / S2 >= 0.1:
        S1 *= 2
        S2 *= 3
        years += 1
    return years


print(calculate_years(1,10))

# 3. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от деления,
# найти количество и сумму его цифр.


def calculate_digits(N):

    digit_count = 0
    digit_sum = 0

    while N > 0:
        digit = N % 10

        digit_count += 1
        digit_sum += digit

        N //= 10

    return digit_count, digit_sum


print(calculate_digits(12345))



# 4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше внука.
# И сколько при этом лет будет деду и внуку.


def calculate_years(grandfather_age, grandson_age):
    years = 0
    while grandfather_age <= 2 * grandson_age:
        grandfather_age += 1
        grandson_age += 1
        years += 1

    # Return the number of years it will take, the grandfather's age at that time, and the grandson's age at that time
    return years, grandfather_age, grandson_age


print(calculate_years(50, 15))