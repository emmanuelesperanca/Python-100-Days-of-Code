import requests
from bs4 import BeautifulSoup
import smtplib

# Set your email and password
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "abcd1234()"

# Choose your product and how much you want to pay for it.
url = 'https://www.amazon.com/-/pt/dp/B09GJN716F/ref=sr_1_9?crid=3FD29LX0XZ5D6&currency=USD&keywords=notebook+monitor' \
      '&qid=1658886951&sprefix=%2Caps%2C147&sr=8-9 '
set_price = 300

# Headers obtained at http://myhttpheader.com, User-Agent below is a generic content.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US,en;q=0.9",
}

# Code for scraping and sending an email with an amazon price alert
response = requests.get(url=url, headers=headers)
website_html = response.text
soup = BeautifulSoup(website_html, 'lxml')
price = int(soup.find("span", class_='a-price-whole').getText().split(',')[0])
product_title = soup.find("span", class_='product-title-word-break').getText()
if price <= set_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        msg_text = f'{product_title} is now ${price}!\n{url}'
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{msg_text}"
        )
