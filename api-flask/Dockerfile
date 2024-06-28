# Utiliza una imagen base de Python
FROM python:3.8-slim

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean

# Copia los requisitos e instala las dependencias de Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . /app

# Expone el puerto 5000
EXPOSE 5000

# Comando para correr la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]

