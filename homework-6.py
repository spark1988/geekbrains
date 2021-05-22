# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

class TrafficLight():
    emp_count = 0
    def __init__(self, color):
        self.color = color
        TrafficLight.emp_count += 1

    def running(self):
        if self.color == 'Красный':
            time.sleep(7)
            return print('Красный цвет! Стоять')
        if self.color == 'Желтый':
            time.sleep(2)
            return print('Желтый цвет. Подожди')
        if self.color == 'Зеленый':
            time.sleep(5)
            return print('Зеленый цвет. Иди')
        else:
            time.sleep(2)
            print('Красный цвет! Стоять')
            time.sleep(2)
            print('Желтый цвет. Подожди')
            time.sleep(2)
            print('Зеленый цвет. Иди')

svetofor = TrafficLight('')
print(svetofor.running())

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def massa_asphalt(self, massa, tolshina):
        self.massa = massa
        self.tolshina = tolshina
        result = self.__width * self.__length * self.massa * self.tolshina
        return int(result / 1000)

R = Road(70, 7000)

print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна  \n = {R.massa_asphalt(25, 5)}')

