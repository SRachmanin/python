def my_sum(var_1, var_2, var_3):
    if var_3 <= var_2 <= var_1:
        return var_1 + var_2
    elif var_2 <= var_3 <= var_1:
        return var_1 + var_3
    elif var_2 <= var_1 <= var_3:
        return var_1 + var_3
    else:
        return var_2 + var_3


print(f"Сумма двух наибольших аргументов: - {my_sum(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))}")