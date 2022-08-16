import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = 'E:\Development\chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = ''
        self.up = ''

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        time.sleep(3)

        test_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(test_speed).click(test_speed).perform()
        time.sleep(60)

        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = download_speed.text
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = upload_speed.text

        self.driver.quit()
        return self.down, self.up

    def tweet_results(self, your_google_email, your_google_password, down, up):
        self.driver.get('https://twitter.com/login')
        wait = WebDriverWait(self.driver, 10)

        # Save twitter window on a variable
        original_window = self.driver.current_window_handle
        time.sleep(3)

        # Click on login with Google
        continue_google = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
        continue_google.click()

        # Wait to open the new window
        wait.until(EC.number_of_windows_to_be(2))

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        # Write your email
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        self.driver.implicitly_wait(10)
        email.send_keys(f'{your_google_email}')

        # Click next
        next_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_btn.click()

        # Write your password
        password = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        self.driver.implicitly_wait(10)
        password.send_keys(f'{your_google_password}')
        time.sleep(1)
        next_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_btn.click()
        time.sleep(1)

        # Switch back to the original window
        self.driver.switch_to.window(original_window)

        # Write your tweet
        time.sleep(3)
        type_message = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span > br')
        type_message.send_keys(f'@ClaroBrasil Eu pago por 300MB down e 30MB up. Estou recebendo agora {down}MB down e {up}MB up.')
        time.sleep(1)

        # Send it
        tweet = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()

        # Close browser
        time.sleep(1)
        self.driver.quit()
