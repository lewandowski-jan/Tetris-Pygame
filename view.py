import pygame as pg
import const
import tetris


class View(object):
    # constructor
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
        self.running = True

        # initialize pygame
        pg.init()
        # set window size to width and height
        self.screen = pg.display.set_mode((self.width, self.height))
        # set window name to name
        pg.display.set_caption(self.name)
        # set icon
        pg.display.set_icon(pg.image.load("tetris.png"))

    # sets screen width to value
    def set_width(self, width):
        self.width = width

    # returns screen width
    def get_width(self):
        return self.width

    # sets screen height to value
    def set_height(self, height):
        self.height = height

    # returns screen height
    def get_height(self):
        return self.height

    # sets screen name to value
    def set_name(self, name):
        self.name = name

    # returns screen name
    def get_name(self):
        return self.name

    # sets running to value
    def set_running(self, running):
        self.running = running

    # returns bool running
    def get_running(self):
        return self.running

    # clears screen
    def clear(self):
        self.screen.fill((0,0,0))

    # updates pygame display
    def update(self):
        pg.display.update()

    # checks for close event
    def check_close(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
