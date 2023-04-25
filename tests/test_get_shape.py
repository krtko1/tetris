import unittest

from tetris import get_piece
from tetris.constants import shapes


class TestGetShape(unittest.TestCase):
    def test_piece_x(self):
        piece = get_piece()
        self.assertEqual(piece.x, 5)

    def test_piece_y(self):
        piece = get_piece()
        self.assertEqual(piece.y, 0)

    def test_piece_shape(self):
        piece = get_piece()
        self.assertTrue(piece.shape in shapes)


if __name__ == "__main__":
    unittest.main()
