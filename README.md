# UAO-Neumonia: Detector de Neumonía

## Descripción

Este proyecto utiliza técnicas de aprendizaje profundo para detectar neumonía a partir de imágenes radiográficas. La aplicación presenta una interfaz gráfica que permite cargar imágenes DICOM o JPG y obtener predicciones junto con un mapa de calor generado mediante Grad-CAM.

## Requisitos

Para ejecutar el proyecto, es necesario instalar las siguientes librerías, especificadas en el archivo `requirements.txt`:
- TensorFlow 2.15.0
- Keras 2.15.0
- NumPy 1.26.4
- Matplotlib 3.9.1
- Pandas 2.2.2
- Pydicom 2.4.4
- OpenCV 4.10.0.84
- Pillow 10.4.0
- Img2pdf 0.5.1
- Tkcap 0.0.3

## Instalación

1. Clonar el repositorio:

   ```
   git clone https://github.com/tu_usuario/UAO-Neumonia.git
   cd UAO-Neumonia
   ```

2. Crear y activar un entorno virtual (opcional, pero recomendado):

   ```
   conda create -n env_tf_tensorflow python=3.10
   conda activate env_tf_tensorflow
   ```

3. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

4. Descargar el modelo y las imágenes por medio de este enlace [Google Drive](https://drive.google.com/drive/folders/13tel7QqV-ckvcpNUr0ic8j7Y49jlovX3?usp=sharing) y ubicarlas en el mismo directorio del proyecto.

## Uso

1. Ejecutar la aplicación:

   ```
   python detector_neumonia.py
   ```

2. Cargar una imagen DICOM o JPG y hacer clic en "Predecir" para obtener el resultado y el mapa de calor.

## Pruebas

Para ejecutar las pruebas unitarias:

1. Ejecutar las pruebas:

   ```
   python -m unittest test_nombre_del_archivo.py
   ```