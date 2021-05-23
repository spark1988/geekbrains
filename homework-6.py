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
        return f'{self.name} машинка тронулась эрон-дон-дон'

    def stop(self):
        return f'{self.name} стоп мотор, машина остановилась'

    def turn(self, side):
        self.side = side
        if side == 'left':
            return f'{self.name} машина повернула налево'
        if side == 'right':
            return f'{self.name} машина повернула направо'
    def show_speed(self):
        if self.speed > 60 and self.is_police != True:
            return f'Вы превышаете скорость {self.speed} км/ч'
        else:
            return f'{self.speed} км/час это норма'

class Towncar(Car):

    def show_speed(self):
        if self.speed > 60:
            return (f'превышение {self.name} на {self.speed - 60}')
        else:
            return (f'Скорость {self.speed} допустимая для {self.name}')

class Workcar(Car):
    def show_speed(self):
        if self.speed > 40:
            return (f'превышение {self.name} на {self.speed - 40}')
        else:
            return (f'Скорость {self.speed} допустимая для {self.name}')

class SportCar(Car):

    def tubroboost(self):
            return f'{self.speed * 2}  км/час'

class PoliceCar(Car):
        def sirens(self):
                if self.is_police == True:
                    print ('Это полиция')
                    time.sleep(1)
                    print ('мигалка синяя')
                    time.sleep(1)
                    print ('мигалка красная')
                    time.sleep(1)
                    return ('остановите машину!')


        def arrest(self):

            if worker_car.speed > 40:
                return (f'Вы арестованы {worker_car.name} т.к скорость = {worker_car.speed} км/час')
            if city_rider.speed > 60:
                return (f'Вы довыделывались {city_rider.name} т.к ваша скорость = {city_rider.speed} км и арестованы')

        def docs(self):
            q = input('могу я увидеть ваши документы?! да/да ')
            if q == 'да':
                return ('спасибо, с документами все в порядке')
            else:
                return ('мы вынуждены вас задержать')


police_car = PoliceCar(190, 'black', 'Lamborgini', True)
print(police_car.go())
city_rider = Towncar(140,'blue','Infinity QX56', False)
worker_car = Workcar(80, 'yellow', 'Volvo Truck', False)
super_car = SportCar(200, 'red', 'Ferrari', False)
print(super_car.speed)
print(super_car.show_speed())
print(super_car.tubroboost())
print(police_car.sirens())
print(police_car.docs())
# worker_car.speed = 40
print(worker_car.speed)
print(police_car.arrest())

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        return (f'Запуск отрисовки выбери {self.title}')
class Pen(Stationery):
    def draw(self):
        return (f'Это {self.title} аккуратней, а то запачкаешься, особенно если я гелевая')

class Pencil(Stationery):
    def draw(self):

        return (f'Это {self.title} хоть сейчас рисуй шарж')

class Handle(Stationery):
    def draw(self):
        return (f'Это {self.title} отлично подойдет для планерок')

predmet_risovaniya = Stationery('инструмент для рисования')
sharzhist = Pencil('Карандаш')
planerovshik = Handle('Маркер')
student = Pen('Ручка')
print(predmet_risovaniya.draw())
print(sharzhist.draw())
print(planerovshik.draw())
print(student.draw())
