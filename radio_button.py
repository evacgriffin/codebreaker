import pygame as pg


class RadioButton:
    # Dimensions
    radius = 15
    width = 2

    # Colors
    select_color = (0, 0, 0)
    text_color = (0, 0, 0)
    bg_color = (210, 180, 140)
    border_color = (105, 105, 105)
    fill_color = (0, 0, 0)

    # Radio group
    group = []

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.hitbox = [self.x - self.radius, self.x + self.radius, self.y - self.radius, self.y + self.radius,
                       self.x, self.y]

        self.font = pg.font.SysFont('Calibri', 30)
        self.text = self.font.render(text, True, self.text_color)
        text_x = self.x + 50
        text_y = self.y - 15
        self.text_pos = (text_x, text_y)

        self.enabled = True
        self.submitted = False
        self.hovered = False
        self.selected = False

    def on_clicked(self):
        for btn in self.group:
            if btn.selected:
                btn.selected = False

        self.selected = True
        self.on_selected()

    def draw(self, screen):
        if self.selected:
            pg.draw.circle(screen, self.fill_color, self.pos, self.radius)
        else:
            pg.draw.circle(screen, self.border_color, self.pos, self.radius, width=self.width)
        if (self.hovered or self.selected) and self.enabled:
            pg.draw.circle(screen, self.border_color, self.pos, self.radius + 2, 3)

        screen.blit(self.text, self.text_pos)
