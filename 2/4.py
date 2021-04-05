user_str = input('Напишите несколько слов через пробел: ')
user_str = user_str.split()
for i, item in enumerate(user_str):
    if len(user_str) < 11:
        print(i + 1, item[0:10])
    else:
        print(i + 1, item)
