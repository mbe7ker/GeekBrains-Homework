# Способ 1

def my_func_one(x, y):
    return print(x ** y)


num_one = float(input("Введите действительное положительное число: "))
while num_one <= 0:
    num_one = float(input("Число неверное. Введите действительное положительное число: "))
num_two = int(input("Введите целое отрицательное число: "))
while num_two >= 0:
    num_two = int(input("Число неверное. Введите целое отрицательное число: "))

my_func_one(num_one, num_two)


# Способ 2
def my_func_two(x, y):
    n = x
    for i in range(1, -y):
        n = n * x
    return print(1 / n)


num_one = float(input("Введите действительное положительное число: "))
while num_one <= 0:
    num_one = float(input("Число неверное. Введите действительное положительное число: "))
num_two = int(input("Введите целое отрицательное число: "))
while num_two >= 0:
    num_two = int(input("Число неверное. Введите целое отрицательное число: "))

my_func_two(num_one, num_two)
