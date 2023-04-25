import unittest

from tetris import check_lost


class TestCheckLost(unittest.TestCase):
    def test_all_positive_positions(self):
        positions = {(1, 18): (0, 255, 0), (2, 18): (0, 255, 0), (5, 5): (88, 25, 72), (10, 2): (14, 22, 200)}
        self.assertFalse(check_lost(positions))

    def test_zero_x_positions(self):
        positions = {(0, 12): (0, 255, 0), (0, 18): (0, 255, 0), (0, 5): (88, 25, 72), (0, 2): (14, 22, 200)}
        self.assertFalse(check_lost(positions))

    def test_negative_x_positions(self):
        positions = {(-1, 18): (0, 255, 0), (-5, 5): (88, 25, 72), (-10, 2): (14, 22, 200), (-22, 1): (88, 12, 0)}
        self.assertFalse(check_lost(positions))

    def test_zero_y_positions(self):
        positions = {(8, 0): (72, 55, 89), (4, 8): (0, 255, 0), (9, 0): (8, 2, 17), (10, 0): (14, 22, 200)}
        self.assertTrue(check_lost(positions))

    def test_negative_y_positions(self):
        positions = {(1, -1): (0, 255, 0), (2, -8): (0, 255, 0), (5, -77): (88, 25, 72), (10, -98): (14, 22, 220)}
        self.assertTrue(check_lost(positions))

if __name__ == "__main__":
    unittest.main()
