import unittest
from load_model import model_fun

class TestModelFun(unittest.TestCase):

    def test_model_fun(self):
        model = model_fun()
        self.assertIsNotNone(model)
        self.assertTrue(hasattr(model, 'predict'))

if __name__ == '__main__':
    unittest.main()
