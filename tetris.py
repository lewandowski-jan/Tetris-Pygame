from random import randrange
import const
import shapes


# single block class in tetris game
class Block(object):
    # constructor
    def __init__(self, x, y, color):
        self.x = x + 1
        self.y = y
        self.color = color
        self.size = const.GRID - 1

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
    blocks = []

    def get_blocks(self):
        return self.blocks

    def __init__(self, shape, x, y):
        self.x = x
        self.y = y
        self.array = []
        self.color = (0, 0, 0)

        if shape == 0:
            self.array = shapes.i
            self.color = const.LIGHTBLUE
        elif shape == 1:
            self.array = shapes.l
            self.color = const.BLUE
        elif shape == 2:
            self.array = shapes.t
            self.color = const.PURPLE
        elif shape == 3:
            self.array = shapes.o
            self.color = const.YELLOW
        elif shape == 4:
            self.array = shapes.ml
            self.color = const.ORANGE
        elif shape == 5:
            self.array = shapes.z
            self.color = const.GREEN
        elif shape == 6:
            self.array = shapes.mz
            self.color = const.RED
        else:
            print("Wrong shape type: " + shape)

        for i in range(4):
            for j in range(4):
                if self.array[0][i * 4 + j] == 1:
                    self.blocks.append(Block(self.x + j * const.GRID, self.y + i * const.GRID, self.color))


class Board(object):
    board = []
    shapes = []

    def __init__(self):
        for i in range(const.SIZE_X):
            for j in range(const.SIZE_Y):
                self.board.append(0)

    def get_shapes(self):
        return self.shapes

    def update(self):
        while len(self.shapes) < 4:
            num = randrange(0, 6)
            randx = randrange(0, 10)
            randy = randrange(0, 20)
            self.shapes.append(Shape(num, randx * const.GRID - const.GRID * 1, randy * const.GRID - const.GRID * 1))


