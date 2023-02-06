n = input("Введите трехзначное число: ")
n = int(n)

digit1 = n % 10
digit2 = n % 100//10
digit3 = n // 100

print("Сумма цифр числа:", digit1 + digit2 + digit3)