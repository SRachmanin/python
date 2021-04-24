my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
translate = []
with open('numbers.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        translate.append(my_dict[i[0]] + ' ' + i[1])

with open('numbers_rus.txt', 'w') as f:
    f.writelines(translate)