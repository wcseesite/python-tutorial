import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=python+tutorial'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))