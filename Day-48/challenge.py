from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'E:\Development\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org')

dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
events = {}

for i in range(len(dates)):
    events[i] = {
        'time': dates[i].text,
        'name': names[i].text
    }
print(events)
driver.quit()

