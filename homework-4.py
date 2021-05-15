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
# Представлен
# список
# чисел.Определить
# элементы
# списка, не
# имеющие
# повторений.
# Сформировать
# итоговый
# массив
# чисел, соответствующих
# требованию.
# Элементы
# вывести
# в
# порядке
# их
# следования
# в
# исходном
# списке.
# Для
# выполнения
# задания
# обязательно
# использовать
# генератор.
# Пример
# исходного
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
# Реализовать
# формирование
# списка, используя
# функцию
# range()
# и
# возможности
# генератора.
# В
# список
# должны
# войти
# четные
# числа
# от
# 100
# до
# 1000(включая
# границы).
# Необходимо
# получить
# результат
# вычисления
# произведения
# всех
# элементов
# списка.
# Подсказка: использовать
# функцию
# reduce().
from functools import reduce

items = list(range(99, 1001))

new = (el for el in items if el % 2 == 0)

sum_all = reduce(lambda x, y: x * y, new)

print(sum_all)
