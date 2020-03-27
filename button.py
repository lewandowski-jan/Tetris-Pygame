import pygame as pg
import const

class Button(object):
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = (100, 100, 100)
        self.font = pg.font.Font('Minecrafter.Reg.ttf', 40)
        self.text = self.font.render("PLAY", True, const.BLACK)
        self.textRect = self.text.get_rect()

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def update(self, screen, ispaused, mousedown):
        pg.draw.rect(screen, self.color, self.rect)
        (mx, my) = pg.mouse.get_pos()

        if not ispaused:
            self.color = (100, 100, 100)
            self.text = self.font.render("PAUSE", True, const.BLACK)
        else:
            self.color = (140, 140, 140)
            self.text = self.font.render("PLAY", True, const.BLACK)

        self.textRect = self.text.get_rect()
        self.textRect.center = (600, 125)
        screen.blit(self.text, self.textRect)

        if self.x <= mx <= self.x + self.width and self.y <= my <= self.y + self.height and mousedown:
            return True
