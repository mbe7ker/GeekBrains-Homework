def my_func(var_1, var_2, var_3):
    return print(var_1 + var_2 + var_3 - min([var_1, var_2, var_3]))


inp_1 = float(input("Введите 1-е число: "))
inp_2 = float(input("Введите 2-е число: "))
inp_3 = float(input("Введите 3-е число: "))

my_func(inp_1, inp_2, inp_3)
