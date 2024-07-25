import unittest
import numpy as np
from integrator import predict

class TestPredict(unittest.TestCase):

    def test_predict(self):
        img = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
        label, proba, _ = predict(img)
        self.assertIn(label, ["bacteriana", "normal", "viral"])
        self.assertTrue(0 <= proba <= 100)

if __name__ == '__main__':
    unittest.main()
