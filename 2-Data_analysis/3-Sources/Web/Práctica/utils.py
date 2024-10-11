import hashlib
import requests
import datetime
import pandas as pd

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


def obtener_personajes(url, params):

    res = requests.get(url,params=params)
    res_json = res.json()
    return res_json

def almacenar_dataframe(respuesta):

    marvel_dict = {"id": [x.get('id') for x in respuesta['data']['results']],
               "name": [x.get('name') for x in respuesta['data']['results']],
               "picture_url": [x.get('thumbnail').get('path') + '.' + x.get('thumbnail').get('extension') for x in respuesta['data']['results']]}

    return pd.DataFrame(marvel_dict)

def guardar_personajes_letra(letra):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

    pub_key = ''
    priv_key = ''
    
    params = {'ts': timestamp, 
        'apikey': pub_key, 
        'hash': hash_params(timestamp,priv_key,pub_key),
        'nameStartsWith': letra,
        'offset': 0,
        'limit': 100
        };

    url = 'http://gateway.marvel.com/v1/public/characters'

    respuesta = obtener_personajes(url, params)

    df = almacenar_dataframe(respuesta)

    while len(df) < respuesta['data']['total']:
        print("Faltan aún datos por obtener")
        params['offset'] += 100
        respuesta = obtener_personajes(url, params)
        df = pd.concat([df, almacenar_dataframe(respuesta)], ignore_index=True)

    df.to_csv("./data/marvel_chars_" + letra + ".csv")