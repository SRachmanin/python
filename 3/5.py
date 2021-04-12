def some_num():
    sum_num = 0
    while True:
        num = input('Вводите числа через пробел. Для выхода нажмите "R" \n').split( )
        for i in num:
            if i == 'R':
                return sum_num
            else:
                sum_num += int(i)
print(f"Сумма: {some_num()}")