# Utilizar una imagen de Python
FROM python:3.11-slim

# Establecer el directorio del contendor
WORKDIR /app

# Copiamos los archivos al directorio del contenedor
COPY . /app

# Instalar las dependecias
RUN pip install -r requirements.txt

# Exponer el puerto en el que la aplicación está corriendo en el contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación
# CMD ["python", "app_model.py"]
CMD ["uvicorn", "app_model:app", "--host", "0.0.0.0"]