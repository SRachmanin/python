# -*- coding: cp1251 -*-

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('������� �������� � ��������� Enter - '))
                self.my_list.append(val)
                print(f"������� ������ - {self.my_list} \n ")
            except:
                print(f"������������ ��������!")
                yes_or_no = input(f"����������� ��� ���? Y/N ")

                if yes_or_no == 'Y' or yes_or_no == 'y':
                    print(try_except.my_input())
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    return f"�� ��������."
                else:
                    return f"�� ��������."
                break


try_except = Error(1)
print(try_except.my_input())
