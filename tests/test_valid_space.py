import unittest

from tetris import constants, convert_shape_format, create_grid, valid_space
from tetris.piece import Piece


class TestValidSpace(unittest.TestCase):
    def test_S_shape_true(self):
        piece = Piece(5, 4, constants.shapes[0])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_Z_shape_true(self):
        piece = Piece(5, 4, constants.shapes[1])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_I_shape_true(self):
        piece = Piece(5, 4, constants.shapes[2])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_O_shape_true(self):
        piece = Piece(5, 4, constants.shapes[3])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_J_shape_true(self):
        piece = Piece(5, 4, constants.shapes[4])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_L_shape_true(self):
        piece = Piece(5, 4, constants.shapes[5])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_T_shape_true(self):
        piece = Piece(5, 4, constants.shapes[6])
        grid = create_grid({(9, 1): piece.color})
        self.assertTrue(valid_space(piece, grid))

    def test_S_shape_false_block(self):
        piece = Piece(5, 4, constants.shapes[0])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))

    def test_Z_shape_false_block(self):
        piece = Piece(5, 4, constants.shapes[1])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))

    def test_I_shape_false_block(self):
        piece = Piece(5, 4, constants.shapes[2])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))

    def test_O_shape_false_block(self):
        piece = Piece(5, 4, constants.shapes[3])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))

    def test_J_shape_false_wall(self):
        piece = Piece(11, 4, constants.shapes[4])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))

    def test_L_shape_false_wall(self):
        piece = Piece(5, 22, constants.shapes[5])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))

    def test_T_shape_false_wall(self):
        piece = Piece(-1, 4, constants.shapes[6])
        grid = create_grid({(5, 3): piece.color})
        self.assertFalse(valid_space(piece, grid))


if __name__ == "__main__":
    unittest.main()
