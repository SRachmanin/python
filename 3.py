# -*- coding: cp1251 -*-

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f"Размер клетки 2 в 1: {self.quantity + other.quantity}"

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f"Размер маленькой клетки: {sub} клеточек." if sub > 0 else "Клетки больше нет."

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell_one = Cell(24)
cell_two = Cell(2)
print(cell_one + cell_two)
print(cell_one - cell_two)
print(cell_one / cell_two)
print(cell_one * cell_two)
print(cell_one.make_order(7))