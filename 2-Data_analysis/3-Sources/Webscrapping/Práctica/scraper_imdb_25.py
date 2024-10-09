from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from fake_useragent import UserAgent
from datetime import datetime


url = "https://www.imdb.com/chart/top/"

ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)

soup = bs(response.content, 'html.parser')

dict_peliculas = {"Ranking": [x.get_text().split(".")[0] for x in soup.find_all("h3", class_="ipc-title__text")[1:26]],
                  "Titulo": [x.get_text().split(".")[1][1:] for x in soup.find_all("h3", class_="ipc-title__text")[1:26]],
                  "Año": [x.get_text() for x in soup.find_all("span", class_="sc-ab348ad5-8 cSWcJI cli-title-metadata-item") if len(x.get_text()) == 4],
                  "Duración": [x.get_text() for x in soup.find_all("span", class_="sc-ab348ad5-8 cSWcJI cli-title-metadata-item") if "h" in x.get_text()],
                  "Rating": [x.get_text() for x in soup.find_all('span', class_="ipc-rating-star--rating")]
}

df = pd.DataFrame(dict_peliculas)
now = str(datetime.now()).replace(" ","_").replace(":","_")[:16]
nombre = "top25_" + now + ".csv"
# print(nombre)
df.to_csv(nombre)