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
