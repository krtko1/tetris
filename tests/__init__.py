import unittest


from tests.test_check_lost import TestCheckLost
from tests.test_convert_shape_format import TestConvertShapeFormat
from tests.test_create_grid import TestCreateGrid
from tests.test_get_shape import TestGetShape

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(
        [
            unittest.defaultTestLoader.loadTestsFromTestCase(TestConvertShapeFormat),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateGrid),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCheckLost),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetShape),
        ]
    )

    unittest.TextTestRunner().run(suite)
