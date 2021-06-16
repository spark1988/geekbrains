# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import timeit
import random
import cProfile


def test_func():
    # a_massive = [8, 3, 15, 6, 4, 2, 8, 9, 11, 13, 15, 16] #первый результат timeit через цикл for. В результате этот вариант является оптимальным решением
# третий результат с циклом while и статичным списком

    a_massive = [random.randint(1, 100) for _ in range(12)]
    #второй результат 6.5535946 timeit через цикл for
    #четвертый результат 6.829843899999999 с генерируемым списком и циклом while
    result = []
    ind = 0
#

    # i, count = 0, len(a_massive)
    # while i < count:
    #     if a_massive[i] % 2 == 0:
    #         result.append([i])
    #     i += 1

    for i in a_massive:
        if i % 2 == 0:
            result.append(ind)
        ind += 1
    return result
# print(test_func())
# print(timeit.timeit(test_func))



cProfile.run('test_func()')

# 1. Вариант делаем замер с готовым массивом через цикл for
# Результат:
# [0, 3, 4, 5, 6, 11]
# 1.4600221 Время
#          10 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:14(test_func)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 2. Вариант делаем замер с готовым массивом через цикл while
# [[0], [3], [4], [5], [6], [11]]
# 2.0677806000000003 Время выполнения больше на пол секунды +
#          11 function calls in 0.000 seconds Функция вызвана на 1 раз больше
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:14(test_func)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 3. Вызываем генерируемый список случайных чисел через цикл while на 12 значений. Результат:
# [[0], [6], [7], [8], [9], [10], [11]]
# 13.230506499999999 - значительно дольше чем готовые списки, это очень долго
#          75 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:14(test_func)
#         1    0.000    0.000    0.000    0.000 main.py:18(<listcomp>)
#        12    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
#        12    0.000    0.000    0.000    0.000 random.py:291(randrange)
#        12    0.000    0.000    0.000    0.000 random.py:335(randint)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        12    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        16    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 4. Вызываем генерируемый список случайных чисел через цикл for на 12 значений. Результат:
# [0, 3, 6, 7, 9, 11]
# 12.5619337 - быстрей чем цикл while
#          74 function calls in 0.000 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:14(test_func)
#         1    0.000    0.000    0.000    0.000 main.py:18(<listcomp>)
#        12    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
#        12    0.000    0.000    0.000    0.000 random.py:291(randrange)
#        12    0.000    0.000    0.000    0.000 random.py:335(randint)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        12    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        17    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Результат: 
# 
# В итоге самым быстрым вариантом исполнения кода будет уже готовый список значений, с перебором через
# цикл for
# На втором месте также готовый список через цикл while 
# и затем аналигично генерируемые списки случайных чисел , но они очень долго исполняются по времени 12 сек + 

