from random import randrange
import const
import shapes


# single block class in tetris game
class Block(object):
    # constructor
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = const.GRID

    # sets x position to value
    def set_x(self, x):
        self.x = x

    # sets y position to value
    def set_y(self, y):
        self.y = y

    # returns x position
    def get_x(self):
        return self.x

    # returns y position
    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size


# single shape class in tetris game
class Shape(object):
    blocks = [4]

    def __init__(self, shape, x, y):
        self.x = x
        self.y = y

        if shape == "i":
            print("OK")
        elif shape == "l":
            print("OK")
        elif shape == "t":
            print("OK")
        elif shape == "o":
            print("OK")
        elif shape == "ml":
            print("OK")
        elif shape == "z":
            print("OK")
        elif shape == "mz":
            print("OK")
        else:
            print("Wrong shape type: " + shape)


class Board(object):
    board = [const.SIZE_X * const.SIZE_Y]
    shapes = [4]

    def __init__(self):
        for i in range(const.SIZE_X):
            for j in range(const.SIZE_Y):
                self.board[i + j * const.SIZE_Y] = 0

    def update(self):
        while len(self.shapes) < 4:
            pass

