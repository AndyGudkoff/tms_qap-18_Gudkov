# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

name_print = lambda name: print(f'Hello {name}')
name_print('Andrei')

# 2 Создать lambda функцию, которая принимает на вход список имен и
# выводит их в формате “Hello, {name}” в другой список
list_of_names = lambda names: print([f'Hello {name}' for name in names])
list_of_names(['Ilia', 'Andrei', 'Ihar'])

# ----
# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и возвращает новый список только с положительными числами


def list_of_floats(list):
    for number1 in list:
        if number1 > 0:
            yield number1


list_with_positive = []

leave_only_positive_generator = list_of_floats([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])
for number in leave_only_positive_generator:
    list_with_positive.append(number)

print(list_with_positive)

# 2 Необходимо составить список чисел которые указывают на длину слов в строке:
# sentence = " thequick brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений

sentence = " thequick brown fox jumps over the lazy dog"
to_list = sentence.split()
list_with_lenght = []

for word in to_list:
    try:
        if word != 'the':
            list_with_lenght.append(len(word))
        else:
            raise Exception
    except Exception:
        print("The is found")

print(list_with_lenght)


# ----
# Шифр Цезаря * — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# ● hello world! -> khoor zruog!
# ● this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.

alpabet = "abcdefghijklmnopqrstuvwxyz"


def to_encode(input_string, num):
    encoded = ''
    for char in input_string:
        if char.isalpha():
            index = alpabet.index(char)+num
            if index >= len(alpabet):
                index -= len(alpabet)
            encoded += alpabet[index]
        else:
            encoded += char
    return encoded


print(to_encode('hello world!', 3))


def to_decode(input_string, num):
    decoded = ''
    for char in input_string:
        if char.isalpha():
            index = alpabet.index(char)-num
            if index < 0:
                index += len(alpabet)
            decoded += alpabet[index]
        else:
            decoded += char
    return decoded


print(to_decode('this is a test string', 21))
