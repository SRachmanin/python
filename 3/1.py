def my_func():
    num_one = int(input('Введите первое число: '))
    num_two = int(input('Введите второе число: '))
    if num_two != 0:
        result = num_one / num_two
    else:
        print('На ноль делить нельзя!')
        num_two = int(input('Введите второе число: '))
        result = num_one / num_two
    return result

print(my_func())