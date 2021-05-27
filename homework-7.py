# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять
# поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
from itertools import zip_longest

class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.matrix
# return f'{self.matrix[0]}\n{self.matrix[1]}'


    def __add__(self, other):
        s = []
        for i in range(len(self.matrix)):  # если в range() задан только один аргумент, отсчёт будет от 0

            # s.append(self.matrix[i] + other[i + 2])
            result = [sum(n) for n in zip_longest(self.matrix[i], other[i + 2], fillvalue=0)]
            s.append(result)
        return s


        # a = self.matrix[0]
        # b = self.matrix[1]
        # c = other[2]
        # d = other[3]
        # c.extend([0, ] * (len(d) - len(c)))
        # d.extend([0, ] * (len(c) - len(d)))
        # a.extend([0, ] * (len(b) - len(a)))
        # b.extend([0, ] * (len(a) - len(b)))
        # data = []
        # data.append(list(map(sum, zip(a, c))))
        # data.append(list(map(sum, zip(b, d))))
        # return data

matrica = [[1, 2, 4, 5], [7, 4, 5, 7]]
matrica2 =[[4, 33, 22, 6], [6, 4, 7, 9]]
matrica3 =[[4, 20, 11], [2, 3, 6]]
matrica4 =[[4, 20, 11], [2, 3, 6]]



m = Matrix(matrica)

print(matrica , matrica2)
print(m.__add__(matrica + matrica2))

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
class Clothes():
    def __init__(self, name):
        self.name = name

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def consumption(self):
        result_coat = (self.size/6.5 + 0.5)
        return result_coat

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        result_suit = (2 * self.height + 0.3)
        return result_suit

c = Coat(23)
b = Suit(45)

print(c.consumption)
print(b.consumption)
