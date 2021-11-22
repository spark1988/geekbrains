# https://ekaterinburg.hh.ru/search/vacancy ? +clusters=true&ored_clusters=true & enable_snippets=true+& text=Data+analyst&from=suggest_post& area=113 & search_field=description&search_field=company_name&search_field=name
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pprint import pprint

pos = input('Выберите профессию: ')

pages = int(input('Сколько страниц вывести?'))

url = 'https://hh.ru'

params = {
    'clusters' : 'true',
    'area' :  1,
    'ored_clusters' : 'true',
    'enable_snippets' : 'true',
    'salary' : 'true',
    'text' : pos,
    'page' : 0
}

headers = {
'User-Agent' : 'V8 9.5.172.25 User Agent	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

vacancy_list = []
while params['page'] < pages:
    response = requests.get(url + '/search/vacancy', params=params, headers=headers)
    dom = bs(response.text, 'html.parser')
    vacancies = dom.find_all('div', {'class' : 'vacancy-serp-item'})

    if response.ok and vacancies:
        for vacancy in vacancies:
            vac_data = {}
            info = vacancy.find('a', {'class' : 'bloko-link'})
            name = info.text
            company = vacancy.find('div', {'class': 'bloko-text bloko-text_small bloko-text_tertiary'}).text
            place = vacancy.find('div', {'class' : 'bloko-text bloko-text_small bloko-text_tertiary'}).nextSibling.text
            link = info['href']
            site = url

            try:
                salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text.split()
                if salary[0] == 'до':
                    salary_min = None
                    salary_max = int(salary[1] + salary[2])
                    salary_currency = salary[3]
                elif salary[0] == 'от':
                    salary_min = int(salary[1] + salary[2])
                    salary_max = None
                    salary_currency = salary[3]
                else:
                    salary_min = int(salary[0] + salary[1])
                    salary_max = int(salary[3] + salary[4])
                    salary_currency = salary[5]
            except:
                salary_min = None
                salary_max = None
                salary_currency = None
            try:
                date = vacancy.find('span', {'class': 'vacancy-serp-item__publication-date'}).text.replace('\xa0', ' ')
            except:
                date = None

            vac_data['name'] = name
            print(vac_data['name'])
            vac_data['company'] = company
            print(vac_data['company'])
            vac_data['place'] = place
            print(vac_data['place'])
            vac_data['link'] = link
            print(vac_data['link'])
            # vac_data['salary'] = salary
            vac_data['salary_min'] = salary_min
            print(f"минимальная ставка {vac_data['salary_min']}")
            vac_data['salary_max'] = salary_max
            print(vac_data['salary_max'])
            vac_data['salary_currency'] = salary_currency
            print(f"валюта =  {vac_data['salary_currency']}")
            vac_data['date'] = date
            print(f"дата публикации {vac_data['date']}")

            vacancy_list.append(vac_data)
        print(f"Обработка {params['page']+1} страницы")
        params['page'] += 1
    else:
        break
result = pd.DataFrame(vacancy_list)
result.to_excel(f'vac-{pos}.xlsx')
print('Finish')