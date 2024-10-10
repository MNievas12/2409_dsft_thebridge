from utils import *


lista_alumnos = ["Nathan", "Sengan", "Manuel"]

for alumno in lista_alumnos:
    print("Descargando personajes para", alumno)
    guardar_personajes_letra(alumno[0])