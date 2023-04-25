import unittest
from tetris.piece import Piece
from tetris import constants, convert_shape_format


class TestConvertShapeFormat(unittest.TestCase):
    def test_S_shape(self):
        piece = Piece(5, 0, constants.shapes[0])
        expected = [(5, -2), (6, -2), (4, -1), (5, -1)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)

    def test_Z_shape(self):
        piece = Piece(5, 0, constants.shapes[1])
        expected = [(4, -2), (5, -2), (5, -1), (6, -1)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)

    def test_I_shape(self):
        piece = Piece(5, 0, constants.shapes[2])
        expected = [(5, -4), (5, -3), (5, -2), (5, -1)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)

    def test_O_shape(self):
        piece = Piece(5, 0, constants.shapes[3])
        expected = [(4, -2), (5, -2), (4, -1), (5, -1)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)

    def test_J_shape(self):
        piece = Piece(5, 0, constants.shapes[4])
        expected = [(4, -3), (4, -2), (5, -2), (6, -2)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)

    def test_L_shape(self):
        piece = Piece(5, 0, constants.shapes[5])
        expected = [(6, -3), (4, -2), (5, -2), (6, -2)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)

    def test_T_shape(self):
        piece = Piece(5, 0, constants.shapes[6])
        expected = [(5, -3), (4, -2), (5, -2), (6, -2)]
        result = convert_shape_format(piece)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
