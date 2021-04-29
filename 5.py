# -*- coding: cp1251 -*-

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"������ ���������"


class Pen(Stationery):
    def draw(self):
        return f"������ ��������� {self.title}"


class Pencil(Stationery):
    def draw(self):
        return f"������ ��������� {self.title}"


class Handle(Stationery):
    def draw(self):
        return f"������ ��������� {self.title}"


pen = Pen("������")
print(pen.draw())
pencil = Pencil("����������")
print(pencil.draw())
handle = Handle("��������")
print(handle.draw())