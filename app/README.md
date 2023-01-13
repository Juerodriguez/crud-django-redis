# Proyecto para practica

- Se logro practicar con redis serverless gracias al servicio provisto por https://upstash.com/ 
- Se realizo la configuracion de un CRUD en FastApi, y se configuro las variables de entorno .env para no exponer claves 

Si quieres probar el proyecto clonalo configura el servicio redis las variables de entorno y ejecuta:

Primero:

```
pip install -r requirements.txt

```
Luego:

```
uvicorn run:app --reload --env-file=.env

```