import tensorflow as tf

def model_fun():
    # The following path is an example of a local path used during development.
    # Replace it with your own path to the model file.
    model_path = r"H:\My Drive\UAO_EIA\5_Desarrollo_Proyectos_IA\Modulo_1_Introduccion_Desarrollo_Software\UAO-Neumonia\conv_MLP_84.h5"
    return tf.keras.models.load_model(model_path)
