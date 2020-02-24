new_str = input("Введите строку из нескольких слов, разделенных пробелами: ")
new_list = new_str.split()
i = 1
for word in new_list:
    print(str(i) + ". " + word[:10])
    i += 1
