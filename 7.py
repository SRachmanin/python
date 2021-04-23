def fact(n):
    step = 1
    for i in range(1, n + 1):
        step *= i
        yield step


n = int(input("Введите значение n: \n"))
j = 0
for _ in fact(n):
    if j == n:
        break
    else:
        j += 1
        print(f"Факториал {j} - {_}")