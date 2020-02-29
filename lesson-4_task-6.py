from itertools import count, cycle

for el in count(10):
    if el > 150:
        break
    else:
        print(el)

# Добавил значение, при котором цикл разрывается, иначе он будет продолжаться бесконечно

c = 0
my_list = ["A", "и", "Б", "сидели", "на", "трубе"]
for el in cycle(my_list):
    if c > 150:
        break
    print(el)
    c += 1

# Добавил счетчик для разрыва цикла, иначе он будет идти бесконечно
