#Хотелось сделать через лямда-функцию, т.к. решение нравится больше, но что-то не работает.
#Через нее вообще реально сделать подобное задание или я брежу?


my_words = lambda name='lalala': name.title()


words = input('Напишите несколько слов через пробел: ')
for i in words:
    result = my_words(i)
print(f"Результат: {result}")