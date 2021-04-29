# -*- coding: cp1251 -*-

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 30
        self.height = 4

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f"Для покрытия дорожного полотна неободимо {round(asphalt_mass)}т массы асфальта")


r = Road(3500, 10)
r.asphalt_mass()