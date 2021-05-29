 # 1. Реализовать класс «Дата», функция-конструктор которого должна
# # принимать дату в виде строки формата «день-месяц-год».
# # В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# # должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# # Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# # (например, месяц — от 1 до 12).
# # Проверить работу полученной структуры на реальных данных.
from datetime import datetime
# #
class Data():

    def __init__(self, str_data):
        self.str_data = str_data
#Как реализовать обертку валидацию? Чтобы корректно работала не получилось реализовать:((
    def wrapper_validation():
        def hello_world():
            getNumber = input('Введите целое положительное число: ')  # Ввод числа
            if getNumber.isdigit(): return getNumber

        return hello_world()

        return wrapper_validation()

# #
# # # должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12)

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
    @wrapper_validation
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

# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q.lower() == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        while True:
            a =  input('*' * 10 + ' have a nice typing ' + '*' * 10 + '\n')
            print("\033[34m {}".format(a))
            b = input('остановить безумие Y')
            if b == 'y':
                break


class Scanner(StoreMashines):
    def to_scan(self):
        import time

        print ("Scanning.")

        print ("Scanning.   ")
        time.sleep(1)
        print ("\rScanning..  ")
        time.sleep(1)
        print ("\rScanning... ")
        time.sleep(1)
        print ("\rScanning....")
        time.sleep(1)
        return ("\rКонец.   ")


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)

# print(unit_1.reception())
# # print(unit_2.reception())
#
# print(unit_1.to_print())
# print(unit_2.to_scan())


# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.



class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)


