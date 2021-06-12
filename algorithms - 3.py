# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

diapazon = range(2, 100)
result = []

k = 2
while k <= 9:
    for i in diapazon:
        if i % k == 0:
            result.append(i)
    k += 1
    print(result)
    print(f'{len(result)} элементов кратны {k - 1}')
    result.clear()

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
# заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

a_massive = [8, 3, 15, 6, 4, 2]
result = []
ind = 0
for i in a_massive:
    if i % 2 == 0:
        result.append(ind)
    ind += 1
print(result)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# import random
#
List = [1,2,3,4,5,6,7,8,9]

random.shuffle(List)
print(List)
for i in List:

    if i == max(List):

        b = List.index(i)
        print(List.index(i))

    if i == min(List):

        a = List.index(i)
        print(List.index(i))

List[b], List[a] = List[a], List[b]

print(List)

# 4. Определить, какое число в массиве встречается чаще всего.
List = [1,2,3,4,5,6,7,8,9,1,2,2, 2]
frequency = max(map(List.count, List))
print(f'{max(a for a in List if List.count(a) == frequency)} то самое число')

print(f'{frequency} количество повторений этого числа в списке')

5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 2, -2]

min_num = min(map(int, List))

print(f'{min_num} минимальное число')

print(f'{List.index(min_num)} его индекс')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

List = [1, 2, 3, 9, 5, 6, 7, 8, 1, 2, 2, -2]

min_num = min(map(int, List))

max_num = max(map(int, List))

for i in List:
    j = List.index(max_num)
    k = List.index(min_num)
print(List[j + 1:k - 1])
print(sum(List[j + 1:k - 1]))

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

List = [1, 2, 3, 9, 5, 6, 7, 8, 2, -2]
result = []

min_num_1 = min(map(int, List))
List.remove(min_num_1)
result.append(min_num_1)
min_num_2 = min(map(int, List))
result.append(min_num_2)

print(List)
print(result)

# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
M = 4
a = []
for i in range(M):
    b = []
    s = 0
    print(f'{i + 1} строка')
    for j in range(M + 1):
        n = int(input('введите число '))
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

print(f'{a} итоговая матрица')

for i in a:
    print(i)
