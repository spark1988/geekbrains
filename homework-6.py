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

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return  'Full name is '+ self.name + ' ' + self.surname

    def get_total_income(self):
        income = self._income.values()
        return sum(income)

Jober = Position('Vladimir', 'Putin', 'The President', 190000, 40000)

print(Jober.name)
print(Jober.position)
print(Jober.get_full_name())
print(Jober.get_total_income())

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f' {self.name} машинка тронулась эрон-дон-дон'

    def stop(self):
        return f' {self.name} стоп мотор, машина остановилась'

    def turn(self, side):
        self.side = side
        if side == 'left':
            return f' {self.name} машина повернула налево'
        if side == 'right':
            return f' {self.name} машина повернула направо'
    def show_speed(self):
        if self.speed > 60 and self.is_police != True:
            return 'Вы превышаете скорость'
        else:
            return self.speed

class Towncar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'превышение {self.name} на {self.speed - 60}')
        else:
            print(f'Скорость {self.speed} допустимая для {self.name}')

class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'превышение {self.name} на {self.speed - 40}')
        else:
            print(f'Скорость {self.speed} допустимая для {self.name}')

class PoliceCar(Car):
        def sirens(self):
                if self.is_police == True:
                    print('Это полиция')
                    time.sleep(1)
                    print('мигалка синяя')
                    time.sleep(1)
                    print('мигалка красная')
                    time.sleep(1)
                    print('остановите машину!')
        def docs(self):
                return 'ваши документики'
        def arrest(self):

            if worker_car.speed > 40:
                print(f'Вы арестованы {worker_car.name} = {worker_car.speed}')
            if city_rider.speed > 60:
                print(f'Вы довыделывались {city_rider.name} = {city_rider.speed}')



police_car = PoliceCar(190, 'black', 'Lamborgini', True)
city_rider = Towncar(120,'blue','Infinity QX65', False)
worker_car = Workcar(60, 'yellow', 'Volvo Truck', False)
worker_car.speed = 40
print(worker_car.speed)
print(police_car.arrest())

