import unittest

from tests.test_get_shape import TestGetShape

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestGetShape))
    unittest.TextTestRunner().run(suite)