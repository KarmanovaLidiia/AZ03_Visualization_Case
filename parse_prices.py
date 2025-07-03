from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Открываем браузер (у тебя может быть Chrome или Firefox, выбери свой)
driver = webdriver.Chrome()  # Или Firefox(), если используешь Firefox

# Переходим на сайт
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)
time.sleep(5)  # ждём загрузку страницы

# Ищем цены
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Сохраняем цены в CSV
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # заголовок
    for price in prices:
        writer.writerow([price.text])

driver.quit()
print("Цены сохранены в файл prices.csv")
