# -*- coding: cp1251 -*-

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f"������ �����: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}"

    @abstractmethod
    def abstract(self):
        return '_'


class Coat(Clothes):
    def consumption(self):
        return f"��� ������ ������: {self.param / 6.5 + 0.5 :.1f}� �����"

    def abstract(self):
        return '__'


class Costume(Clothes):
    def consumption(self):
        return f"��� ������ �������: {2 * self.param + 0.3 :.1f}� �����"

    def abstract(self):
        pass


coat = Coat(350)
costume = Costume(105)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())