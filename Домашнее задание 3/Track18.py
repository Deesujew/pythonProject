from random import randint


n = int(input("Введите количество элементов в массиве:"))
list_1 = [randint(0,10) for i in range(n)]
print(list_1)
x = int(input("Введите требуемое число:"))
min = 10
el=list_1[0]
for i in list_1:
    if i - x <= min:
        el = i
        min = el-i
print(" самый близкий к заданному числу элемент массива: ", el)
