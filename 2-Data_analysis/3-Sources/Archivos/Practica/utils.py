import os
import shutil


def ordenar_carpeta(ruta_carpeta, categorias):
    for categoria in categorias:
        os.makedirs(ruta_carpeta + "/" + categoria, exist_ok = True)
        for archivo in os.listdir(ruta_carpeta):
            ruta_archivo = ruta_carpeta + "/" + archivo
            print("Archivo", archivo)
            if os.path.isdir(ruta_carpeta + "/" + archivo):
                print("Carpeta", archivo)
            elif archivo.endswith(categorias[categoria]) or categoria == "Otros":
                print(archivo, "Moviendo a", categoria)
                shutil.move(ruta_archivo, ruta_carpeta + "/" + categoria)

class Fichero:

    def __init__(self, categoria, extensiones, ruta):
        self.categoria = categoria
        self.extensiones = extensiones
        self.ruta = ruta

    def crear_categoria(self):
        os.makedirs(self.ruta + "/" + self.categoria, exist_ok = True)

    def mover_archivos(self):
        for archivo in os.listdir(self.ruta):
            ruta_archivo = self.ruta + "/" + archivo
            print("Archivo", archivo)
            if os.path.isdir(self.ruta + "/" + archivo):
                print("Carpeta", archivo)
            elif archivo.endswith(self.extensiones) or self.categoria == "Otros":
                print(archivo, "Moviendo a", self.categoria)
                shutil.move(ruta_archivo, self.ruta + "/" + self.categoria)