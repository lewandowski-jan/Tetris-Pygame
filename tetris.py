# single block class in tetris game
class Block(object):
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

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


# single shape class in tetris game
class Shape(object):
    blocks = [4]

    def __init__(self, x, y, shape):
        if shape == "I":
            print("OK")
        elif shape == "L":
            print("OK")
        elif shape == "T":
            print("OK")
        elif shape == "O":
            print("OK")
        elif shape == "ML":
            print("OK")
        elif shape == "Z":
            print("OK")
        elif shape == "MZ":
            print("OK")
        else:
            print("Wrong shape type: " + shape)



