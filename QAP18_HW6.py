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
