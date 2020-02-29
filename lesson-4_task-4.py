my_list = [45, 65, 23, 7, 9, 37, 865, 7, 9, 3, 24, 3, 85, 19, 65]

new_list = []
for el in my_list:
    if my_list.count(el) == 1:
        new_list.append(el)
print(new_list)
