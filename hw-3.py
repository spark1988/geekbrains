# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку ситуации деления на ноль.
def division_numbers(num1, num2):
    if num1 > 0 and num2 > 0:
        result = int(num1 / num2)
    else:
        print('делить на 0 нельзя')
    return result

print(division_numbers(4, 1))

# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def user(**datas):
    return datas

print(user(name = 'vlad', surname = 'vologodskiy', age = 32, male = True))

# 3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(num1, num2, num3):
    table = [num1, num2, num3]
    table.sort()
    result = table[1] + table[2]
    return result

print(my_func(9, 5, 6))


# 4. Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.
def multiple(x, y):
    mistake = 'число должно быть меньше 0'
    if y < 0:
        result = int(x) ** int(y)
    else:
        print(mistake)
    return result

print(multiple(5, -2))


def division_minus(num1, num2):
    formula = (1/(num2 ** num1))
    table = []
    if num2 < 0:
        table.append(formula)

        for i in table:
            return i



print(division_minus(4, -3))
