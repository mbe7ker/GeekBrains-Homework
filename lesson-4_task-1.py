from sys import argv

salary_parameters, num_of_hours, salary_per_hour, bonus = argv


def salary(a, b, c):
    x = int(a) * int(b) + int(c)
    return print(x)


salary(num_of_hours, salary_per_hour, bonus)
