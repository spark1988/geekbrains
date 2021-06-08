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










