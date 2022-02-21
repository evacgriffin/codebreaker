import pygame as pg


class Pin:

    radius = 15
    x = 25
    border_color = (105, 105, 105)

    def __init__(self, y, color):
        self.y = 50 + y * 100
        self.pos = (self.x, self.y)
        self.color = color
        self.hitbox = [25 - self.radius, 25 + self.radius, self.y - self.radius, self.y + self.radius]
        self.hovered = False
        self.selected = False

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.radius)
        if self.hovered or self.selected:
            pg.draw.circle(screen, self.border_color, self.pos, self.radius + 2, 3)
