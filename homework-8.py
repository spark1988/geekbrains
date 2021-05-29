# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import datetime

class Data():

    def __init__(self, str_data):
        self.str_data = str_data

# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12)

    def validation(self):
        a = (list(self.split('-')))
        if int(a[0]) > 0 and int(a[0]) < 32:
            print('Значение верное')
        elif isinstance(a[0], int):
            print('значение должно быть числом')
        else:
            print('значение должно быть в пределах от 0 до 31')
        a = (list(self.split('-')))
        if int(a[1]) > 0 and int(a[1]) < 13:
            print('Значение верное')
        elif isinstance(a[1], int):
            print('значение должно быть числом')
        else:
            print('значение должно быть в пределах от 0 до 12')
        if int(a[2]) > 0:
            print('Значение верное')
        elif isinstance(a[0], int):
            print('значение должно быть числом')
        else:
            print('значение должно быть > 0')

    def time_func_convert(self):

        print((datetime.strptime(self, '%d-%m-%Y')))


Data.validation('31-01-2012')
Data.time_func_convert('31-01-2012')

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Exception():

    def zero(num1, num2):
        try:
            print(int(num1/num2))
        except ZeroDivisionError as Z:
            print( f'{Z} ну так нельзя')

Exception.zero(30,5)


# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо
# реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и
# отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
class New:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево ")
                y_or_n = input(f'Если хочешь выйти из программы то введи stop ')

                if y_or_n.lower() == 'y':
                    print(N.my_input())
                elif y_or_n.lower() == 'stop':
                    print(f'Вы вышли {self.my_list}')
                    break
                else:
                        print( f'введите нормальное значение Y или stop для текущего списка {self.my_list}')
                continue

N = New(2)
print(N.my_input())


