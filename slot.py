import pygame as pg


class Slot:
    # Dimensions
    radius = 15
    width = 2

    # Colors
    bg_color = (210, 180, 140)
    border_color = (105, 105, 105)
    color = None

    type = 'slot'

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.pos = (81.25 + self.x * 62.50, 25 + self.y * 50)
        self.hitbox = [81.25 + self.x * 62.50 - self.radius, 81.25 + self.x * 62.50 + self.radius,
                       25 + self.y * 50 - self.radius, 25 + self.y * 50 + self.radius, self.x, self.y]

        self.enabled = False
        self.submitted = False
        self.hovered = False
        self.selected = False

    def draw(self, screen):
        if self.color:
            pg.draw.circle(screen, self.color, self.pos, self.radius)
        else:
            pg.draw.circle(screen, self.border_color, self.pos, self.radius, width=self.width)
        if (self.hovered or self.selected) and self.enabled:
            pg.draw.circle(screen, self.border_color, self.pos, self.radius + 2, 3)
