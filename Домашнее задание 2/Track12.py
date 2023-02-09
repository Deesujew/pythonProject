a = int(input('Введите сумму чисел: '))
b = int(input('Введите произведение чисел: '))
if (a==0 and b==0) or  (a!=0 and b==0):
    print( a,b)
else:
    for i  in range(b):
        if i == (a * i - b) ** 0.5:
            print(i, end=" ")
