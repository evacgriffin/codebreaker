import pygame as pg


class Button:

    # Dimensions
    width = 130
    height = 30
    radius = 10

    # Colors
    btn_color = (211, 211, 211)
    txt_color = (0, 0, 0)
    disabled_txt_color = (169, 169, 169)
    border_color = (105, 105, 105)

    def __init__(self, x, y, font, text):
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, self.width, self.height)
        rect_center = (self.width/2 + x, self.height/2 + y)
        self.font = font
        self.text = text
        self.enabled_img = self.font.render(self.text, True, self.txt_color)
        self.disabled_img = self.font.render(self.text, True, self.disabled_txt_color)
        img_size = self.enabled_img.get_size()
        img_center = (img_size[0]/2, img_size[1]/2)
        img_x = rect_center[0] - img_center[0]
        img_y = rect_center[1] - img_center[1]
        self.img_pos = (img_x, img_y)
        self.hitbox = [x, x + self.width, y, y + self.height]
        self.enabled = True
        self.hovered = False
        self.selected = False

    def draw(self, screen):
        pg.draw.rect(screen, self.btn_color, self.rect, border_radius=self.radius)
        if self.enabled:
            screen.blit(self.enabled_img, self.img_pos)
        else:
            screen.blit(self.disabled_img, self.img_pos)

        if (self.hovered or self.selected) and self.enabled:
            outline = [self.x - 2, self.y - 2, self.width + 2, self.height + 2]
            pg.draw.rect(screen, self.border_color, outline, width=3, border_radius=self.radius)
            