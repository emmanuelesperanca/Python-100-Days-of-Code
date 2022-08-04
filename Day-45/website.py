from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com')
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
article_texts = []
article_links = []
article_points = []
article = soup.find_all(class_='titlelink')
points = soup.find_all(name='span', class_='score')

for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_points = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]


