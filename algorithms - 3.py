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
import random

List = [1,2,3,4,5,6,7,8,9]

random.shuffle(List)

ind = 0
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










