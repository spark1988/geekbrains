# 1. Написать программу, которая будет складывать, вычитать, умножать или
# делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак
# операции. Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.

while True:
    try:
        num1 = int(input('введите первое число'))
        num2 = int(input('введите второе число'))
        what_to_do = input("введите что делаем числами '*','+', '-', '/' '0 - если хотите завершить программу' ")

        if what_to_do == '+':
            print(num1 + num2)
        elif what_to_do == '-':
            print(num1 - num2)
        elif what_to_do == '*':
            print(num1 * num2)
        elif what_to_do == '/':
            print(num1 / num2)
        elif what_to_do == '0':
            print('до свидания!')
            break
    except ZeroDivisionError:
        print('на ноль нельзя делить')

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input('введите число чтобы узнать в нем четные и нечетные числа')
result = list(map(int, number))
b = 0
c = 0

for i in result:
    if i % 2 == 0:
        b += 1
        print( i , 'четная' + '\n')

    if i % 2 !=0:
        c += 1
        print(i, 'нечетная цифра' + '\n')

print(b, 'итого четных цифр')
print(c, 'итого нечетных цифр')

# 3. Сформировать из введенного числа обратное по порядку входящих
# в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = input('введите число, чтобы получить число наоборот ')

rev_number = list(map(str, number))

rev_number.reverse()

print(''.join(rev_number))

# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
ask = int(input('введите кол-во элементов для ряда 1, -0.5, 0.25, -0.125,…'))
s = 0
num = 1
while s < ask:
    print(num)
    num /= -2
    s += 1
