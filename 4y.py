num = int(input('Введите положительное целое число - '))
check = num % 10
num = num // 10
while num > 0:
    if num % 10 > check:
        check = num % 10
    num = num // 10
print(check)