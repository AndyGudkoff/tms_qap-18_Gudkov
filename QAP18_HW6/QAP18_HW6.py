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





# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.


list_with_real_numbers = read_file('fileWithRealNumbers.txt')
splited = list_with_real_numbers.split()
squared_numbers = []

for i in range(len(splited)):
    splited[i] = str(float(splited[i]) ** 2)
    squared_numbers.append(splited[i])

file = open('FileWithSquaredOfFloats.txt','w')
file.write(str(squared_numbers))
file.close()




# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа


def swap_files (file1, file2):
    with open(file1, 'rb') as f1:
        data1 = f1.read()
    with open(file2, 'rb') as f2:
        data2 = f2.read()

    with open(file1, 'wb') as f1:
        f1.write(data2)
    with open(file2, 'wb') as f2:
        f2.write(data1)


file1 = "firstFile.txt"
file2 = "secondFile.txt"

swap_files(file1, file2)
