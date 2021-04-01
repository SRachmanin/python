gain = int(input('Введите сумму выручки фирмы - '))
expenses = int(input('Введите сумму издержек фирмы - '))

if gain > expenses:
    print('У вас прибыльный бизнес!')
elif gain < expenses:
    print('Ваша компания работает в убыток!')
elif gain == expenses:
    print('Ваша компания работает не в убыток, но и прибыли не приносит. Стоит что-то изменить!')

profit = gain - expenses
rent = profit / gain
print('Рентабельность вашей выручки: ', rent)

staff = int(input('Сколько сотрудников в вашей фирме? - '))

rent_staff = profit / staff
print('Прибыль фирмы в расчете на одного сотрудника: ', rent_staff)