import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = 'E:\Development\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://tinder.com/app/recs')

enter = driver.find_element(By.CLASS_NAME, 'l17p5q9z')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(enter).click(enter).perform()

Pos(r) Z(1) D(ib)


# button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn)
# Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-like-green):a