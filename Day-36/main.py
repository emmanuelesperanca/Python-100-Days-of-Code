import requests as requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = (os.environ['STOCK_API_KEY'])
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = (os.environ['NEWS_API_KEY'])
TWILIO_SID = (os.environ['TWILIO_SID'])
TWILIO_AUTH = (os.environ['TWILIO_AUTH'])

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

# Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = (difference / float(yesterday_closing_price)) * 100

# News API to get articles related to the COMPANY_NAME.

if abs(diff_percent) > 1:
    news_params = {
        "apikey": NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    three_articles = articles[:3]

# Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f'{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article["title"]}. ' \
                      f'\n Brief: {article["description"]}' for article in three_articles]

# Send each article as a separate message via Twilio.

client = Client(TWILIO_SID, TWILIO_AUTH)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=(os.environ['from_']),
        to=(os.environ['to']),
    )
