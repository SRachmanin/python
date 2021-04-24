with open('some_data.txt', 'w', encoding='utf-8') as f:
    line = input('Вводите данные через enter: \n')
    while line:
        f.writelines(line + '\n')
        line = input('Вводите данные через enter: \n')
        if not line:
            break

with open('some_data.txt') as f:
    data = f.read()
    print(f"some_data.txt:\n{data}")