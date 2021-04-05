my_list = [8, 7, 6, 3, 2]
print(f'Рейтинг - {my_list}')
user_num = int(input('Введите числа через "enter". Для выхода введите "666"): '))
while user_num != 666:
    for el in range(len(my_list)):
        if my_list[el] == user_num:
            my_list.insert(el + 1, user_num)
            break
        elif my_list[0] < user_num:
            my_list.insert(0, user_num)
        elif my_list[-1] > user_num:
            my_list.append(user_num)
        elif my_list[el] > user_num and my_list[el + 1] < user_num:
            my_list.insert(el + 1, user_num)
    print(f'Итоговый рейтинг - {my_list}')
    user_num = int(input('Введите число: '))

