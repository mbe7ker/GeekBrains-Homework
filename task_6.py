n = 1
total = int(input("Введите общее количество товаров: "))
my_list = []
list_names = []
list_prices = []
list_volumes = []
list_units = []

while n <= total:
    name = input("Введите название товара " + str(n) + ": ")
    price = int(input("Введите цену товара " + str(n) + ": "))
    volume = int(input("Введите количество товара " + str(n) + ": "))
    unit = input("Введите единицу для товара " + str(n) + ": ")
    goods = {"название": name, "цена": price, "количество": volume, "ед": unit}
    my_tuple = (n, goods)
    my_list.append(my_tuple)
    list_names.append(name)
    list_prices.append(price)
    list_volumes.append(volume)
    list_units.append(unit)
    n += 1
print(my_list)

dict_output = {"название": list_names, "цена": list_prices, "количество": list_volumes, "ед": list_units}
print(dict_output)
