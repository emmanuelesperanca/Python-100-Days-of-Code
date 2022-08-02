from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'E:\Development\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')



name = driver.find_element(By.NAME, 'search')
name.send_keys('Python')
name.send_keys(Keys.ENTER)
python = driver.find_element(By.LINK_TEXT, 'Python (programming language)')
python.click()
driver.quit()
