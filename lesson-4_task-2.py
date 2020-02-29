my_list = [300, 250, 680, 430, 4, 8, 125, 420, 56, 34, 45, 7, 12]
new_list = [el for el in my_list if
            my_list.index(el) > 0 and my_list[my_list.index(el)] > my_list[my_list.index(el) - 1]]
# Первое число в списке my_list не берем в расчет, так как перед ним нет других элементов. В связи с этим условие my_list.index(el) > 0
print(new_list)
