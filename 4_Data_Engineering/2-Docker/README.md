# 🐳TALLER DOCKER THE BRIDGE 🐳

> **En el taller de hoy vamos a ver lo básico que necesitamos saber para saber usar Docker en un entorno profesional sin tener conocimientos previos sobre la herramienta.**
> 

# 1. ¿Qué es Docker?

## Definición

> **Docker es un sistema operativo para contenedores. De manera similar a cómo una máquina virtual virtualiza (elimina la necesidad de administrar directamente) el hardware del servidor, los contenedores virtualizan el sistema operativo de un servidor.**
> 

## Características

- **MISMO ENTORNO**
    
    La idea de Docker es que te permite correr tu aplicación siempre en un mismo entorno. Esto quiere decir que todas las dependencias van a estar dentro de un mismo contenedor.
    
    Nosotros vamos a poder mover un contenedor entre una máquina u otra y nuestras dependencias siempre van a estar ahí dentro.
    
- **SANDBOX**
    
    Vamos a poder utilizar nuestro código independientemente del ordenador, sistema operativo o entorno en el que nos encontremos.
    
- **FÁCIL DE MOVER**
    
    Siempre funciona.
    

## Docker y Virtual Machine (VM)

Seguramente algunos de vosotros os estéis preguntando cuál es la diferencia entre Docker y una Virtual Machine.

![Untitled](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/Untitled.png)

- **Similitudes**
    
    La idea de una máquina virtual es que nuestras aplicaciones pueden correrse dentro de un sistema operativo y, para crear una nueva aplicación, vamos a tener que correr otra máquina virtual.
    
    Todo ello corre sobre un hipervisor y siempre sustentado por una infraestructura que puede ser, por ejemplo un servidor físico o una instancia en la nube.
    
- **Diferencias**
    
    La idea de Docker es que vamos a sacar una de esas capas de la ecuación y vamos a correr nuestra app junto con los archivos que necesita esa aplicación para correr.
    
    El kernel que corre cada uno de esos contenedores tiene un host compartido.
    
    Esto quiere decir que el host te da el kernel para que se corran mis aplicaciones.
    
    Esto quiere decir que un contenedor de Windows solo puede correr en un servidor que tenga un kernel de Windows.
    

**Imagino que ahora te estarás preguntando**

> ¿**Entonces cómo vamos a correr contenedores linux en una máquina con windows o con mac?**
> 

Cuando nosotros descargamos Docker Desktop, lo que estamos haciendo es crear una pequeño kernel que nos permite correr esos contenedores sobre ese kernel.

Simplemente esto nos viene bien a nivel de aprendizaje y desarrollo a pequeña escala, por lo que no debería preocuparnos el hecho de que tal vez nos tarde un poco más o ciertos procesos puedan ejecutarse más lentamente.

Lo ideal es correr un servidor linux con servidores de linux y así con cada sistema operativo.

![docker_etapas.png](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/docker_etapas.png)

# 2. Instalación de Docker

Para instalar docker:

```bash
https://www.docker.com/get-started
```

En función de nuestro sistema operativo, tendremos que descargar una versión de escritorio. Para los usuarios de Linux, entiendo que sabrán cómo apañárselas.

# 3. Funcionamiento de Docker

Básicamente Docker va a hacer lo siguiente:

> **Correr un contenedor a partir de una imagen**
> 

## **¿Qué es una imagen de Docker?**

> **Una imagen Docker es un archivo, compuesto por múltiples capas, que se utiliza para ejecutar código en un contenedor Docker. Estas imágenes son las plantillas base desde la que partimos ya sea para crear una nueva imagen o crear nuevos contenedores para ejecutar las aplicaciones.**
> 

**ESTRUCTURA**

- Sistema operativo.
    1. Ubuntu
    2. Debian
    3. Fedora
- Software
    1. Apache
    2. Php
    3. Mysql
- App
    1. Nuestro código

El código junto con las librerías y el sistema operativo son los elementos que componen nuestra imagen.

## ¿Cómo lanzamos esa imagen?

Para generar imágenes generamos lo que se conoce como Dockerfile

**DOCKERFILE**

> Archivo que contiene las instrucciones para crear nuestra imagen.
> 

Después de crear ese **Dockerfile**, corremos el comando que se llama `docker build` para generar esa imagen.

Si queremos correr esa imagen para crear este contenedor, utilizamos el comando `docker run` 

> **Probablemente, lo más interesante que tiene docker es que podemos correr un contenedor ejecutado por nosotros o bien podemos cargar una imagen que ha sido creada por otra persona.**
> 

Esto es genial porque nosotros podemos bajarnos una imagen ya creada y modificarla teniendo en cuenta las especificaciones de nuestra app.

### Ejemplo

Si queremos correr nuestro código Wordpress, en lugar de bajar una imagen de ubuntu, instalar todas las dependencias y demás, simplemente podemos bajarnos una imagen de wordpress y modificarla como queramos.

# Follow-Along

## AVISO PARA MAC 🍏

Es posible que tengáis un error a la hora de lanzar vuestros contenedores e imágenes por un tema de **PERMISOS.**

Para solucionarlo, tenéis que seguir los siguientes **PASOS:**

- **HABILITAR PERMISOS EN MAC**
    
    Abrir el menú 🍏 e ir a **"Preferencias del sistema"**
    
    Seleccionar **"Seguridad y Privacidad"**
    
    Hacer click en el **Candado** e introducir vuestra contraseña de usuario.
    
    En la barra desplegable de la izquierda, elegir **ACCESO TOTAL AL DISCO**
    
    Añadir una seleccionando el icono ➕
    
    Ir a Aplicaciones → Utilidades → Terminal
    
    **RELANZAR LA TERMINAL**
    
    [https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/](https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/)
    

## Correr una imagen

Vamos a correr una imagen a través de terminal

```bash
docker run postgres
```

**¿Cómo sé yo que hay una imagen que se llama *postgres?***

Esto lo tenemos en lo que se conoce como el registro de Docker.

Es el lugar en el que se hostean (es decir, se encuentran) estas imágenes.

```python
# Si no lo habéis hecho aún, tenéis que crearos vuestro usuario de Dockerhub
https://hub.docker.com/
```

Si aquí buscamos ***postgres***, vamos a tener todos los detalles sobre esta imagen, así como sus distintas versiones.

Si esta imagen no la tenemos previamente descargada, lo que se va a hacer es descargarla de Dockerhub, por eso veremos cómo se ejecutan varios comandos pull.

**Si queremos utilizar una versión concreta de una imagen, podemos añadirle un tag**

Si no especificamos, se va a descargar latest

Por ejemplo:

```python
# Es una buena práctica especificar la versión
docker run postgres:latest
```

Como véis, os habrá dado un error porque se exige que se añada un comando a correr.

En este caso, tenemos que mandarle una variable de entorno al contenedor para que se autoconfigure.

**NO OS PREOCUPÉIS. Si tenemos tiempo, lo veremos más adelante.**

**Por ahora, vamos a hacerle caso y a añadir esa línea de código.**

**FUNCIONA!!**

Como véis, yo no tengo descargado postgres en mi ordenador ni en ningún sitio. Simplemente creo esa imagen de postgres con la información necesaria para que mi app funcione.

Cuando se descarga una imagen, vamos a ver que cada una es un listado de capas, que vienen identificadas con su valor hash.

Nosotros podemos abrir una nueva terminal y correr una imagen de postgres con una versión distinta en otro contenedor dentro de un mismo servidor y no vamos a tener ningún problema.

## PostgreSQL + docker

Crear y lanzar contenedor postgreSQL

- Opción 1 - Te descarga imágen y carga el contenedor de una vez

```python
# Es una buena práctica especificar la versión
docker run --name postgres-db -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

- Opción 2

```python
docker pull postgres

docker images

docker create -e  POSTGRES_PASSWORD=Admin_123 -e  POSTGRES_USER=postgres  -p 5010:5432  --name psqlserver ID_IMAGEN2 - Acceder por consola al contenedor postgresql
```

```python
docker exec -it 608 bash
```

Para poder ejecutar el motor de PSQL tenemos que cambiarnos de usuario, en este caso usaremos el usuario "postgres".

```python
 psql -U postgres
```

- Comandos SQL

Creación de la BBDD y tablas (hay que definir la bbdd y tablas del proyecto)

```sql
CREATE DATABASE bbdd;

-- Conectarse a la BBDD
\c bbdd

-- Authors

CREATE TABLE authors (
  id_author serial NOT NULL PRIMARY KEY,
  name varchar(45) NOT NULL,
  surname varchar(45) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  image varchar(255)
);

-- Entries

CREATE TABLE entries (
  id_entry serial NOT NULL PRIMARY KEY,
  title varchar(100) NOT NULL,
  content text NOT NULL,
  date date DEFAULT CURRENT_DATE,
  id_author int,
  category varchar(15),
  FOREIGN KEY (id_author) REFERENCES authors(id_author)
);

-- Inserta varios autores

INSERT INTO authors(name,surname,email,image) VALUES
('Alejandru','Regex','alejandru@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/75.jpg'),
('Guillermu','Develawyer','develawyer@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/78.jpg'),
('Albertu','Henriques','albertu@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/80.jpg'),
('Alvaru','Arias','alvaru@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/70.jpg'),
('Birja','Ryvera','birja@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/72.jpg'),
('Muchelle','Ualis','muchelle@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/women/70.jpg'),
('Christianu','City','christianu@thebridgeschool.es','https://randomuser.me/api/portraits/thumb/men/45.jpg');

-- Insertar una entry del blog

INSERT INTO entries(title,content,id_author,category) VALUES ('Nos vamos de pizzas al patio','The bridge invita a pizzas por reto de tripus','1','Sucesos');
```

Cheatsheet comandos por consola:

[https://www.postgresqltutorial.com/postgresql-cheat-sheet/](https://www.postgresqltutorial.com/postgresql-cheat-sheet/)

[https://www.valentinog.com/blog/psql/](https://www.valentinog.com/blog/psql/)

## Comandos más comunes en Docker

```python
# Solamente va a descargar las imágenes
docker pull 

# Para ver todas las imágenes que tenemos
docker images

# Para ver los contenedores que estamos corriendo en este momento
docker ps

# Para ver todos los conetendores que corrimos y los que están en ejecución
docker ps -a

# Ver los logs del contenedor
docker logs <container_id>
docker logs <container_nam e>

# Ejecuta un comando en un contenedor que ya está corriendo
docker exec -it <container_id> # crear una sesion interactiva. Con la t creamos una shell

# Para parar un contenedor
docker stop <container_id>

# Para correr un contenedor en segundo plano
docker run -d <image>

```

## Desarrollando en Docker una app React

Ahora que ya sabemos desenvolvernos en docker, vamos ahora a intentar comprender cómo vamos a poder utilizarlo en la vida real.

**DESCARGAD/CLONAD ESTE ARCHIVO**

[https://github.com/alejandroereyesb/front-assesment](https://github.com/alejandroereyesb/front-assesment)

[front-assesment-main .zip](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/front-assesment-main_.zip)

![batman.png](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/batman.png)

**VAMOS A ECHAR UN VISTAZO AL PROYECTO**

Vamos a modificar un poco el proyecto para hacerlo nuestro, en nuestro App.js hay una tag <p> en la linea 16. 

La cambiamos por lo que nosotros queramos, por ejemplo poned:

<p>Dockerhub demo - by “Vuestro Nombre”</p>

### **CREAMOS UN ARCHIVO DOCKERFILE**

Para que el contenedor docker sepa que dependencias instalar tenemos que especificar unas órdenes:

```python
# pull official base image
FROM node:13.12.0-alpine
 
# set working directory
WORKDIR /app
 
# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH
 
# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
 
# add app
COPY . ./
EXPOSE 3001
 
# start app
CMD ["npm", "start"]
```

Y para evitar que en el contenedor se suban contenidos no necesarios tenemos un archivo .dockerignore

```jsx
node_modules
build
.dockerignore
Dockerfile
Dockerfile.prod
```

### **¿Por qué node?**

Porque es lenguaje utilizado por los compañeros de full-stack en el Desafío de Tripulaciones. Pero no os preocupéis, también vamos a ver un ejemplo en Python.

### **¿Por qué Alpine?**

Si nos vamos a Docker Hub, vamos a ver todas las versiones de las distintas imágenes que podemos utilizar. Si nos vamos a la que se está utilizando en este proyecto **(13.12.0-alpine)** vemos que aún así hay varias opciones. Esto simplemente son distintas distribuciones de Linux.

Sin entrar en mucho detalle, alpine es una distribución bastante empleada porque están pensadas para utilizar contenedores. Si vemos el espacio que ocupa, vemos que es muy pequeña en cuanto a memoria.

No tendría mucho sentido el utilizar una imagen de windows super pesada para levantar una app muy pequeñita. En términos de rendimiento, no tendría demasiado sentido.

**PARTES DE UN DOCKERFILE**

[Qué es DockerFile](https://openwebinars.net/blog/que-es-dockerfile/)

- **FROM** → se especifica la versión exacta de la imagen que queremos.
- **WORKDIR** → dentro del contenedor voy a crear una carpeta que se llama /app
- **COPY** → con este comando lo que estoy haciendo es pasar todo lo que tengo en el directorio en el que se encuentra el Dockerfile **(CON EL PRIMER PUNTO)** al contenedor en el directorio que le hemos creado **(EL SEGUNDO PUNTO)**
- **RUN** → nos permite ejecutar comandos dentro del contenedor, por ejemplo, instalar paquetes y librerías.
- **CMD** → a diferencia del RUN, cmd es lo que nos permite accionar ese contenedor a través de línea de comandos.
- **EXPOSE** → indica a la aplicación en que puerto se debe ejecutar

### CONSTRUIR UNA IMAGEN

Estando en la ubicación de nuestro dockerfile, para construir nuestra imagen, simplemente tenemos que hacer lo siguiente:

```python
# -t es para poner un tag

docker build -t <nombre-contenedor>:<tag> . (!IMPORTANTE EL PUNTO FINAL)

docker build -t react-docker:v1 .
```

Ahora nuestra imagen está construida, pero recuerdo una vez más que eso no es suficiente.

```python
# Si hacemos
docker ps
# No vamos a ver nada
```

Busca el ID de la imágen creada

```python
# busca la imágen creada
docker images
```

**VAMOS A POR ELLO**

```python
docker run -p 3001:3000 -t <id de imagen>
#Ejemplo:
docker run -p 3001:3000 -t 1e2387cc51b2
```

AHORA nuestro contenedor está corriendo

¿Si vamos a nuestro navegador debería de funcionar?

Vamos a probarlo.

### Docker Push

Una vez que hayamos terminado de trabajar con nuestra imagen haciendo todas las modificaciones pertinentes, tenemos que volver a construirla, y lo podemos hacer de la siguiente manera:

```python
docker build -t <cuentaDockerHub>/<nombre repositorio>:<tag> . (¡EL PUNTO!)

docker build -t christianciudad/react-docker:v1 .
```

De esta manera añadimos el tag de segunda versión.

Si nos fijamos, vemos que en la parte de **WORKDIR /app** nos sale **CACHED**. Eso quiere decir que hasta el momento, esos dos primeros pasos se conservan de la versión anterior.

Sin embargo, vemos que el punto de **COPY . .**  no lo está, porque es en este punto donde se han producido modificaciones. Entonces, a partir de ahí, se tienen que volver a correr los comandos **RUN y CMD**.

### Subir una imágen a [DockerHub](https://hub.docker.com/)

**¿Cómo puedo yo compartir esta imagen con otra persona?**

Ahora lo que podemos hacer es subirla a un registro.

En este caso vamos a subirlas a **DockerHub**, que nos permite subir nuestras imágenes siempre y cuando estas sean públicas.

**Para subirla, hay que seguir estos pasos:**

- Conectarte con tu cuenta.
    
    ```python
    docker login
    # Después te va a pedir nombre de usuario y contraseña
    Username:
    Password:
    # Ignorad el Warning
    ```
    
    Cuando quiero subir una imagen pública, el propio DockerHub me pide que lo haga con mi nombre de usuario delante para reconocer que es mía y así no guiarnos por nombres de archivo genéricos.
    
- Construyo la imagen con el nombre del repositorio de DockerHub
    
    ```python
    docker tag <image_id> <nombre_usuario/nombre_imagen>
    
    docker build -t <cuentaDockerHub>/<nombre repositorio>:<tag> . (¡EL PUNTO!)
    docker build -t christianciudad/react-docker:v1 .
    ```
    
    Si ahora volvemos a ver las imágenes que tenemos, vemos que hay dos imágenes con un pequeño cambio en el nombre, pero con el mismo tag y el mismo **IMAGE ID**
    
- Lanzar la imagen a **DockerHub**
    
    ```python
    docker push <nombre_usuario/imagen:tag> 
    
    docker push christianciudad/react-docker:v1
    ```
    

### Descargar una imagen subida en DockerHub

Ahora si queremos ejecutar la imagen subida por algún compañero debemos especificar los campos correspondientes:

```jsx
docker run -p 3001:3000 -t <id de contenedor/nombre contenedor>
```

## Desarrollando en Docker con Python

Ahora que ya sabemos desenvolvernos en docker, vamos ahora a intentar comprender cómo vamos a poder utilizarlo en la vida real.

**DESCARGAD/CLONAD ESTE ARCHIVO**

[https://github.com/alejandroereyesb/API_flask_docker](https://github.com/alejandroereyesb/API_flask_docker)

[API_flask_docker-main.zip](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/API_flask_docker-main.zip)

**VAMOS A ECHAR UN VISTAZO A EL PROYECTO**

Vamos a modificar un poco el proyecto para hacerlo nuestro, en nuestro  app.py modificamos el texto de la linea 10 que hay entre comillas. 

La cambiamos por lo que nosotros queramos, por ejemplo poned:

"Hello <tu nombre>! Welcome to Flask + Docker. Lets Rock and Roll”

![back-to-the-future-docker.jpg](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/back-to-the-future-docker.jpg)

### **CREAMOS UN ARCHIVO DOCKERFILE**

Para que el contenedor docker sepa que dependencias instalar tenemos que especificar unas ordenes:

```python
FROM python:3.8-alpine
RUN mkdir /src
WORKDIR /src
ADD . /src
RUN mkdir /src/tmp
RUN touch /src/tmp/data.txt
RUN echo "[{\"name\":\"alejandru\",\"email\":\"alejandru@gmail.com\"},{\"name\":\"birja\",\"email\":\"birja@gmail.com\"},{\"name\":\"muchelle\",\"email\":\"muchelle@gmail.com\"},{\"name\":\"christianu\",\"email\":\"christianu@gmail.com\"},{\"name\":\"alvaru\",\"email\":\"alvaru@gmail.com\"}]" >> /src/tmp/data.txt
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000
```

**PARTES DE UN DOCKERFILE**

[Qué es DockerFile](https://openwebinars.net/blog/que-es-dockerfile/)

- **FROM** → se especifica la versión exacta de la imagen que queremos.
- **WORKDIR** → dentro del contenedor voy a crear una carpeta que se llama /app
- **COPY** → con este comando lo que estoy haciendo es pasar todo lo que tengo en el directorio en el que se encuentra el Dockerfile **(CON EL PRIMER PUNTO)** al contenedor en el directorio que le hemos creado **(EL SEGUNDO PUNTO)**
- **RUN** → nos permite ejecutar comandos dentro del contenedor, por ejemplo, instalar paquetes y librerías.
- **CMD** → a diferencia del RUN, cmd es lo que nos permite accionar ese contenedor a través de línea de comandos.
- **EXPOSE** → indica a la aplicación en que puerto se debe ejecutar

### CONSTRUIR UNA IMAGEN

Estando en la ubicación de nuestro dockerfile, para construir nuestra imagen, simplemente tenemos que hacer lo siguiente:

```python
# -t es para poner un tag

docker build . -t <nombreusuario>/mi-app-flask
```

Ahora nuestra imagen está construida, pero recuerdo una vez más que eso no es suficiente.

```python
# Si hacemos
docker ps
# No vamos a ver nada
```

**VAMOS A POR ELLO**

```python
docker run -p 5000:5000 -d <nombreusuario>/mi-app-flask
```

AHORA nuestro contenedor está corriendo

¿Si vamos a nuestro navegador debería de funcionar?

Vamos a probarlo.

### Docker Push

Una vez que hayamos terminado de trabajar con nuestra imagen haciendo todas las modificaciones pertinentes, tenemos que volver a construirla, y lo podemos hacer de la siguiente manera:

```python
docker build -t <cuentaDockerHub>/<nombre repositorio>:<tag> . (¡EL PUNTO!)

docker build -t christianciudad/mi-app-flask
```

De esta manera añadimos el tag de segunda versión.

Si nos fijamos, vemos que en la parte de **WORKDIR /app** nos sale **CACHED**. Eso quiere decir que hasta el momento, esos dos primeros pasos se conservan de la versión anterior.

Sin embargo, vemos que el punto de **COPY . .**  no lo está, porque es en este punto donde se han producido modificaciones. Entonces, a partir de ahí, se tienen que volver a correr los comandos **RUN y CMD**.

### Subir una imagen a DockerHub

**¿Cómo puedo yo compartir esta imagen con otra persona?**

Ahora lo que podemos hacer es subirla a un registro.

En este caso vamos a subirlas a **DockerHub**, que nos permite subir nuestras imágenes siempre y cuando estas sean públicas.

**Para subirla, hay que seguir estos pasos:**

- Conectarte con tu cuenta.
    
    ```python
    docker login
    # Después te va a pedir nombre de usuario y contraseña
    Username:
    Password:
    # Ignorad el Warning
    ```
    
    Cuando quiero subir una imagen pública, el propio DockerHub me pide que lo haga con mi nombre de usuario delante para reconocer que es mía y así no guiarnos por nombres de archivo genéricos.
    
- Construyo la imagen con el nombre del repositorio de DockerHub
    
    ```python
    docker tag <image_id> <nombre_usuario/nombre_imagen>
    
    docker build -t <cuentaDockerHub>/<nombre repositorio>:<tag> . (¡EL PUNTO!)
    docker build -t christianciudad/mi-app-flask:v1.
    ```
    
    Si ahora volvemos a ver las imágenes que tenemos, vemos que hay dos imágenes con un pequeño cambio en el nombre, pero con el mismo tag y el mismo **IMAGE ID**
    
- Lanzar la imagen a **DockerHub**
    
    ```python
    docker push <nombre_usuario/imagen:tag> 
    
    docker push christianciudad/react-docker:v1
    ```
    

### Ejercicio: Descargar una imagen subida en DockerHub

Queremos ejecutar la imagen subida a dockerHub por algún/a compañero/a 

## DOCKER COMPOSE

![docker-compose.jpg](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/docker-compose.jpg)

- [microservices](https://www.redhat.com/es/topics/microservices)

Seguro que muchos de vosotros estaréis pensando:

> **¿Cómo c*** me voy a acordar de todos esos comandos?**
> 

Seguramente ya os ha pasado que si os equivocáis en una línea o un espacio o guion, probablemente no os funcione.

Pero la gente de Docker es maravillosa e inventó una cosa llamada **Docker compose**.

Pero antes de nada lo que vamos a hacer es frenar estos dos contenedores.

Ahora lo que vamos a hacer es abrir un `docker-compose.yaml` (podéis hacerlo desde terminal o en la propia carpeta de archivos).

[docker-compose.yaml](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/docker-compose.yaml)

[app.zip](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/app.zip)

![docker-compose-meme.jpg](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/docker-compose-meme.jpg)

### PARTES DE UN DOCKER COMPOSE

Como podéis ver, el comentario del docker compose son la serie de comandos que hemos metido a través de terminal.

Vamos a ir paso a paso viendo qué es cada cosa.

Al crear un docker-compose ya se crea una propia red, por lo que no va a hacer falta habilitar una network, sino que lo va a hacer por defecto.

Este es un archivo yaml, similar a un JSON que sigue la lógica clave-valor.

Podemos diferenciar dos secciones importantes:

- version
- services
    - es donde declaramos los servicios que vamos a correr dentro de Docker compose.
    - Nos permite correr varios contenedores a través de un solo archivo que crea una red para todos ellos.
    - Tenemos la app y mysql:
        - image: la imagen que vamos a correr.
        - ports: los puertos expuestos.
        - environment: donde declaramos todas las variables de entorno.

**Para correr docker compose:**

Estando en la carpeta en la que se encuentra `docker-compose.yaml` 

```jsx
docker-compose up -d
```

**Para parar el multicontenedor**

```jsx
docker-compose down
```

### DEMOS APP FULLSTACK MERN: React + Express + MongoDB + Docker Compose

![Untitled](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/Untitled%201.png)

[https://github.com/alejandroereyesb/products_mern](https://github.com/alejandroereyesb/products_mern)

[https://github.com/alejandroereyesb/mern-docker](https://github.com/alejandroereyesb/mern-docker)

[mern-docker-master.zip](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/mern-docker-master.zip)

La parte de react está en

[http://localhost:8080](http://localhost:8080/)

Fichero docker-compose.yml

```jsx
version: '3.7'
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    env_file: ./server/.env
    environment:
      NODE_ENV: production
    depends_on:
      - mongo
    networks:
      - app-network
  mongo:
    image: mongo
    volumes:
      - data-volume:/data/db
    ports:
      - "27017:27017"
    networks:
      - app-network

networks:
    app-network:
        driver: bridge

volumes:
    data-volume:
    node_modules:
    web-root:
      driver: local
```

Producción. Funciona en puerto 8080(server) y puerto 8080 (client)

```jsx
docker-compose up -d --build --remove-orphans

//La parte de react está en http://localhost:8080
//Funciona en puerto 8080(server) y puerto 8080 (client)

docker-compose down

// Crear algunas noticias
POST http://localhost:8080/api/posts

//Ejemplo 1:
{
"title":"The Bridge se prepara para la fiesta de reto de tripulaciones",
"body":"Ojo con ",
"author":"Pepe perez"
}

// Ejemplo 2:
{
"title": "Dónde están mis amigos?",
"body": "Huele a que nos vamos al rocafría a por tarta de limón",
"author": "Alvaru"
}

// Devolver todas las noticias creadas
GET http://localhost:8080/api/posts/

// Editar una noticia ya creada por ID
PATCH http://localhost:8080/api/posts/:post_id
PATCH http://localhost:8080/api/posts/61dd7868491e9c004ae1833c

// Pasar por Body los nuevos datos

{
"title": "Vamos a por un margarita",
"body": "El mexicano amplía capacidad para que vaya todo The Bridge",
"author": "Muchelle"
}

// Borrar una noticia por ID

DELETE http://localhost:8080/api/posts/:post_id
DELETE http://localhost:8080/api/posts/61dd7868491e9c004ae1833c
```

Interactuar con la BBDD MongoDB

```jsx
//Acceder a la consola de MongoDB desde la Shell
docker exec -it ID_container sh

//Ver las BBDD correspondientes
show dbs

//Usar la BBDD correspondiente
use myapp_db

//Ver colecciones
show collections

Desde dentro del contenedor, accedo a la colección de posts, hago un find() de MongoDB por consola y me devuelve todos los documentos.
db.posts.find()

Insertar un documento en la BBDD MongoDB
db.posts.insertOne({"title":"El mejor bocata del barrio - Rocafía","body":"Ojo con el bocata lomo Queso de Rocafría","author":"Guillermu"})

Borrar un documento
db.posts.deleteOne({"title":"El mejor bocata del barrio 2 - Rocafía"})
```

### DEMO APP FULLSTACK PERN: React + Express + PostgreSQL + Docker Compose

[https://github.com/JavierEspinosaP/demo-mern-docker-compose](https://github.com/JavierEspinosaP/demo-mern-docker-compose)

![Untitled](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/Untitled%202.png)

### DE CAMINO A MICROSERVICIOS

> La **arquitectura de microservicios** es una aproximación para el desarrollo de software que consiste en construir una aplicación como un conjunto de pequeños servicios, los cuales se ejecutan en su propio proceso y se comunican con mecanismos ligeros.- [Wikipedia](https://es.wikipedia.org/wiki/Arquitectura_de_microservicios)
> 

- [¿Qué son y para qué sirven los microservicios?](https://www.redhat.com/es/topics/microservices)
- E[ntendiendo qué son los contenedores y por qué es una de las mayores revoluciones de la industria del desarrollo](https://www.xataka.com/otros/docker-a-kubernetes-entendiendo-que-contenedores-que-mayores-revoluciones-industria-desarrollo)

![microservices (1).png](%F0%9F%90%B3TALLER%20DOCKER%20THE%20BRIDGE%20%F0%9F%90%B3%20d2e78aebd67b4b41935d71e3a375a3f1/microservices_(1).png)

### INFORMACIÓN ADICIONAL

- [Cheatsheet](https://devhints.io/docker) → Docker
- [Despliegue-de-aplicaciones-con-docker-compose](https://colaboratorio.net/davidochobits/sysadmin/2018/despliegue-de-aplicaciones-con-docker-compose/)
- [Cheatsheet para trabajar con MongoDB por consola](https://www.digitalocean.com/community/tutorials/how-to-use-the-mongodb-shell)