a = int(input('Результат спортсмена в первый день (в км) - '))
b = int(input('Ожидаемый результат спортсмена (в км) - '))
day = 0

while a < b:
    a += a * 0.1
    day += 1
else:
    print('Ожидаемого результата спортсмен достигнет на ', day, 'день.')