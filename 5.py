# -*- coding: cp1251 -*-
def my_sum():
    try:
        with open('sum.txt', 'w+') as f:
            num = input('Введите цифры через пробел: \n')
            f.writelines(num)
            my_numb = num.split()
            print(sum(map(int, my_numb)))
    except ValueError:
        print('Введены неверные значения.')
my_sum()