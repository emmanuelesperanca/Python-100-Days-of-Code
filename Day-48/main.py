from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from time import time

chrome_driver_path = 'E:\Development\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

minutes = 5
fiveMinutes = time() + 60*minutes

while fiveMinutes > time():
    click_cookie = driver.find_element(By.ID, 'cookie')
    click_cookie.click()
    try:
        time_machine_value = int(driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= time_machine_value:
            buy_time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
            buy_time_machine.click()
    except StaleElementReferenceException:
        pass
    try:
        portal_value = int(driver.find_element(By.CSS_SELECTOR, '#buyPortal b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= portal_value:
            buy_portal = driver.find_element(By.CSS_SELECTOR, '#buyPortal')
            buy_portal.click()
    except StaleElementReferenceException:
        pass
    try:
        alchemy_lab_value = int(driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= alchemy_lab_value:
            buy_alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
            buy_alchemy_lab.click()
    except StaleElementReferenceException:
        pass
    try:
        shipment_value = int(driver.find_element(By.CSS_SELECTOR, '#buyShipment b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= shipment_value:
            buy_shipment = driver.find_element(By.CSS_SELECTOR, '#buyShipment')
            buy_shipment.click()
    except StaleElementReferenceException:
        pass
    try:
        mine_value = int(driver.find_element(By.CSS_SELECTOR, '#buyMine b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= mine_value:
            buy_mine = driver.find_element(By.CSS_SELECTOR, '#buyMine')
            buy_mine.click()
    except StaleElementReferenceException:
        pass
    try:
        factory_value = int(driver.find_element(By.CSS_SELECTOR, '#buyFactory b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= factory_value:
            buy_factory = driver.find_element(By.CSS_SELECTOR, '#buyFactory')
            buy_factory.click()
    except StaleElementReferenceException:
        pass

    try:
        grandma_value = int(driver.find_element(By.CSS_SELECTOR, '#buyGrandma b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= grandma_value:
            buy_grandma = driver.find_element(By.CSS_SELECTOR, '#buyGrandma')
            buy_grandma.click()
    except StaleElementReferenceException:
        pass

    try:
        cursor_value = int(driver.find_element(By.CSS_SELECTOR, '#buyCursor b').text.split('-')[-1].replace(",", ""))
        money = int(driver.find_element(By.ID, 'money').text)
        if money >= cursor_value:
            buy_cursor = driver.find_element(By.CSS_SELECTOR, '#buyCursor')
            buy_cursor.click()
    except StaleElementReferenceException:
        pass

cookies_per_second = driver.find_element(By.ID, 'cps').text
print(cookies_per_second)

driver.quit()
