# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list_1 = [randint(0,10) for i in range(20)]
print(list_1)
minimum = int(input("Введите минимум:"))
maximum = int(input("Введите максимум:"))
list_2 = []
for i in range(len(list_1)):
    if minimum <= list_1[i] <= maximum:
        list_2.append(i)

print(list_2)

