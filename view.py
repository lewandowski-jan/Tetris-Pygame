import pygame as pg
import const
import tetris
import button

class View(object):
    # constructor
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
        self.running = True
        self.mouseDown = False
        self.mouseUp = True
        self.isPaused = False
        self.clicked = False

        # initialize pygame
        pg.init()
        # set window size to width and height
        self.screen = pg.display.set_mode((self.width, self.height))
        # set window name to name
        pg.display.set_caption(self.name)
        # set icon
        pg.display.set_icon(pg.image.load("tetris.png"))
        # set font and text
        self.font = pg.font.Font('Minecrafter.Reg.ttf', 64)
        self.text = self.font.render("Tetris", True, const.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (600, 45)
        self.but = button.Button(480, 100, 240, 80, "PLAY")
        self.font40 = pg.font.Font('Minecrafter.Reg.ttf', 40)

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

    # sets isPaused to value
    def change_isPaused(self):
        if self.isPaused:
            self.isPaused = False
        else:
            self.isPaused = True

    # clears screen
    def clear(self):
        self.screen.fill((200,200,200))

    # updates pygame display
    def update(self):
        pg.display.update()

    # checks for close event
    def check_close(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.mouseDown = True
                self.mouseUp = False
            elif event.type == pg.MOUSEBUTTONUP:
                self.mouseDown = False
                self.mouseUp = True

    # draws ui
    def ui(self):
        for i in range(10):
            for j in range(20):
                rect = pg.Rect(1 + i * const.GRID, j * const.GRID, const.GRID - 1, const.GRID - 1)
                pg.draw.rect(self.screen, const.BLACK, rect)

        self.screen.blit(self.text, self.textRect)

        if self.but.update(self.screen, self.isPaused, self.mouseDown) and not self.clicked:
            self.change_isPaused()
            self.clicked = True

        if self.mouseUp:
            self.clicked = False

        nexttext = self.font40.render("next shape", True, const.BLACK)
        nexttextrect = nexttext.get_rect()
        nexttextrect.center = (600, 240)
        self.screen.blit(nexttext, nexttextrect)

        for i in range(3):
            rect = pg.Rect(480, 260 + i * 180, 240, 160)
            pg.draw.rect(self.screen, const.BLACK, rect)