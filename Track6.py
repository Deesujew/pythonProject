n = input("Введите шестизначный номер билета: ")
n = int(n)

d1 = n//100000
d2 = n//10000 % 10
d3 = n//1000 % 10
d4 = n % 1000 // 100
d5 = n % 100 // 10
d6 = n % 10

if d1+d2+d3 == d4+d5+d6:
    print (" yes ")
else:
    print (" no ")