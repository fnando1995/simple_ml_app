# Usa una imagen base de Python 3.12
FROM python:3.12-slim

RUN mkdir -p /usr/app/src
RUN mkdir -p /usr/app/data

# Establecer el directorio de trabajo
WORKDIR /usr/app/

# Copiar los archivos requeridos al contenedor
COPY requirements.txt .
COPY src/* ./src
COPY data/* ./data

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la API
EXPOSE 8000

# Comando para ejecutar la API
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"] 
