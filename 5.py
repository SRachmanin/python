from functools import reduce

def my_func(x, y):
    return x * y

list_1 = range(100, 1001)
my_list = [el for el in list_1 if el % 2 == 0]

print(reduce(my_func, my_list))