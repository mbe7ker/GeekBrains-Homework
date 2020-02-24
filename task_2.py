new_list = []
new_element = input('Добавьте новый элемент списка: ')
new_list.append(new_element)
i = 0
while True:
    new_element = input("Продолжить список? Если да, добавьте новый элемент. Если нет, напишите 'Нет' ")
    if new_element == "Нет":
        break
    else:
        new_list.append(new_element)
        i += 1
print(new_list)
amended_list = []
n = 0
if n == i:
    amended_list.append(new_list[n])
else:
    while n < i:
        amended_list.append(new_list[n+1])
        amended_list.append(new_list[n])
        n += 2
    if n >= i:
        amended_list.append(new_list[i])
print(amended_list)
