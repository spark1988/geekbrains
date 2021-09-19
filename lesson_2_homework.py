#!/usr/bin/env python
# coding: utf-8

# 
# # Тема “Визуализация данных в Matplotlib”
# 

# Задание 1
# Загрузите модуль pyplot библиотеки matplotlib с псевдонимом plt, а также библиотеку numpy с псевдонимом np.
# Примените магическую функцию %matplotlib inline для отображения графиков в Jupyter Notebook и настройки конфигурации ноутбука со значением 'svg' для более четкого отображения графиков.
# Создайте список под названием x с числами 1, 2, 3, 4, 5, 6, 7 и список y с числами 3.5, 3.8, 4.2, 4.5, 5, 5.5, 7.
# С помощью функции plot постройте график, соединяющий линиями точки с горизонтальными координатами из списка x и вертикальными - из списка y.
# Затем в следующей ячейке постройте диаграмму рассеяния (другие названия - диаграмма разброса, scatter plot).
# 

# In[1]:


from matplotlib import pyplot as plt


# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


import matplotlib.style as style
style.available


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


# In[7]:


x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([3.5, 3.8, 4.2, 4.5, 5, 5.5, 7])
x, y


# In[8]:


plt.plot(x, y)


# In[9]:


plt.scatter(x, y)


# # Задание 2
# 

# С помощью функции linspace из библиотеки Numpy создайте массив t из 51 числа от 0 до 10 включительно.
# 
# Создайте массив Numpy под названием f, содержащий косинусы элементов массива t.
# 
# Постройте линейную диаграмму, используя массив t для координат по горизонтали,а массив f - для координат по вертикали. Линия графика должна быть зеленого цвета.
# 
# Выведите название диаграммы - 'График f(t)'. Также добавьте названия для горизонтальной оси - 'Значения t' и для вертикальной - 'Значения f'.
# 
# Ограничьте график по оси x значениями 0.5 и 9.5, а по оси y - значениями -2.5 и 2.5.
# 

# In[10]:


t = np.linspace(0, 10, 51)
t


# In[11]:


f = np.cos(t)
f


# In[12]:


plt.plot(t,f, color = "green")
plt.title("График f(t)")
plt.xlabel("Значения t")
plt.ylabel("Значения f")
plt.axis([0.5, 9.5, -2.5, 2.5])


# # *Задание 3
# С помощью функции linspace библиотеки Numpy создайте массив x из 51 числа от -3 до 3 включительно.
# Создайте массивы y1, y2, y3, y4 по следующим формулам:
# y1 = x**2
# y2 = 2 * x + 0.5
# y3 = -3 * x - 1.5
# y4 = sin(x)
# 
# Используя функцию subplots модуля matplotlib.pyplot, создайте объект matplotlib.figure.Figure с названием fig и массив объектов Axes под названием ax,причем так, чтобы у вас было 4 отдельных графика в сетке, состоящей из двух строк и двух столбцов. 
# 
# В каждом графике массив x используется для координат по горизонтали.В левом верхнем графике для координат по вертикали используйте y1,в правом верхнем - y2, в левом нижнем - y3, в правом нижнем - y4.Дайте название графикам: 'График y1', 'График y2' и т.д.
# 
# Для графика в левом верхнем углу установите границы по оси x от -5 до 5.
# Установите размеры фигуры 8 дюймов по горизонтали и 6 дюймов по вертикали.
# Вертикальные и горизонтальные зазоры между графиками должны составлять 0.3.
# 

# In[13]:


x = np.linspace(-3, 3, 51)
x


# In[14]:


y1 = x**2
y2 = 2 * x + 0.5
y3 = -3 * x - 1.5
y4 = np.sin(x)


# In[15]:


y1, y2, y3, y4


# Используя функцию subplots модуля matplotlib.pyplot, создайте объект matplotlib.figure.Figure с названием fig и массив объектов Axes под названием ax,причем так, чтобы у вас было 4 отдельных графика в сетке, состоящей из двух строк и двух столбцов.

# In[16]:


fig, ax = plt.subplots(nrows=2, ncols=2)
ax1, ax2, ax3, ax4 = ax.flatten()
fig.subplots_adjust(wspace=0.3, hspace=0.3)
fig.set_size_inches(8, 6)    

ax1.plot(x, y1)
ax1.set_xlim(-5, 5)
ax1.set_title("График y1")

ax2.plot(x, y2)
ax2.set_title("График y2")

ax3.plot(x, y3)
ax3.set_title("График y3")

ax4.plot(x, y4)
ax4.set_title("График y4")


# В каждом графике массив x используется для координат по горизонтали.В левом верхнем графике для координат по вертикали используйте y1,в правом верхнем - y2, в левом нижнем - y3, в правом нижнем - y4.
# Дайте название графикам: 'График y1', 'График y2' и т.д.

# Для графика в левом верхнем углу установите границы по оси x от -5 до 5. Установите размеры фигуры 8 дюймов по горизонтали и 6 дюймов по вертикали. Вертикальные и горизонтальные зазоры между графиками должны составлять 0.3.

# # *Задание 4
# В этом задании мы будем работать с датасетом, в котором приведены данные по мошенничеству с кредитными данными: Credit Card Fraud Detection (информация об авторах: Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson and Gianluca Bontempi. Calibrating Probability with Undersampling for Unbalanced Classification. In Symposium on Computational Intelligence and Data Mining (CIDM), IEEE, 2015).
# 
# Ознакомьтесь с описанием и скачайте датасет creditcard.csv с сайта Kaggle.com по ссылке:
# Credit Card Fraud Detection
# 
# Данный датасет является примером несбалансированных данных, так как мошеннические операции с картами встречаются реже обычных.
# Импортируйте библиотеку Pandas, а также используйте для графиков стиль “fivethirtyeight”.
# Посчитайте с помощью метода value_counts количество наблюдений для каждого значения целевой переменной Class и примените к полученным данным метод plot, чтобы построить столбчатую диаграмму. Затем постройте такую же диаграмму, используя логарифмический масштаб.
# 
# На следующем графике постройте две гистограммы по значениям признака V1 - одну для мошеннических транзакций (Class равен 1) и другую - для обычных (Class равен 0). Подберите значение аргумента density так, чтобы по вертикали графика было расположено не число наблюдений, а плотность распределения. Число бинов должно равняться 20 для обеих гистограмм, а коэффициент alpha сделайте равным 0.5, чтобы гистограммы были полупрозрачными и не загораживали друг друга. Создайте легенду с двумя значениями: “Class 0” и “Class 1”. Гистограмма обычных транзакций должна быть серого цвета, а мошеннических - красного. Горизонтальной оси дайте название “V1”.
# 

# In[17]:


DATASET_PATH = 'E:/Education/GeekBrains/python_data/les_2/creditcard.csv'


# In[18]:


style.use('fivethirtyeight')


# In[19]:


df = pd.read_csv(DATASET_PATH, sep=',')
df.head(10)


# In[20]:


df.shape


# In[21]:


t=df['Class'].value_counts()
t


# In[22]:


df_class_info = t
df_class_info.plot(kind='bar')
plt.show()


# In[23]:


df_class_info.plot(kind='bar', logy=True)
plt.show()


# In[24]:


#На следующем графике постройте две гистограммы по значениям признака V1 — одну для 
#мошеннических транзакций (Class равен 1) и другую — для обычных (Class равен 0). 
#Подберите значение аргумента density так, чтобы по вертикали графика было расположено 
#не число наблюдений, а плотность распределения. Число бинов должно равняться 20 для 
#обеих гистограмм, а коэффициент alpha сделайте равным 0.5, чтобы гистограммы были 
#полупрозрачными и не загораживали друг друга. 
v1_1=df.set_index('Class')['V1'].filter(like='1', axis=0)
v1_1=v1_1.reset_index()
v1_1=v1_1.drop('Class', axis=1)
v1_1.head(5)


# In[25]:


v1_1.count()


# In[26]:


v1_0=df.set_index('Class')['V1'].filter(like='0', axis=0)
v1_0=v1_0.reset_index()
v1_0=v1_0.drop('Class', axis=1)
v1_0.head()


# In[27]:


v1_0.count()


# In[28]:


#Создайте легенду с двумя значениями: Class 0 и Class 1. Гистограмма обычных транзакций 
#должна быть серого цвета, а мошеннических — красного. Горизонтальной оси дайте название Class.
plt.hist(v1_0['V1'], bins=20, color='grey', edgecolor='black', density = True, orientation = 'horizontal',alpha=0.5)
plt.hist(v1_1['V1'], bins=20, color='red', edgecolor='black', density = True, orientation = 'horizontal',alpha=0.5)
plt.plot()
plt.xlabel('Class')
plt.legend(labels=['Class 0', 'Class 1'])


# # Задание на повторение материала
# 
# 

# 1. Создать одномерный массив Numpy под названием a из 12 последовательных целых чисел чисел от 12 до 24 невключительно
# 

# In[29]:


a = np.arange(12,24,1)
a


# 2. Создать 5 двумерных массивов разной формы из массива a. Не использовать в аргументах метода reshape число -1.
# 

# In[30]:


a1 = a.reshape(4,3)
a2 = a.reshape(6,2)
a3 = a.reshape(2,6)
a4 = a.reshape(3,4)
a1, a2, a3, a4


# 3. Создать 5 двумерных массивов разной формы из массива a. Использовать в аргументах метода reshape число -1 (в трех примерах - для обозначения числа столбцов, в двух - для строк).
# 

# In[31]:


a5 = a.reshape(-1, 6)
a6 = a.reshape(-1, 4)
a7 = a.reshape(3, -1)
a8 = a.reshape(4, -1)
a9 = a.reshape(6, -1)
a5, a6, a7, a8, a9


# In[32]:


a10 = a.reshape(12,1)
a10


# 4. Можно ли массив Numpy, состоящий из одного столбца и 12 строк, назвать одномерным?
# Ответ: Нельзя)

# 5. Создать массив из 3 строк и 4 столбцов, состоящий из случайных чисел с плавающей запятой из нормального распределения со средним, равным 0 и среднеквадратичным отклонением, равным 1.0. Получить из этого массива одномерный массив с таким же атрибутом size, как и исходный массив.
# 

# In[33]:


ax = np.random.randn(3, 4)
ax


# In[34]:


ax.size


# In[35]:


ax2 = ax.flatten()
ax2


# In[36]:


ax.size == ax2.size


# 6. Создать массив a, состоящий из целых чисел, убывающих от 20 до 0 невключительно с интервалом 2.
# 

# In[38]:


a = np.arange(20, 0, -2)
a


# 7. Создать массив b, состоящий из 1 строки и 10 столбцов: целых чисел, убывающих от 20 до 1 невключительно с интервалом 2. В чем разница между массивами a и b?
# 

# In[45]:


b = np.arange(20, 0, -2).reshape(1, 10)
b


# В чем разница между массивами a и b?
# a является одномерным, а b двумерным.

# 8. Вертикально соединить массивы a и b. a - двумерный массив из нулей, число строк которого больше 1 и на 1 меньше, чем число строк двумерного массива b, состоящего из единиц. Итоговый массив v должен иметь атрибут size, равный 10.
# 

# In[66]:


a = np.zeros((2,2))
a


# In[63]:


b = np.ones((3,2))
b


# In[67]:


c = np.vstack((a, b))
c


# In[68]:


c.size


# 9. Создать одномерный массив а, состоящий из последовательности целых чисел от 0 до 12. 
# Поменять форму этого массива, чтобы получилась матрица A (двумерный массив Numpy), состоящая из 4 строк и 3 столбцов. 
# Получить матрицу At путем транспонирования матрицы A. 
# Получить матрицу B, умножив матрицу A на матрицу At с помощью матричного умножения. Какой размер имеет матрица B? 
# Получится ли вычислить обратную матрицу для матрицы B и почему?

# In[81]:


A = np.arange(0, 12).reshape(4,3)
A


# In[83]:


At = A.transpose()
At


# In[86]:


B = np.dot(A, At)
B


# In[90]:


B.shape, B.size


# In[91]:


B_inv=np.linalg.inv(B)
B_inv


# 10. Инициализируйте генератор случайных числе с помощью объекта seed, равного 42.
# 

# In[97]:


np.random.seed(42)


# 11. Создайте одномерный массив c, составленный из последовательности 16-ти 
# случайных равномерно распределенных целых чисел от 0 до 16 невключительно. 
# 

# In[101]:


c = np.random.randint(0, 16, 16)
c


# 12. Поменяйте его форму так, чтобы получилась квадратная матрица C. 
# Получите матрицу D, поэлементно прибавив матрицу B из предыдущего вопроса к матрице C, умноженной на 10. 
# Вычислите определитель, ранг и обратную матрицу D_inv для D.
# 

# In[105]:


C = c.reshape(4,4)
C


# In[108]:


D = B + C * 10
D


# In[109]:


d=np.linalg.det(D)
d


# In[111]:


r=np.linalg.matrix_rank(D)
r


# In[ ]:




