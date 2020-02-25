def int_func(word):
    return word.title()


input_str = input("Введите строку из латинских слов, разделенных пробелом, в нижнем регистре. - ")
new_list = input_str.split()
title_list = []
for i in new_list:
    title_word = int_func(i)
    title_list.append(title_word)
title_string = " ".join(title_list)
print(title_string)
