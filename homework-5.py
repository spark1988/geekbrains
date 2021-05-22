# # 1. Создать программно файл в текстовом формате, записать
# # в него построчно данные, вводимые пользователем.
# # Об окончании ввода данных свидетельствует пустая строка.
#
with open('test.txt', 'w') as my_f:
    line = input('Введите текст')
    while line:
        my_f.write(line + '\n')
        line = input('Введите текст')
        if not line:
            break

with open('test.txt', 'r') as my_f:
    content = my_f.readlines()
    print(content)

#2.  Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open("dz2.txt", "r") as home:
    lines = 0
    words = 0
    letters = 0
    for line in home:
        lines += 1
        letters += len(line)
        pos = 'out'
        for letter in line:
            if letter != ' ' and pos == 'out':
                words += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'
print("Количество строк:", lines)
print("Количество слов:", words)
print("Количество символов:", letters)

# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Данные в файле:
# Antony 6000
# Patrick 10000
# John 20000
# Mike 30000
# Eva 50000
# Travis 70000
with open('staff.txt', 'r') as calculation:
    listing = []
    result = []
    for word in calculation:
        listing.append(word.split())
        print(word.split(' '))
    q = input('Хотите узнать кто получает меньше 20 тысяч?!')
    for num in listing:
        result.append(int(num[1]))
        if int(num[1]) < 20000:
            print(f'{num[0]} к сожалению пока что получают меньше 20k, а именно {num[1]}')
    q = input('Хотите узнать среднюю зарплату?!')
    print(f'{int(sum(result)/len(result))} = средняя зп по организации')
    
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One 1
# Two 2
# Three 3
# Four 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
with open('task4.txt', 'r') as initial:
    new_file = []
    for i in initial:
        new_file.append(i.split())
        # print(i)

dictionary = dict(new_file)

dictionary.clear()

# for keys, values in dictionary.items():
#             print(keys, values)

updates = {'Один': '1', 'Два': '2', 'Три': '3', 'Четыре': '4'}

dictionary.update(updates)

with open('task4updates.txt', 'w', encoding='utf-8') as newdata:
    for keys, values in dictionary.items():
        newdata.write(keys + ' ')
        newdata.write(values + '\n')
        
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических
# и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла (именно в таком виде!***):
# Информатика: 100 (л) 50 (пр) 20 (лаб).
# Физика: 30 (л) — 10 (лаб)
# Физкультура: — 30 (пр)
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

table = {}
with open('plan-obucheniya.txt', 'r', encoding='utf-8') as plan:


    for i in plan.readlines():
        b = [int(s) for s in i.split() if s.isdigit()]
        key, val = i.strip().split(':')
        table[key] = sum(b)
    with open('plan-obucheniya.txt', 'w', encoding='utf-8') as plan:
        for key, val in table.items():
            plan.write('{}:{}\n'.format(key, val))
# 7. Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json
import statistics

with open('firms.txt', 'r+', encoding='utf-8') as firm:
    table = {}
    losers = {}
    average = {}
    numbers = []
    for i in firm.readlines():
            b = [int(s) for s in i.split() if s.isdigit()]
            viruchka = b[0] - b[1]
            table[i] = viruchka
            if viruchka > 0:
                numbers.append(viruchka)
            if viruchka < 0:
                losers[i] = viruchka
    average['Средняя выручка'] = statistics.mean(numbers)

    out_file = open('json_out', 'w+')
    json.dump(table, out_file)
    json.dump(losers, out_file)
    json.dump(average, out_file)
