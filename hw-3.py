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

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
# этого завершить программу.
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        numbers = input('Введи числа для выхода из программы нажмите Q - ').split()

        res = 0
        for number in range(len(numbers)):
            if numbers[number].lower() == 'q':
                ex = True
                break
            elif numbers[number].isdigit() == False:
                print('символы всё сломали!!')
                ex = True
                break
            elif numbers[number].isdigit() == False:
                res = res + int(numbers[number-1]) - int(numbers[number-1])
                ex = True
                print('символы всё сломали, но программа подсчитала!')
                break
            else:
                res = res + int(numbers[number])
        sum_res = sum_res + res
        print(f'Текущая сумма чисел =  {sum_res}')
my_sum()

6. 

import re

def word_func(*args):

    words = input('введите слова через пробел на русском/латинице:  ').lower().title()
    question = input('на каком языке вывести текст? ru/eng')
    russian_words = " ".join(re.findall(r"[а-я ]+", words, re.I))
    english_words = " ".join(re.findall(r"[a-z ]+", words, re.I))

    if question.lower() == 'ru':
        print(russian_words)
    elif question.lower() == 'eng':
        print(english_words)
    else:
        print('такого языка не предлагалось выбрать!')

word_func()
