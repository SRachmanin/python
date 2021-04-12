def rank(num_1, num_2):
    if num_1 < 0 or num_2 > 0:
        return 'Кто-то неправильно прочитал задание ('
    else:
        result = num_1 ** num_2
        return result
print(f"x в степени y = {rank(float(input('Введите положительное действительное число: ')), int(input('Введите отрицательное целое число: ')))}")

# def rank(num_1, num_2):
#     if num_1 < 0 or num_2 > 0:
#         return 'Кто-то неправильно прочитал задание ('
#     else:
#         result = 1
#         for i in range(num_2 * -1):
#             result *= 1 / num_1
#         return result
# print(f"x в степени y = {rank(float(input('Введите положительное действительное число: ')), int(input('Введите отрицательное целое число: ')))}")