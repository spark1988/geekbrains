#спарсить с сайта мвидео карусель с товарами

from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

driver = webdriver.Chrome()

driver.get("https://www.mvideo.ru/")

driver.implicitly_wait(10)

driver.execute_script('window.scrollTo(0, 1700)')

elem = driver.find_element(By.XPATH, "//button/div/span[contains(text(), ' В тренде ')]")

elem.click()

names = driver.find_elements(By.XPATH,
                "//mvid-carousel[contains(@class, 'carusel ng-star-inserted')]//div[@class='title']/a[@class='ng-star-inserted']/div")


prices = driver.find_elements(By.XPATH,
                "//mvid-carousel[contains(@class, 'carusel ng-star-inserted')]//span[@class='price__main-value']")

info = []

for i in range(len(names)):
    data = {}
    data['Наименование'] = names[i].text
    data['Цена'] = prices[i].text
    info.append(data)

pprint(info)

driver.close()
