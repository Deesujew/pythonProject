from random import randint


n = int(input("Введите количество элементов в массиве:"))
list_1 = [randint(0,10) for i in range(n)]
print(list_1)
x = int(input("Введите требуемое число:"))
count = 0
for el in list_1:
    if el == x:
        count += 1
print(count)
