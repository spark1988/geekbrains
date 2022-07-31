# Вариант I
# Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172#

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime




chrome_options = Options()
chrome_options.add_argument('start-optimized')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://account.mail.ru/login')

driver.implicitly_wait(20)

elem = driver.find_element(By.NAME, 'username')
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.ENTER)

elem = driver.find_element(By.NAME, 'password')
elem.send_keys('NextPassword172#')
elem.send_keys(Keys.ENTER)

emails_set = set()

for i in range(5):
    articles = driver.find_elements(By.XPATH, "//a[contains(@class, 'js-letter-list-item')]")
    for el in articles:
        emails_set.add(el.get_attribute('href'))
    actions = ActionChains(driver)
    actions.move_to_element(articles[-1])
    actions.perform()
    time.sleep(5)

client = MongoClient('localhost', 27017)

# Connect to our database
db = client['parser_db']

# Fetch our series collection
series_collection = db['mail_ru']
series_collection.delete_many({})

def insert_document(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id


for link in emails_set:
    driver.get(link)
    author = driver.find_element(By.XPATH, "//div[contains(@class, 'letter__author')]/span[contains(@class, 'letter-contact')]").text
    date = driver.find_element(By.XPATH, "//div[contains(@class, 'letter__author')]/div[contains(@class, 'letter__date')]").text
    subject = driver.find_element(By.XPATH, "//h2[contains(@class, 'thread-subject')]").text
    text = driver.find_element(By.XPATH, "//div[contains(@class, 'letter-body__body-content')]").text
    email = {
        'author': author,
        'datetime': date.replace('Сегодня,', datetime.now().strftime("%Y-%m-%d")),
        'subject': subject,
        'text': text
    }
    insert_document(series_collection, email)

driver.close()