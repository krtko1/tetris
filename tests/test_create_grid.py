import unittest

from tetris import constants, create_grid


class TestCreateGrid(unittest.TestCase):
    def test_grid_size(self):
        grid = create_grid()
        self.assertEqual(len(grid), constants.rows)
        self.assertTrue(all(len(row) for row in grid))

    def test_grid_default_values(self):
        grid = create_grid()
        default_value = (0, 0, 0)
        self.assertTrue(all(all(col == default_value for col in row) for row in grid))

    def test_grid_with_locked_positions(self):
        default_value = (0, 0, 0)
        locked_positions = {
            (0, 0): (0, 128, 64),
            (0, 1): (0, 18, 87),
            (2, 3): (25, 0, 81),
            (4, 5): (18, 47, 11),
            (8, 7): (18, 120, 200),
            (-8, -7): (63, 120, 200),
            (9999, 9999): (111, 111, 111),
        }
        grid = create_grid(locked_positions)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_positions:
                    self.assertEqual(grid[i][j], locked_positions[(j, i)])
                else:
                    self.assertEqual(grid[i][j], default_value)


if __name__ == "__main__":
    unittest.main()
