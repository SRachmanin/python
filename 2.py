list_1 = [4, 29, 138, 8, 1, 1, 0, 421, 17, 1, 45, 376, 8, 91, 3]
my_list = []
for i in range(len(list_1) - 1):
    if list_1[i] < list_1[i+1]:
        my_list.append(list_1[i+1])
print(my_list)