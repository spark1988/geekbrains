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

class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self, other):
        return self.matrix + other
# return f'{self.matrix[0]}\n{self.matrix[1]}'


    def __add__(self, other):
        a = self.matrix[0]
        b = self.matrix[1]
        c = other[2]
        d = other[3]
        c.extend([0, ] * (len(d) - len(c)))
        d.extend([0, ] * (len(c) - len(d)))
        a.extend([0, ] * (len(b) - len(a)))
        b.extend([0, ] * (len(a) - len(b)))
        data = []
        data.append(list(map(sum, zip(a, c))))
        data.append(list(map(sum, zip(b, d))))
        return data

matrica = [[1, 2, 4], [4, 5, 7]]
matrica2 =[[4, 33, 22], [6, 4, 7]]



m = Matrix(matrica)

print(matrica + matrica2)
print(m.__add__(matrica + matrica2))






