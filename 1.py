from sys import argv
def my_salary():
    file_name, time, rate, bonus = argv
    return print(f"Заработная плата составляет - {(float(time) * float(rate)) + float(bonus)}")
my_salary()