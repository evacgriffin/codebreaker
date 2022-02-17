import pygame as pg
from state import State


class Menu(State):
    # Dimensions
    x = 25
    y = 50
    width = 300
    height = 355
    radius = 10
    border_width = 3

    # Colors
    bg_color = (210, 180, 140)
    txt_color = (0, 0, 0)
    border_color = (105, 105, 105)

    def __init__(self, manager):
        State.__init__(self, manager)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.rect_center = (self.width / 2 + self.x, self.height / 2 + self.y)
        self.font = pg.font.SysFont('Calibri', 30)
        self.outline = [self.x - 2, self.y - 2, self.width + 2, self.height + 2]

    def draw(self, screen):
        # Draw menu base appearance
        pg.draw.rect(screen, self.bg_color, self.rect, border_radius=self.radius)
        pg.draw.rect(screen, self.border_color, self.outline, width=self.border_width, border_radius=self.radius)
