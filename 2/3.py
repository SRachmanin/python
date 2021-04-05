# user_num = int(input('Введите номер месяца: '))
# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#
# if user_num >= 1 and user_num <= 12:
#     print(months[user_num - 1])
# else:
#     print('Нет такого месяца!')
#     user_num = int(input('Попробуйте еще раз: '))
#     print(months[user_num - 1])

user_num = int(input('Введите номер месяца: '))
months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

if user_num >= 1 and user_num <= 12:
    print(months[user_num])
else:
    print('Нет такого месяца!')
    user_num = int(input('Попробуйте еще раз: '))
    print(months[user_num])
