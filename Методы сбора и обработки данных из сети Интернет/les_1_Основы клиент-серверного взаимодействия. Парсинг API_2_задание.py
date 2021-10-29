from tapi_yandex_metrika import YandexMetrikaStats
import json
import pandas as pd

ACCESS_TOKEN = "AQAAAAAH6ChQAAd3FcOAC2rGgEO_j2w7kMxSF30"
METRIC_IDS = "68144668"

# По умолчанию возвращаются только 10000 строк отчета, 
# если не указать другое кол-во в параметре limit.
# В отчете может быть больше строк, чем указано в limit 
# Тогда необходимо сделать несколько запросов для получения всего отчета.
# Чтоб сделать это автоматически вы можете указать 
# параметр receive_all_data=True при инициализации класса.

#Параметры запроса для библиотеки tapi_yandex_metrika
api = YandexMetrikaStats(
    access_token=ACCESS_TOKEN, 
    # Если True, будет скачивать все части отчета. По умолчанию False.
    receive_all_data=True
)

#Параметры запроса для библиотеки tapi_yandex_metrika
params = dict(
    ids = METRIC_IDS,
    metrics = "ym:s:users,ym:s:visits,ym:s:pageviews,ym:s:bounceRate,ym:s:pageDepth,ym:s:avgVisitDurationSeconds",
    dimensions = "ym:s:date,ym:s:<attribution>TrafficSource,ym:s:<attribution>SourceEngine,ym:s:gender",
    date1 = "10daysAgo",
    date2 = "yesterday",
    sort = "ym:s:date",
    accuracy="full",
    limit = 200
)
#Получаем данные из Yandex.Metrika API
result = api.stats().get(params=params)
result = result().data
result = result[0]['data']

#Создаем пустой dict (словать данных)
dict_data = {}

#Парсим исходный list формата Json в dictionary (словарь данных)
for i in range(0, len(result)-1):
    dict_data[i] = {
            'date':result[i]["dimensions"][0]["name"],
            'traffic-source':result[i]["dimensions"][1]["name"],
            'traffic-details':result[i]["dimensions"][2]["name"],
            'users':result[i]["metrics"][0],
            'visits':result[i]["metrics"][1],
            'pageviews':result[i]["metrics"][2],
            'bounceRate':result[i]["metrics"][3],
            'pageDepth':result[i]["metrics"][4],
            'avgVisitDurationSeconds':result[i]["metrics"][5]
          }

#Создаем DataFrame из dict (словаря данных или массива данных)
dict_keys = dict_data[0].keys()
df = pd.DataFrame.from_dict(dict_data, orient='index',columns=dict_keys)

#Выгрузка данных из DataFrame в Excel
df.to_excel("traffic2.xlsx",
        sheet_name='data',
        index=False)