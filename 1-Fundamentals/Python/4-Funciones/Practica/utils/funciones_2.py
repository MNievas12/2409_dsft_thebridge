import math

def ejer_1(dia):
    dias_semana = {1: "Lunes", 
               2: "Martes",
               3: "Miércoles",
               4: "Jueves",
               5: "Viernes",
               6: "Sábado",
               7: "Domingo"}
    dia_str = dias_semana.get(dia, "Día erróneo")
    # print(dia_str)
    return dia_str


def ejer_2(filas):

    lista_8 = list(range(filas,0,-1))

    while len(lista_8) > 0:
        print(*lista_8)
        lista_8.pop(0)

def ejercicio_3(num_1:int|float, num_2:int|float):
    '''
    Comprueba si los números son iguales, mayores o menores
    '''
    # num_1 = float(num_1)
    if num_1 == num_2:
        out = "Son iguales"
    elif num_1 > num_2:
        out = "Primer número mayor que el segundo"
    else:
        out = "Segundo número mayor que el primero"

    return out

def limpieza_texto(texto, dict_vocales={'á':'a','é':'e','í':'i','ó':'o','ú':'u'}):
    texto = texto.lower()
    for clave in dict_vocales:
        texto = texto.replace(clave, dict_vocales[clave])
    return texto

def ejercicio_4(texto, letra):
    letra = letra.lower()
    texto = limpieza_texto(texto)
    return texto.count(letra)

def ejercicio_5(texto):
    dict_conteo = {}

    texto = limpieza_texto(texto)

    for caracter in texto:
        if caracter not in dict_conteo and caracter not in [" ", ","]:
            dict_conteo[caracter] = texto.count(caracter)

    return dict_conteo

def ejercicio_6(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        try:
            lista.remove(elemento)
        except:
            print("El elemento no se encuentra en la lista")
    else:
        print("Comando no reconocido")
    return lista

def ejercicio_7(*args):
    return " ".join(args)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def cuadrado(l):
    return l ** 2

def triangulo(b, a):
    return b * a / 2

def circulo(r):
    return math.pi * r ** 2