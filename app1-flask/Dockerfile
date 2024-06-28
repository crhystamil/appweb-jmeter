# Utiliza una imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . .

# Indica que el contenedor escucha en el puerto 5000
EXPOSE 5000

# Define el comando para correr la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]

