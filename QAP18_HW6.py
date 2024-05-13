# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку


def read_file(path):
    f1 = open(path,'r')
    daten = f1.read()
    f1.close()
    return daten
date_from_file = read_file('file_with_ints.txt')
listik = date_from_file.split()
print(listik)
if len(listik) < 3:
    print("Error")
else:
    print(listik[0], listik[1], listik[len(listik)-2])


# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.


date_from_file = read_file('file_with_ints.txt')
list_with_all_integers = date_from_file.split()

odd = []
ints = []
for i in list_with_all_integers:
    if int(i) % 2 == 0:
        ints.append(i)
    else:
        odd.append(i)

file1 = open('FileWithIntegers.txt', 'w')
file1.write(str(ints))
file1.close()

file2 = open('FileWithOddNumbers.txt', 'w')
file2.write(str(odd))
file2.close()