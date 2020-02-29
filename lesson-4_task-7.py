from math import factorial


def fibo_gen(my_list):
    new_list = []
    for el in my_list:
        new_list.append(factorial(el))
    return new_list


inp_list = [el for el in range(1, 100)]


def generator():
    for el in fibo_gen(inp_list):
        yield el


g = generator()
n = 1
for el in g:
    if n <= 15:
        print(el)
        n += 1
