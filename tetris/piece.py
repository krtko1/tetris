from tetris import constants


class Piece(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = constants.shape_colors[constants.shapes.index(shape)]
        self.rotation = 0  # number from 0-3
