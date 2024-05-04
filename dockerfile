# Usamos la imagen oficial de Python 3 como base
FROM python:3

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el archivo de requerimientos (requirements.txt) al directorio de trabajo
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido del directorio actual al directorio de trabajo
COPY . .

# Exponemos el puerto 8000 para poder acceder a la aplicación
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django en el puerto 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
