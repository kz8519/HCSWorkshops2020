import urllib
from bs4 import BeautifulSoup
import requests
import webbrowser

text = 'november'
text = urllib.parse.quote_plus(text)

url = 'https://www.foodnetwork.com/search/' + text + '-'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for g in soup.find_all(class_='m-MediaBlock__a-HeadlineText'):
    print(g.get_text())
    print('---')


