import sys

file_name = sys.argv[0]
worked_hour = input('Введите часы работы в месяц: ')
rate = input('Введите зарплату в час:')
benefit = input('Какая премия? ')

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Зарплата вашего сотрудника = {calculation}")


# 2.
# Пример
# исходного
# списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

g = (a[i] for i in range(1, len(a)) if a[i] > a[i - 1])
# классический
# вывод
for i in g:
    print(i)
# через
# генератор
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# классическое
# решение
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# 3.
num = (i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0)
# классический
# перебор
for i in num:
    print(i)
# через
# генератор
print(num)
print(next(num))
print(next(num))
print(next(num))
print(next(num))

# 4.
# списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = (el for el in my_list if my_list.count(el) == 1)
print(next(new))
print(next(new))
print(next(new))
print(next(new))
print(next(new))
print(next(new))

# 5.

from functools import reduce

items = list(range(99, 1001))

new = (el for el in items if el % 2 == 0)

sum_all = reduce(lambda x, y: x * y, new)

print(sum_all)


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть
# условие, при котором повторение элементов списка будет прекращено.


def numbers(num1):
    try:
        for i in count(num1, 1):
            if i > 10:
                break
            else:
               print(i)
    except: ValueError

print(numbers(4))

from itertools import count, cycle

def numbers_cycle():

    for item in cycle([1,2,3,4,5,6,7,8,9,10,11]):
        if item >= 11:
            break
        print(item)
        item += 1
print(numbers_cycle())

# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# # Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def func():
    n = int(input('введите n'))

    factorial = 1

    for i in range(2, n + 1):
            factorial *= i
            yield factorial

print((func()))

for b in func():
    print(b)
