import pygame as pg


class Pin:
    # Dimensions
    radius = 15
    x = 25

    # Colors
    border_color = (105, 105, 105)

    # Pin group
    group = []

    def __init__(self, y, color):
        self.y = 50 + y * 100
        self.pos = (self.x, self.y)
        self.color = color
        self.hitbox = [25 - self.radius, 25 + self.radius, self.y - self.radius, self.y + self.radius]
        self.hovered = False
        self.selected = False

    def on_clicked(self):
        for p in self.group:
            if p.selected:
                p.selected = False

        self.selected = True

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.radius)
        if self.hovered or self.selected:
            pg.draw.circle(screen, self.border_color, self.pos, self.radius + 2, 3)
