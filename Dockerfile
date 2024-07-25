# Usar una imagen base oficial de Python
FROM python:3.10

# Instalar dependencias del sistema necesarias
RUN apt-get update && \
    apt-get install -y python3-opencv xvfb && \
    apt-get clean

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["xvfb-run", "-a", "python", "detector_neumonia.py"]