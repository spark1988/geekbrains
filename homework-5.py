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
