import unittest
from PIL import Image
import numpy as np
from read_img import read_dicom_file, read_jpg_file
import os

class TestImageReading(unittest.TestCase):

    def test_read_dicom_file(self):
        # Ruta a una imagen DICOM de prueba
        dicom_path = os.path.join(os.path.dirname(__file__), 'DICOM', 'normal (2).dcm')
        img_rgb, img_show = read_dicom_file(dicom_path)

        # Verificar que la salida es una matriz numpy
        self.assertIsInstance(img_rgb, np.ndarray)
        # Verificar que la salida es una imagen PIL
        self.assertIsInstance(img_show, Image.Image)

    def test_read_jpg_file(self):
        # Ruta a una imagen JPG de prueba
        jpg_path = os.path.join(os.path.dirname(__file__), 'JPG', 'normal', 'NORMAL2-IM-1147-0001.jpeg')
        img_rgb, img_show = read_jpg_file(jpg_path)

        # Verificar que la salida es una matriz numpy
        self.assertIsInstance(img_rgb, np.ndarray)
        # Verificar que la salida es una imagen PIL
        self.assertIsInstance(img_show, Image.Image)

if __name__ == '__main__':
    unittest.main()
