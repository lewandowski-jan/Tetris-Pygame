from random import randrange
import const
import shapes

count = 0


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
    def get_blocks(self):
        return self.blocks

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_shape(self):
        return self.shape

    def __init__(self, shape, x, y):
        self.x = x
        self.y = y
        self.array = []
        self.color = (0, 0, 0)
        self.blocks = []
        self.turnpossible = True
        self.spin = 0
        self.shape = shape

        if self.shape == 0:
            self.array = shapes.i
            self.color = const.LIGHTBLUE
        elif self.shape == 1:
            self.array = shapes.l
            self.color = const.BLUE
        elif self.shape == 2:
            self.array = shapes.t
            self.color = const.PURPLE
        elif self.shape == 3:
            self.array = shapes.o
            self.color = const.YELLOW
        elif self.shape == 4:
            self.array = shapes.ml
            self.color = const.ORANGE
        elif self.shape == 5:
            self.array = shapes.z
            self.color = const.GREEN
        elif self.shape == 6:
            self.array = shapes.mz
            self.color = const.RED
        else:
            print("Wrong shape type: " + shape)

        for i in range(4):
            for j in range(4):
                if self.array[0][i * 4 + j] == 1:
                    self.blocks.append(Block(self.x + j * const.GRID, self.y + i * const.GRID, self.color))

    def turn(self):
        temp = []
        for i in range(4):
            for j in range(4):
                if self.spin < 3:
                    if self.array[self.spin + 1][i * 4 + j] == 1:
                        temp.append(Block(self.x + j * const.GRID, self.y + i * const.GRID, self.color))
                else:
                    if self.array[0][i * 4 + j] == 1:
                        temp.append(Block(self.x + j * const.GRID, self.y + i * const.GRID, self.color))

        for block in temp:
            if block.get_x() <= 0 or block.get_x() >= 362:
                self.turnpossible = False
                break
            else:
                self.turnpossible = True

        temp.clear()

        if self.turnpossible:
            if self.spin < 3:
                self.spin += 1
                self.blocks.clear()
                for i in range(4):
                    for j in range(4):
                        if self.array[self.spin][i * 4 + j] == 1:
                            self.blocks.append(Block(self.x + j * const.GRID, self.y + i * const.GRID, self.color))
            else:
                self.spin = 0
                self.blocks.clear()
                for i in range(4):
                    for j in range(4):
                        if self.array[self.spin][i * 4 + j] == 1:
                            self.blocks.append(Block(self.x + j * const.GRID, self.y + i * const.GRID, self.color))


class Board(object):
    shapesnums = [None] * 4

    def __init__(self):

        self.shapes = []
        self.board = []
        self.pressed = False
        self.possibleleft = True
        self.possibleright = True
        self.possibledown = True
        self.lastIndexes = [0, 0, 0, 0]
        self.lastshape = 0
        self.score = 0
        self.touched = False

        for i in range(const.SIZE_Y * const.SIZE_X):
            self.board.append(-1)

        while len(self.shapes) < 4:
            num = randrange(0, 7)
            if len(self.shapes) == 0:
                self.shapesnums[0] = num
                self.shapes.append(Shape(self.shapesnums[0], 120, 0))
            elif len(self.shapes) == 1:
                self.shapesnums[1] = num
                self.shapes.append(Shape(self.shapesnums[1], 520, 240))
            elif len(self.shapes) == 2:
                self.shapesnums[2] = num
                self.shapes.append(Shape(self.shapesnums[2], 520, 420))
            elif len(self.shapes) == 3:
                self.shapesnums[3] = num
                self.shapes.append(Shape(self.shapesnums[3], 520, 600))

    #restarts game
    def restart(self):
        self.shapes = []
        self.board = []
        self.pressed = False
        self.possibleleft = True
        self.possibleright = True
        self.possibledown = True
        self.lastIndexes = [0, 0, 0, 0]
        self.lastshape = 0
        self.score = 0
        self.Touched = False

        for i in range(const.SIZE_Y * const.SIZE_X):
            self.board.append(-1)

        while len(self.shapes) < 4:
            num = randrange(0, 7)
            if len(self.shapes) == 0:
                self.shapesnums[0] = num
                self.shapes.append(Shape(self.shapesnums[0], 120, 0))
            elif len(self.shapes) == 1:
                self.shapesnums[1] = num
                self.shapes.append(Shape(self.shapesnums[1], 520, 240))
            elif len(self.shapes) == 2:
                self.shapesnums[2] = num
                self.shapes.append(Shape(self.shapesnums[2], 520, 420))
            elif len(self.shapes) == 3:
                self.shapesnums[3] = num
                self.shapes.append(Shape(self.shapesnums[3], 520, 600))

    # returns score
    def get_score(self):
        return self.score

    #returns list of shapes
    def get_shapes(self):
        return self.shapes

    # returns board list
    def get_board(self):
        return self.board

    # clears the board from 7s which means moving shape
    def clear_board7(self):
        for i in range(const.SIZE_X):
            for j in range(const.SIZE_Y):
                if self.board[j * const.SIZE_X + i] == 7:
                    self.board[j * const.SIZE_X + i] = -1

    # saves last position of moving shape
    def update_last(self):
        self.lastIndexes[0] = int((self.shapes[0].get_blocks()[0].get_y() / const.GRID) * const.SIZE_X + (
                self.shapes[0].get_blocks()[0].get_x() - 1) / const.GRID)
        self.lastIndexes[1] = int((self.shapes[0].get_blocks()[1].get_y() / const.GRID) * const.SIZE_X + (
                self.shapes[0].get_blocks()[1].get_x() - 1) / const.GRID)
        self.lastIndexes[2] = int((self.shapes[0].get_blocks()[2].get_y() / const.GRID) * const.SIZE_X + (
                self.shapes[0].get_blocks()[2].get_x() - 1) / const.GRID)
        self.lastIndexes[3] = int((self.shapes[0].get_blocks()[3].get_y() / const.GRID) * const.SIZE_X + (
                self.shapes[0].get_blocks()[3].get_x() - 1) / const.GRID)

        self.lastshape = self.shapes[0].get_shape()

    # deletes row at given index
    def delete_row(self, index):
        for i in range(const.SIZE_X):
            self.board[index * const.SIZE_X + i] = -1

        while index > 0:
            for i in range(const.SIZE_X):
                if self.board[index * const.SIZE_X + i] != 7:
                    self.board[index * const.SIZE_X + i], self.board[(index - 1) * const.SIZE_X + i] = self.board[(index - 1) * const.SIZE_X + i], self.board[index * const.SIZE_X + i]
            index -= 1

    # updates board with moving shape, places shape in board if it hit something and returns True if so else False
    def update_board(self):
        self.clear_board7()

        for block in self.shapes[0].get_blocks():
            index = int((block.get_y() / const.GRID) * const.SIZE_X + (block.get_x() - 1) / const.GRID)
            if 0 <= index < const.SIZE_X * const.SIZE_Y:
                if self.board[index] == -1:
                    self.board[index] = 7
                else:
                    for ind in self.lastIndexes:
                        self.board[ind] = self.lastshape

                    self.shapes.clear()
                    self.shapesnums.pop(0)
                    self.shapesnums.append(randrange(0, 7))
                    self.shapes.append(Shape(self.shapesnums[0], 120, -160))
                    self.shapes.append(Shape(self.shapesnums[1], 520, 240))
                    self.shapes.append(Shape(self.shapesnums[2], 520, 420))
                    self.shapes.append(Shape(self.shapesnums[3], 520, 600))
                    self.score += 100
                    return True
                    break
        return False

    # checks if block hits ground
    def check_ground(self):
        for block in self.shapes[0].get_blocks():

            # when shape hits ground
            if block.get_y() == const.WIN_HEIGHT - const.GRID:

                for i in range(const.SIZE_X):
                    for j in range(const.SIZE_Y):
                        if self.board[j * const.SIZE_X + i] == 7:
                            self.board[j * const.SIZE_X + i] = self.shapes[0].get_shape()

                self.shapes.clear()
                self.shapesnums.pop(0)
                self.shapesnums.append(randrange(0, 7))
                self.shapes.append(Shape(self.shapesnums[0], 120, -160))
                self.shapes.append(Shape(self.shapesnums[1], 520, 240))
                self.shapes.append(Shape(self.shapesnums[2], 520, 420))
                self.shapes.append(Shape(self.shapesnums[3], 520, 600))
                self.score += 100

                break

    def check_row(self):
        for j in range(const.SIZE_Y):
            check = True
            for i in range(const.SIZE_X):
                ind = j * const.SIZE_X + i
                if self.board[ind] == -1:
                    check = False
                if self.board[ind] == 7:
                    check = False
            if check:
                self.delete_row(j)
                self.score += 1000

    def update(self, isPaused, keyu, keyup, keyl, keyr, keyd):

        if not isPaused:
            self.update_last()
            self.update_board()
            self.check_ground()

            for i in range(9):
                if self.board[i] != -1 and self.board[i] != 7:
                    return False

            for block in self.shapes[0].get_blocks():
                if block.get_x() <= 1:
                    self.possibleleft = False
                    break
                else:
                    self.possibleleft = True

            for block in self.shapes[0].get_blocks():
                if block.get_x() >= 361:
                    self.possibleright = False
                    break
                else:
                    self.possibleright = True

            for block in self.shapes[0].get_blocks():
                if block.get_y() >= const.WIN_HEIGHT - const.GRID:
                    self.possibledown = False
                    break
                else:
                    self.possibledown = True

            self.update_last()

            if keyu and not self.pressed:
                self.shapes[0].turn()
                self.pressed = True

            if keyl and not self.pressed and self.possibleleft:
                for block in self.shapes[0].get_blocks():
                    block.set_x(block.get_x() - const.GRID)
                self.shapes[0].set_x(self.shapes[0].get_x() - const.GRID)
                self.pressed = True

            if keyr and not self.pressed and self.possibleright:
                for block in self.shapes[0].get_blocks():
                    block.set_x(block.get_x() + const.GRID)
                self.shapes[0].set_x(self.shapes[0].get_x() + const.GRID)
                self.pressed = True

            if keyd and not self.pressed and self.possibledown:
                for block in self.shapes[0].get_blocks():
                    block.set_y(block.get_y() + const.GRID)
                self.shapes[0].set_y(self.shapes[0].get_y() + const.GRID)
                self.pressed = True

            if keyup:
                self.pressed = False

            self.update_board()
            self.check_ground()

            global count
            count += 1

            if count >= const.FPS/4:
                # moves shape one lower
                for block in self.shapes[0].get_blocks():
                    block.set_y(block.get_y() + const.GRID)
                self.shapes[0].set_y(self.shapes[0].get_y() + const.GRID)

                self.check_row()

                count = 0

                self.update_board()

        return True
