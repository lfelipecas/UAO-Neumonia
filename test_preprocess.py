import unittest
import numpy as np
from preprocess_img import preprocess

class TestPreprocess(unittest.TestCase):

    def test_preprocess(self):
        img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        processed_img = preprocess(img)
        self.assertEqual(processed_img.shape, (1, 512, 512, 1))
        self.assertTrue(np.all(processed_img >= 0) and np.all(processed_img <= 1))

if __name__ == '__main__':
    unittest.main()
