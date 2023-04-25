import unittest
from tests.test_convert_shape_format import TestConvertShapeFormat


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestConvertShapeFormat))

    unittest.TextTestRunner().run(suite)