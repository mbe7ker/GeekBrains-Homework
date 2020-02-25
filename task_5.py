stop_symbol = "Q"
add_numbers = input(f"Введите строку чисел, разделенных пробелом. После ввода {stop_symbol} программа прекращается. - ")


def my_func(my_str):
    result = 0
    while True:
        str_list = my_str.split()
        if stop_symbol not in str_list:
            numbers_list = []
            for i in str_list:
                numbers_list.append(int(i))
            for n in numbers_list:
                result += n
            my_str = input(
                f"Введите строку чисел, разделенных пробелом. После ввода {stop_symbol} программа прекращается. - ")
        if stop_symbol in str_list:
            str_list.remove("Q")
            numbers_list = []
            for i in str_list:
                numbers_list.append(int(i))
            for n in numbers_list:
                result += n
            return print(result)


my_func(add_numbers)
