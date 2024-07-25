import os
import tensorflow as tf

def model_fun():
    # Obtiene el directorio del archivo actual
    current_dir = os.path.dirname(__file__)
    
    # Construye la ruta al archivo del modelo en relación al directorio actual
    model_path = os.path.join(current_dir, 'conv_MLP_84.h5')
    
    return tf.keras.models.load_model(model_path)
