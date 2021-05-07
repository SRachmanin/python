# -*- coding: cp1251 -*-

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


mat_one = Matrix([[1, 0, 3], [0, 5, 0], [-7, 0, 9], [-1, -2, -3]])
print(mat_one)
new_mat = Matrix([[-1, 0, 3], [-1, -3, 0], [0, 5, -1], [7, 0, -5]])
print(mat_one.__add__(new_mat))