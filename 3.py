with open('salary.txt', 'r') as f:
    salary = []
    middle = []
    f = f.read().split('\n')
    for i in f:
        i = i.split()
        if int(i[1]) < 20000:
           middle.append(i[0])
           salary.append(i[1])
print(f"Оклад меньше 20000: {middle}\nСредний оклад: {sum(map(int, salary)) / len(salary)}")
