my_list = []
print('Напишите элемент списка и нажмите "enter". Для выхода просто напишите "end".')
user_add = input('---> ')
while user_add != 'end':
    my_list.append(user_add)
    user_add = input('---> ')

n = 0
for i in range(int(len(my_list)/2)):
    my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
    n += 2
print(my_list)