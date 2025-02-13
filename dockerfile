# Usa una imagen base de Python 3.12
FROM python:3.12

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY . .

# Instala las dependencias del sistema necesarias para tus bibliotecas
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5002 para la aplicación Flask
EXPOSE 5002

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
