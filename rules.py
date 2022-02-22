import pygame as pg
from menu import Menu
from button import Button


class Rules(Menu):
    def __init__(self, manager, is_paused):
        Menu.__init__(self, manager)
        self.is_paused = is_paused

        self.text = "Goal: Correctly guess the randomly generated color code.\n" \
                    "Difficulties: Easy - 12 attempts, no repeat colors\n" \
                    "Normal - 12 attempts, repeat colors allowed\n" \
                    "Hard - 8 attempts, repeat colors allowed\n" \
                    "After each turn, a hint will be displayed. A black dot appears for each color guess that is "\
                    "both correct in color and position. A white dot appears if a color " \
                    "was guessed correctly but was placed in the wrong position." \

        self.rules_font = pg.font.SysFont('Calibri', 20)
        self.font_height = self.rules_font.size(self.text)
        self.box_top = self.rect.top
        self.box_bottom = self.rect.bottom

        # Buttons
        self.highlightable = []
        self.back_btn = Button(self.x + 85, self.y + 310, self.header_font, 'Back')
        self.highlightable.append(self.back_btn)
        self.back_btn.on_clicked = self.on_back_btn_clicked

    def on_back_btn_clicked(self):
        self.manager.pop()

    def draw(self, screen):
        Menu.draw(self, screen)

        words = [word.split(' ') for word in self.text.splitlines()]
        space = self.rules_font.size(' ')[0]
        max_width, max_height = self.width, self.height
        x = self.x
        y = self.y
        pos = (x, y)
        for line in words:
            for word in line:
                word_surface = self.rules_font.render(word, 0, self.txt_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

        self.back_btn.draw(screen)
