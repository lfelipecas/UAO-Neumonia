import numpy as np
from preprocess_img import preprocess
from load_model import model_fun
from grad_cam import grad_cam

def predict(array):
    batch_array_img = preprocess(array)
    model = model_fun()
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ["bacteriana", "normal", "viral"][prediction]
    heatmap = grad_cam(array)
    return (label, proba, heatmap)
