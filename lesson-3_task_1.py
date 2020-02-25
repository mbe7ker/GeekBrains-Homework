def my_func(var_1, var_2):
    return print(var_1 / var_2)


inp_1 = float(input("Введите числитель: "))
inp_2 = float(input("Введите знаменатель: "))

while inp_2 == 0:
    inp_2 = float(input("На ноль делить нельзя. Введите знаменатель еще раз: "))

my_func(inp_1, inp_2)
