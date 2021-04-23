from itertools import count, cycle
#
# for el in count(int(input('Введите начальное значение последовательности (до 20): '))):
#     if el <= 20:
#         print(el)
#     else:
#         break

some_list = [1, 2, 3]
i = 0
for el in cycle(some_list):
    if i > 10:
        break
    else:
        print(el)
    i += 1