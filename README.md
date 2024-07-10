# appweb-jmeter

Desplegar app1-flask

```bash
sudo docker build -t app1 .
sudo docker run -p 5000:5000 app1 
```

Desplegar api-flask

```bash
sudo docker-compose up 
```

Una vez iniciado los contenedores, ingresar al docker api-flask-web
Con el siguiente comando listamos los contenedores.

```bash
sudo docker ps 
```

buscamos el docker api-flask-web y ejecutamos algunos comandos.

```bash
sudo docker exec -ti XXXXXXXX bash 
```

iniciar la base de datos.

```bash
flask db init
flask db upgrade
```
Generar datos que sean introducidos en la DB.

```bash
python generate_products.py
```

