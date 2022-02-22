from menu import Menu
from button import Button
from rules import Rules


class PauseMenu(Menu):
    def __init__(self, manager, is_paused):
        Menu.__init__(self, manager)
        self.is_paused = is_paused

        self.text = 'PAUSED'
        self.img = self.header_font.render(self.text, True, self.txt_color)
        img_size = self.img.get_size()
        img_center = (img_size[0] / 2, img_size[1] / 2)
        img_x = self.rect_center[0] - img_center[0]
        img_y = self.y + 25
        self.img_pos = (img_x, img_y)

        # Buttons
        self.rules_btn = Button(self.x + 85, self.y + 150, self.header_font, 'Rules')
        self.resume_btn = Button(self.x + 85, self.y + 200, self.header_font, 'Resume')
        self.reset_btn = Button(self.x + 85, self.y + 250, self.header_font, 'Reset')

        # Highlightable objects
        self.highlightable.append(self.rules_btn)
        self.highlightable.append(self.resume_btn)
        self.highlightable.append(self.reset_btn)

        # On-clicked property
        self.rules_btn.on_clicked = self.on_rules_btn_clicked
        self.resume_btn.on_clicked = self.on_resume_btn_clicked
        self.reset_btn.on_clicked = self.on_reset_btn_clicked

    def on_rules_btn_clicked(self):
        self.manager.push(Rules(self.manager))

    def on_resume_btn_clicked(self):
        self.manager.pop()

    def on_reset_btn_clicked(self):
        from main_menu import MainMenu
        self.manager.clear()
        self.manager.push(MainMenu(self.manager))

    def process_input(self, event):
        Menu.process_input(self, event)

        # Additional input processing (handle button clicks)

    def draw(self, screen):
        Menu.draw(self, screen)
        screen.blit(self.img, self.img_pos)

        for obj in self.highlightable:
            obj.draw(screen)
