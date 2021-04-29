# -*- coding: cp1251 -*-

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f"��� �����!"
                else:
                    return f"������������ ���"
            else:
                return f"������������ �����"
        else:
            return f"������������ ����"

    def __str__(self):
        return f"������� ���� - {Data.extract(self.day_month_year)}"


today = Data('3 - 5 - 2021')
print(today)
print(Data.valid(13, 13, 2022))
print(today.valid(13, 3, 2013))
print(Data.extract('15 - 5 - 2005'))
print(today.extract('15 - 5 - 2021'))
print(Data.valid(13, 1, 2003))