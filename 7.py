# -*- coding: cp1251 -*-

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'����� z1 � z2 �����')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'������������ z1 � z2 �����')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z_1 = ComplexNumber(5, -7)
z_2 = ComplexNumber(1, 3)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)