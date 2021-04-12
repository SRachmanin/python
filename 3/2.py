def users_inf():
    name = input('Ваше имя: ')
    surname = input('Ваша фамилия: ')
    birthday = input('Год вашего рождения: ')
    city = input('Город вашего проживания: ')
    email = input('Ваш email: ')
    phone = input('Номер вашего телефон: ')
    return name, surname, birthday, city, email, phone
name, surname, birthday, city, email, phone = users_inf()
print(f"Имя - {name}; Фамилия - {surname}; Год рождения - {birthday}; Город - {city}; Email - {email}; Телефон - {phone}")