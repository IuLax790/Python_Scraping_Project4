#Scrapping with requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

source = requests.get('https://outdooradventurestore.ie/blog/category/camping/').text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())


article = soup.find('article')
print(article.prettify())

img_src = article.find('img',alt="")['src']

print("Image:",img_src)
headline = article.h2.a.text
print("Article Headline:",headline)
