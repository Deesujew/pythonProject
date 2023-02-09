n = int(input('Введите количество монеток: '))
count = 0
for i in range(n):
    temp = int(input())
    if temp == 0:
        count += 1
if n / 2 > count:
    print(count)
else:
    print(n-count)




