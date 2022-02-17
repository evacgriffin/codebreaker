import pygame as pg
from menu import Menu
from gameplay import Gameplay
from button import Button


class MainMenu(Menu):
    def __init__(self, manager, is_paused):
        Menu.__init__(self, manager)
        self.is_paused = is_paused

        self.text = 'MAIN MENU'
        self.img = self.font.render(self.text, True, self.txt_color)
        img_size = self.img.get_size()
        img_center = (img_size[0] / 2, img_size[1] / 2)
        img_x = self.rect_center[0] - img_center[0]
        img_y = self.y + 25
        self.img_pos = (img_x, img_y)

        # Buttons
        self.difficulty_btn = Button(self.x + 85, self.y + 100, self.font, 'Difficulty')
        self.rules_btn = Button(self.x + 85, self.y + 150, self.font, 'Rules')
        self.start_btn = Button(self.x + 85, self.y + 200, self.font, 'Start')
        self.resume_btn = Button(self.x + 85, self.y + 250, self.font, 'Resume')
        self.resume_btn.enabled = False
        self.reset_btn = Button(self.x + 85, self.y + 300, self.font, 'Reset')
        self.reset_btn.enabled = False

        # Highlightable objects
        self.highlightable.append(self.difficulty_btn)
        self.highlightable.append(self.rules_btn)
        self.highlightable.append(self.start_btn)
        self.highlightable.append(self.resume_btn)
        self.highlightable.append(self.reset_btn)

        # On-clicked property
        self.start_btn.on_clicked = self.on_start_btn_clicked


    def on_start_btn_clicked(self):
        self.manager.pop()
        if not self.is_paused:
            self.manager.push(Gameplay(self.manager))

    def process_input(self, event):
        Menu.process_input(self, event)

        # Additional input processing (handle button clicks)

    def draw(self, screen):
        Menu.draw(self, screen)
        screen.blit(self.img, self.img_pos)

        for obj in self.highlightable:
            obj.draw(screen)
