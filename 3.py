# -*- coding: cp1251 -*-

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f"Текущий список - {self.my_list} \n ")
            except:
                print(f"Недопустимое значение!")
                yes_or_no = input(f"Попробовать еще раз? Y/N ")

                if yes_or_no == 'Y' or yes_or_no == 'y':
                    print(try_except.my_input())
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    return f"До свидания."
                else:
                    return f"До свидания."
                break


try_except = Error(1)
print(try_except.my_input())
