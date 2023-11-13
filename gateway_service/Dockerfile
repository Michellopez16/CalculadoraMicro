# Utilizar la imagen oficial de Python como imagen base
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos y el script del servicio
COPY requirements.txt .
COPY gateway_service.py .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Indicar el puerto que el contenedor escuchará
EXPOSE 8000

# Comando para ejecutar el servicio
CMD ["uvicorn", "gateway_service:app", "--host", "0.0.0.0", "--port", "8000"]
