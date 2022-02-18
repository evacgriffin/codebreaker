from menu import Menu
from button import Button


class DifficultySelect(Menu):
    def __init__(self, manager, is_paused):
        Menu.__init__(self, manager)
        self.is_paused = is_paused

        self.text = 'SELECT DIFFICULTY'
        self.img = self.font.render(self.text, True, self.txt_color)
        img_size = self.img.get_size()
        img_center = (img_size[0] / 2, img_size[1] / 2)
        img_x = self.rect_center[0] - img_center[0]
        img_y = self.y + 25
        self.img_pos = (img_x, img_y)

        # Buttons
        self.back_btn = Button(self.x + self.width - 210, self.y + 250, self.font, 'Back')
        self.start_btn = Button(self.x + self.width - 210, self.y + 300, self.font, 'Start')
        self.back_btn.on_clicked = self.on_back_btn_clicked
        self.start_btn.on_clicked = self.on_start_btn_clicked

        # Highlightable objects
        self.highlightable.append(self.back_btn)
        self.highlightable.append(self.start_btn)

    def on_back_btn_clicked(self):
        self.manager.pop()

    def on_start_btn_clicked(self):
        pass

    def draw(self, screen):
        Menu.draw(self, screen)
        screen.blit(self.img, self.img_pos)

        for obj in self.highlightable:
            obj.draw(screen)
