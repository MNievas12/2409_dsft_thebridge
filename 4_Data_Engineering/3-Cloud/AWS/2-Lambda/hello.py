def lambda_handler(event, context):
    # Obtener parámetros de la solicitud (desde query string)
    name = event.get('queryStringParameters', {}).get('name', 'Amigo')
    
    return {
        'statusCode': 200,
        'body': {'message': f'Hola, {name}! Bienvenido a mi API Lambda.'}
    }