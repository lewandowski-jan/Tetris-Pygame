import pygame as pg
import const
import tetris


class View(object):
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
        self.running = True

        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.name)
        pg.display.set_icon(pg.image.load("tetris.png"))

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_running(self, running):
        self.running = running

    def get_running(self):
        return self.running

    def clear(self):
        self.screen.fill((0,0,0))

    def update(self):
        pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
