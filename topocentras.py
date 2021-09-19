from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import csv

CHROMEDRIVER_PATH = 'drivers/chromedriver.exe'

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
driver.get('https://www.topocentras.lt/kompiuteriai-ir-plansetes/nesiojamieji-kompiuteriai.html')

time.sleep(5) # Optimize time

prices = driver.find_elements_by_xpath('//div/div/div[6]/div/div/span')
# titles = driver.find_elements_by_xpath('//div/div[1]/div[3]')
for price in prices:
    print(price.text)

with open('topocentras.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(price.text)




