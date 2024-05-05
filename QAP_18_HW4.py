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