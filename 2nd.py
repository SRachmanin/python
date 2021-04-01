user_count = int(input('Введите время в секундах - '))

hours = user_count // 3600
minutes = (user_count - hours * 3600) // 60
seconds = user_count - (hours * 3600 + minutes * 60)

if hours < 10:
    hours = '0' + str(hours)
else:
    hours = str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = str(seconds)

result = [hours, minutes, seconds]

if user_count > 86400:
    print('Вы ввели слишком большое число.')
elif user_count < 0:
    print('Вы ввели слишком маленькое число.')
elif user_count > 0 and user_count <= 86400:
    print(f"Время: {':'.join(result)}")