#!/usr/bin/env python
# coding: utf-8

# In[309]:


import numpy as np
import pandas as pd
import random

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score as r2
from sklearn.model_selection import KFold, GridSearchCV

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[310]:


import os
for dirname, _, filenames in os.walk('../vladv/data_files/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[311]:


import warnings
warnings.filterwarnings('ignore')


# In[312]:


matplotlib.rcParams.update({'font.size': 16})


# In[313]:


train_df = pd.read_csv('Desktop/GeekBrains/train.csv')
test_df = pd.read_csv('Desktop/GeekBrains/test.csv')


# Функция оценки качества по коэффициенту детерминации.

# In[314]:


def evaluate_preds(train_true_values, train_pred_values, test_true_values, test_pred_values):
    '''
    
    '''
    print("Train R2:\t" + str(round(r2(train_true_values, train_pred_values), 3)))
    print("Test R2:\t" + str(round(r2(test_true_values, test_pred_values), 3)))
    
    plt.figure(figsize=(18,10))
    
    plt.subplot(121)
    sns.scatterplot(x=train_pred_values, y=train_true_values)
    plt.xlabel('Predicted values')
    plt.ylabel('True values')
    plt.title('Train sample prediction')
    
    plt.subplot(122)
    sns.scatterplot(x=test_pred_values, y=test_true_values)
    plt.xlabel('Predicted values')
    plt.ylabel('True values')
    plt.title('Test sample prediction')

    plt.show()


# Обзор данных

# In[315]:


train_df.head()


# In[316]:


test_df.head()


# In[317]:


train_df.shape, test_df.shape


# 
# # Приведение типов данных

# In[318]:


train_df.info()


# Приведем Id к текстовому типу данных, чтобы он не попал в выборку.

# In[319]:


train_df['Id'] = train_df['Id'].astype(str)
train_df['Id'].dtype


# In[320]:


test_df['Id'] = test_df['Id'].astype(str)
test_df['Id'].dtype


# Обзор количественных переменных

# In[321]:


df_num_features = train_df.select_dtypes(include=['float64', 'int64'])


# In[322]:


df_num_features.head()


# Обзор номинативных переменных

# In[323]:


df_object_features = train_df.select_dtypes(include=['object'])
df_object_features.head()


# In[324]:


train_df['Ecology_2'].value_counts()


# In[325]:


train_df['Ecology_3'].value_counts()


# In[326]:


train_df['Shops_2'].value_counts()


# Заменим признаки на 0 и 1 соответственно.

# In[327]:


train_df['Ecology_2_bin'] = train_df['Ecology_2'].replace({'A' : 0, 'B' : 1})
train_df['Ecology_3_bin'] = train_df['Ecology_3'].replace({'A' : 0, 'B' : 1})
train_df['Shops_2_bin'] = train_df['Shops_2'].replace({'A' : 0, 'B' : 1})


# In[328]:


test_df['Ecology_2_bin'] = test_df['Ecology_2'].replace({'A' : 0, 'B' : 1})
test_df['Ecology_3_bin'] = test_df['Ecology_3'].replace({'A' : 0, 'B' : 1})
test_df['Shops_2_bin'] = test_df['Shops_2'].replace({'A' : 0, 'B' : 1})


# In[329]:


train_df.tail()


# In[330]:


train_df.isnull().sum()


# In[331]:


train_df.loc[train_df['Healthcare_1'].isnull(), :].head()


# In[332]:


train_df.loc[train_df['Healthcare_1'].isnull(), 'Healthcare_1'] = train_df['Healthcare_1'].median()


# In[333]:


test_df.loc[test_df['Healthcare_1'].isnull(), 'Healthcare_1'] = train_df['Healthcare_1'].median()


# In[334]:


train_df.loc[train_df['LifeSquare'].isnull(), :].head()


# In[335]:


train_df.loc[train_df['LifeSquare'].isnull(), 'LifeSquare'] = train_df['Square'].median()
test_df.loc[test_df['LifeSquare'].isnull(), 'LifeSquare'] = train_df['Square'].median()


# In[336]:


train_df.head()


# 
# 
# # Обработка выбросов

# In[337]:


train_df.describe()


# Rooms

# In[338]:


train_df[(train_df['Rooms']<1) | (train_df['Rooms']>5)].head(5)


# In[339]:


train_df['Rooms'].mode()[0]


# In[340]:


train_df.loc[(train_df['Rooms'] < 1) | (train_df['Rooms'] > 5), 'Rooms'] = train_df['Rooms'].mode()[0]
test_df.loc[(test_df['Rooms'] < 1) | (test_df['Rooms'] > 5), 'Rooms'] = train_df['Rooms'].mode()[0]


# Square

# In[341]:


train_df.nlargest(5, 'Square')


# In[342]:


train_df.loc[(train_df['Square'] < 15) | (train_df['Square'] > 300), 'Square'] = train_df['Square'].median()


# Life Square

# In[343]:


train_df.nlargest(5, 'LifeSquare')


# In[344]:


train_df.loc[(train_df['LifeSquare']<15) | (train_df['LifeSquare']>250), 'LifeSquare'] = train_df['Square']


# In[345]:


test_df.loc[(test_df['LifeSquare'] < 15) | (test_df['LifeSquare'] > 250), 'LifeSquare'] = train_df['Square']


# In[346]:


train_df[(train_df['LifeSquare']>15) | (train_df['LifeSquare']<250)].head(5)


# Kitchen Square

# In[347]:


train_df.nlargest(10, 'KitchenSquare')


# In[348]:


train_df.loc[train_df['KitchenSquare'] < 4, 'KitchenSquare'] = 4


# In[349]:


test_df.loc[test_df['KitchenSquare'] < 4, 'KitchenSquare'] = 4


# Также заменим нелогичные данные мединой, где площадь кухни больше чем жилая площадь.

# In[350]:


train_df.loc[train_df['KitchenSquare'] > train_df['LifeSquare'], 'KitchenSquare'] = train_df['KitchenSquare'].median()


# In[351]:


test_df.loc[test_df['KitchenSquare'] > test_df['LifeSquare'], 'KitchenSquare'] = train_df['KitchenSquare'].median()


# HouseFloor

# In[352]:


train_df.nlargest(5, 'HouseFloor')


# In[353]:


train_df.loc[(train_df['HouseFloor'] < 2) | (train_df['HouseFloor'] > 50), 'HouseFloor'] = train_df['HouseFloor'].mode()[0]


# In[354]:


test_df.loc[(test_df['HouseFloor'] < 2) | (test_df['HouseFloor'] > 50), 'HouseFloor'] = train_df['HouseFloor'].mode()[0]


# Floor

# In[355]:


train_df[train_df['Floor']>train_df['HouseFloor']]


# In[356]:


train_df.loc[train_df['Floor']>train_df['HouseFloor'], 'Floor'] = train_df['Floor']
test_df.loc[test_df['Floor']>test_df['HouseFloor'], 'Floor'] = train_df['Floor']


# House Year

# In[357]:


train_df.nlargest(10, 'HouseYear')


# In[358]:


train_df.loc[train_df['HouseYear']>2021, 'HouseYear'] = train_df['HouseYear'].median()
test_df.loc[test_df['HouseYear']>2021, 'HouseYear'] = train_df['HouseYear'].median()


# In[359]:


train_df.describe()


# # Отбор признаков

# In[360]:


train_df.head()


# исключим Id, Ecology_2, Ecology_3, Shops_2 как неподходящие для основной выборки

# In[361]:


feature_names = ['DistrictId', 'Rooms', 'Square', 'LifeSquare', 'KitchenSquare', 'Floor', 'HouseFloor', 'HouseYear',
                 'Ecology_1', 'Ecology_2_bin', 'Ecology_3_bin', 'Social_1', 'Social_2', 'Social_3',
                 'Healthcare_1', 'Helthcare_2', 'Shops_1', 'Shops_2_bin']
target_name = 'Price'


# In[362]:


train_df[['DistrictId', 'Rooms', 'Square', 'LifeSquare', 'KitchenSquare', 'Floor', 'HouseFloor', 'HouseYear',
                 'Ecology_1','Social_1', 'Social_2', 'Social_3',
                 'Healthcare_1', 'Helthcare_2', 'Shops_1']].hist(figsize=(16,16), bins=25, grid=True)


# In[363]:


sns.pairplot(train_df[['DistrictId', 'Rooms', 'Square', 'Floor', 'HouseYear', 'Ecology_1', 'Social_1', 'Healthcare_1', 'Helthcare_2', 'Shops_1', 'Price']])


# In[364]:


plt.figure(figsize=(20,15))

sns.set(font_scale=1.4)
sns.heatmap(train_df[feature_names + ['Price']].corr(), annot=True, linewidths=.5, cmap='GnBu')

plt.title('Матрица корреляции')
plt.show()


# уберем признак Social_2, т.к. он сильно кореллирует с Social_1

# In[365]:


feature_names = ['DistrictId', 'Rooms', 'Square', 'LifeSquare', 'KitchenSquare', 'Floor', 'HouseFloor', 'HouseYear',
                 'Ecology_1', 'Ecology_2_bin', 'Ecology_3_bin', 'Social_1', 'Social_3',
                 'Healthcare_1', 'Helthcare_2', 'Shops_1', 'Shops_2_bin']
target_name = 'Price'


# In[366]:


train_df = train_df[feature_names + [target_name]]
test_df = test_df[feature_names]
train_df.head()


# # Анализ целевой переменной

# In[367]:


target_mean = round(train_df[target_name].mean(), 2)
target_mean


# In[368]:


target_median = round(train_df[target_name].median(), 2)
target_median 


# In[369]:


target_mode = round(train_df[target_name].mode()[0], 2)
target_mode


# In[370]:


plt.figure(figsize = (16, 8))

sns.distplot(train_df[target_name])

y = np.linspace(0, 0.000005, 10)
plt.plot([target_mean]*10, y, label='mean', linestyle=':', linewidth=4)
plt.plot([target_median]*10, y, label='median', linestyle='--', linewidth=4)
plt.plot([target_mode]*10, y, label='mode', linestyle='-', linewidth=4)

plt.title('Распределение цены')
plt.legend()
plt.show()


# # Оценка распределения цены в разрезе других признаков

# Общая площадь жилья

# In[371]:


grid = sns.jointplot(train_df[target_name], train_df['Square'], kind='reg')
grid.fig.set_figwidth(12)
grid.fig.set_figheight(12)

plt.show()


# Район

# In[372]:


grid = sns.jointplot(train_df[target_name], train_df['DistrictId'], kind='reg')
grid.fig.set_figwidth(12)
grid.fig.set_figheight(12)

plt.show()


# # Стандартизация признаков

# In[373]:


feature_names_for_stand = ['DistrictId', 'Rooms', 'Square', 'LifeSquare', 'KitchenSquare', 'Floor', 'HouseFloor', 'HouseYear',
                 'Ecology_1', 'Social_1', 'Social_3',
                 'Healthcare_1', 'Helthcare_2', 'Shops_1']


# In[374]:


scaler = StandardScaler()
stand_features = scaler.fit_transform(train_df[feature_names_for_stand])
stand_features_test = scaler.transform(test_df[feature_names_for_stand])


# In[375]:


train_df[feature_names_for_stand] = pd.DataFrame(stand_features, columns=feature_names_for_stand)
test_df[feature_names_for_stand] = pd.DataFrame(stand_features_test, columns=feature_names_for_stand)


# In[376]:


train_df.head()


# In[377]:


train_df.std()


# # Построение базовых моделей

# In[378]:


X = train_df[feature_names]
y = train_df[target_name]


# In[379]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, shuffle = True, random_state = 42)


# # Gradient Boosting

# In[380]:


gb_model = GradientBoostingRegressor()
gb_model.fit(X_train, y_train)


# In[381]:


y_train_preds = gb_model.predict(X_train)
y_test_preds = gb_model.predict(X_test)


# In[382]:


evaluate_preds(y_train, y_train_preds, y_test, y_test_preds)


# # Подбор гиперпараметров

# In[383]:


gb_model = GradientBoostingRegressor(random_state=42)
gb_model


# In[384]:


params = {'n_estimators': [50, 100, 200, 400],
         'max_depth': [3, 5 , 7 ,10]}


# In[385]:


gs = GridSearchCV(gb_model, params, scoring='r2', cv=KFold(n_splits=3, random_state=42, shuffle=True), n_jobs=-1)


# In[386]:


gs.fit(X,y)


# In[387]:


gs.best_params_


# In[388]:


gs.best_score_


# # Итоговая модель

# Применим оптимальные параметры, которые мы получили выше

# In[389]:


final_model = GradientBoostingRegressor(random_state=42, n_estimators=200, max_depth=5)
final_model.fit(X_train, y_train)


# In[390]:


y_train_preds = final_model.predict(X_train)
y_test_preds = final_model.predict(X_test)


# In[391]:


evaluate_preds(y_train, y_train_preds, y_test, y_test_preds)


# # Важность признаков

# In[392]:


feature_importances = pd.DataFrame({'feature': X_train.columns, 'importance': final_model.feature_importances_})
feature_importances = feature_importances.sort_values(by='importance', ascending=True)
feature_importances.reset_index(drop=True).plot(kind='bar')
plt.xticks(ticks=range(feature_importances.shape[0]), labels=feature_importances.feature,size=14)
plt.show()


# Удалим очевидно малозначимые признаки "Ecology_3_bin, Shops_2_bin, Ecology_2_bin" и др.

# In[393]:


feature_names = ['DistrictId', 'Rooms', 'Square', 'KitchenSquare', 'Floor', 'HouseYear',
                 'Ecology_1', 'Social_1', 'Social_3',
                 'Healthcare_1', 'Helthcare_2', 'Shops_1']


# In[394]:


X = train_df[feature_names]
y = train_df[target_name]


# In[395]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=True, random_state=42)


# In[396]:


final_model = GradientBoostingRegressor(random_state=42, n_estimators=200, max_depth=5)


# In[397]:


final_model.fit(X_train, y_train)


# In[398]:


y_train_preds = final_model.predict(X_train)
y_test_preds = final_model.predict(X_test)


# In[399]:


evaluate_preds(y_train, y_train_preds, y_test, y_test_preds)


# # Применение модели на тестовом датасете

# In[400]:


y_test_preds = final_model.predict(test_df[feature_names])


# In[401]:


test_df = pd.read_csv('Desktop/GeekBrains/test.csv')


# In[402]:


result = pd.DataFrame()


# In[403]:


result['Id'] = test_df['Id'].copy()


# In[404]:


result['Price'] = pd.Series(y_test_preds)


# In[405]:


result.to_csv('VladVologodskiy_predictions_GU_BigData.csv', index=False)


# In[406]:


result.values


# In[407]:


result.shape


# In[408]:



result['Price'].describe()


# In[409]:


result.tail(10)


# In[ ]:




