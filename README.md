
# Creditoo API

Implementacion de la API para aplicaciones de Creditoo.

## Tech Stack

**Server:** Python, Django

**Containers:** Docker

**Database:** Postgres

## Instalacion

### Containers
Para construir los contenedores de la base de datos vamos a usar Docker Compose. Usando la terminal vamos a la raiz del proyecto y ejecutar:

```bash
$ docker-compose up
```
Los contenedores de PgAdmin y Postgres deberian crearse.

### Python Environment
Con python vamos a usar VirtualEnv para administrar las dependencias del proyecto. En la raiz del proyecto (creditoo-api) ejecutar:

```bash
$ virtualenv venv
```
Esta instruccion va a crear un entorno virtual llamado "venv". Antes de ejecutar el proyecto activemos el ambiente virtual ejecutando:

Mac/Linux: 
```bash
$ source venv/bin/activate
```

Windows:
```bash
PS C:\> <venv>\Scripts\Activate.ps1
```

Con el ambiente virtual activado (venv) ahora instalemos las dependencias del proyecto ejecutando:

```bash
$ pip install -r requirements.txt
```

## Running App
Para ejecutar este proyecto ejecutar desde la carpeta "creditoo"

```bash
  python manage.py runserver
```

  