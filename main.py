import time

import random
from selenium import webdriver

chromedriver = r'C:\\Users\\esbha\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chromedriver)

driver.get('https://www.youtube.com/watch?v=n8ipgADH6Tg')



while True:
    time.sleep(1)
    driver.refresh()

