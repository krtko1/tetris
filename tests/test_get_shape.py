import unittest
from tetris.constants import shapes

from tetris import get_shape


class TestGetShape(unittest.TestCase):

    def test_piece_x(self):
        piece = get_shape()
        self.assertEqual(piece.x, 5)

    def test_piece_y(self):
        piece = get_shape()
        self.assertEqual(piece.y, 0)

    def test_piece_shape(self):
        piece = get_shape()
        self.assertTrue(piece.shape in shapes)


if __name__ == '__main__':
    unittest.main()
