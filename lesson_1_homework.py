#!/usr/bin/env python
# coding: utf-8

# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# 
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. 
# 
# Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. 
# 
# Будем считать, что каждый столбец - это признак, а строка - наблюдение. 
# 
# Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. 
# 
# Результат запишите в массив mean_a, в нем должно быть 2 элемента.
# 

# # Задание 1

# In[11]:


import numpy as np


# In[21]:


a = np.array([
[1, 6],
[2, 8],
[3, 11],
[3, 10],
[1, 7],
])
a


# In[22]:


mean_a = a.mean(axis=0)
mean_a


# # Задание 2

# Вычислите массив a_centered, отняв от значений массива “а” средние значения 
# соответствующих признаков, содержащиеся в массиве mean_a. 
# Вычисление должно производиться в одно действие. 
# Получившийся массив должен иметь размер 5x2.

# In[23]:


a_centered = a - mean_a.reshape(1,2)
a_centered


# # Задание 3

# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.
# *!!столбец - это признак, а строка - наблюдение!!*
# 

# In[24]:


a1 = a_centered[:, 0]
a1


# In[25]:


a2 = a_centered[:, 1]
a2


# In[26]:


a_centered_sp = a1@a2
a_centered_sp


# In[27]:


N = a.shape[0]
N


# In[28]:


total = a_centered_sp / (N - 1)
total


# In[29]:


c = np.cov(a.transpose())
c


# In[30]:


cavariation = c[1, 0]
cavariation


# # Работа с данными в Pandas
# 

# # Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# 

# In[31]:


import pandas as pd 


# In[32]:


a = {
    "author_id": [1, 2, 3],
    "author_name": ["Тургенев'", "Чехов", "Островский"]
}
authors = pd.DataFrame(a)
authors


# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[33]:


c = {
    "author_id" : [1, 1, 1, 2, 2, 3, 3],
    "book_title" : ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price" : [450, 300, 350, 500, 450, 370, 290]
}
books = pd.DataFrame(c)
books


# # Задание 2

# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# 

# In[34]:


authors_price = pd.merge(authors, books, on='author_id', how='inner')
authors_price


# 
# 
# # Задание 3
# 

# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
# 

# In[35]:


top5 = authors_price.nlargest(5, 'price')
top5


# # Задание 4
# 

# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[36]:


df1 = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns={'price':'min_price'})
df2 = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns={'price':'max_price'}) 
df3 = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns={'price':'mean_price'})
df1, df2, df3 


# In[37]:


authors_stat = pd.concat([df1, df2, df3], axis = 1)
authors_stat


# # Задание 5**
# Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
# ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
# Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
# Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.
# 

# In[38]:


df1 = pd.DataFrame({'cover':['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']})
authors_price = pd.concat([authors_price, df1], axis = 1)

authors_price


# In[39]:


get_ipython().run_line_magic('pinfo', 'pd.pivot_table')


# In[40]:


book_info = pd.pivot_table(authors_price, values='price', index=['author_name'],
                    columns=['cover'], aggfunc=np.sum, fill_value=0)
book_info


# In[41]:


book_info.to_pickle('book_info.pkl')


# In[42]:


book_info2 = pd.read_pickle('book_info.pkl')


# In[43]:


book_info==book_info2

