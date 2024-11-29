# pip install requests -t .
import requests

def lambda_handler(event, context):
    url = "https://www.kaggle.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': f"Kaggle está disponible. Status: {response.status_code}"
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': f"No se pudo conectar a Kaggle. Status: {response.status_code}"
        }