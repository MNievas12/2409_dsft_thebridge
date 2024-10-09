from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from fake_useragent import UserAgent
from datetime import datetime
import json


url = "https://www.imdb.com/chart/top/"

ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)

soup = bs(response.content, 'html.parser')

data = json.loads(soup.find('script', {'type':"application/ld+json"}).text)
data_next = json.loads(soup.find("script", {'id': '__NEXT_DATA__'}).text)


dict_peliculas = {"Ranking": [x['currentRank'] for x in data_next['props']['pageProps']['pageData']['chartTitles']['edges']],
                  "Titulo": [x['item'].get('alternateName', x['item']['name']) for x in data['itemListElement']],
                  "Año": [x['node']['releaseYear']['year'] for x in data_next['props']['pageProps']['pageData']['chartTitles']['edges']],
                  "Duración": [x['item']['duration'][2:] for x in data['itemListElement']],
                  "Rating": [x['item']['aggregateRating']['ratingValue'] for x in data['itemListElement']]
}

df = pd.DataFrame(dict_peliculas)
now = str(datetime.now()).replace(" ","_").replace(":","_")[:16]
nombre = "top250_" + now[5:] + ".csv"
# print(nombre)
df.to_csv(nombre)