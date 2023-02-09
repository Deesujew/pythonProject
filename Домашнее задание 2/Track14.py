N = input("Введите число:")
N = int(N)
k = 0
while 2**k <= N:
    print (2**k, end=" ")
    k += 1
