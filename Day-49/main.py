import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = 'E:\Development\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://www.linkedin.com/jobs/view/information-technology-intern-remote-internship-at-rsi-security-31456009'
           '22?refId=Qq3a3W9R3kZOGG3GmzI1fQ%3D%3D&trackingId=cINs01OTmoV8rszAE8piuw%3D%3D&position=2&pageNum=0&trk=pub'
           'lic_jobs_jserp-result_search-card')

login = driver.find_element(By.CLASS_NAME, 'apply-button')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(login).click(login).perform()

username = driver.find_element(By.ID, 'username')
username.send_keys('youremail@mail.com')
password = driver.find_element(By.ID, 'password')
password.send_keys('password')
password.send_keys(Keys.ENTER)
time.sleep(1)
apply = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(apply).click(apply).perform()

number = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3145600922,'
                                    '4440116749549276268,phoneNumber~nationalNumber)')
number.send_keys('81982139440')
time.sleep(1)
apply = driver.find_element(By.ID, 'ember150')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(apply).click(apply).perform()

address = driver.find_element(By.CLASS_NAME, 'fb-single-line-text__input')
address.send_keys('Av Conselheiro Aguiar')
city = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3145600922,'
                                  '4891408810025353941,city~HOME_CITY)')
city.send_keys('Recife')
time.sleep(1)
city.send_keys(Keys.ARROW_DOWN)
city.send_keys(Keys.ENTER)
zipcode = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3145600922, '
                                     '5214191238009369236,text)')
zipcode.send_keys('51020-020')
state = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3145600922,'
                                   '5600389243786461541,text)')
state.send_keys('Pernambuco')
advance = driver.find_element(By.ID, 'ember150')
advance.click()
time.sleep(1)
advance = driver.find_element(By.ID, 'ember150')
advance.click()
time.sleep(1)

interest = driver.find_element(By.XPATH, '//*[@id="ember138"]/div/div[2]/form/div/div/div[1]/fieldset/div/div['
                                         '1]/label/span')
interest.click()

time = driver.find_element(By.XPATH, '//*[@id="ember138"]/div/div[2]/form/div/div/div[2]/fieldset/div/div[2]/'
                                     'label/span')
time.click()

bachelor = driver.find_element(By.XPATH, '//*[@id="ember138"]/div/div[2]/form/div/div/div[3]/fieldset/div/div['
                                         '1]/label/span')
bachelor.click()

expected = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3145600922,'
                                      '2126630064887395525,text)')
expected.send_keys('Dez-2023')

cybersecurity = driver.find_element(By.XPATH, '//*[@id="ember138"]/div/div[2]/form/div/div/div[5]/fieldset/div/div['
                                              '2]/label/span')
cybersecurity.click()

pay = driver.find_element(By.ID, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3145600922,'
                                 '1476839574773830656,text)')
pay.send_keys('$20-$30')

available = driver.find_element(By.XPATH, '//*[@id="ember138"]/div/div[2]/form/div/div/div[7]/fieldset/div/div['
                                          '1]/label/span')
available.click()

advance = driver.find_element(By.ID, 'ember239')
advance.click()

company = driver.find_element(By.XPATH, '//*[@id="ember138"]/div/div[2]/div/footer/div[1]/label')
company.click()

finish = driver.find_element(By.ID, 'ember250')
finish.click()
