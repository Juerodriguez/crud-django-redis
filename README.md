# Proyecto para práctica

Ejemplo práctico de CRUD con Redis dockerizando la aplicación e iniciando los servicios de la misma y Redis con
Docker Compose

Si quieres probar el proyecto clonalo instala docker.io y docker-compose luego ejecuta en bash:


```
docker-compose up

```

Por último accede al puerto 0.0.0.0/docs y podras ver la documentación de la API

---------------------------------------------

Si quieres ejecutar curl puedes hacerlo ;)

```
curl -X 'POST' \
  'http://0.0.0.0/books/create' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "author": "string"
}'
```

Los parámetros id y date se generaran automáticamente
