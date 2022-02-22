from menu import Menu
from button import Button
from radio_button import RadioButton
from gameplay import Gameplay


class DifficultySelect(Menu):
    # Default difficulty: normal
    difficulty = 1

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

        # Radio Buttons
        radio_x = 100
        self.easy_rad = RadioButton(radio_x, 150, 'Easy')
        self.normal_rad = RadioButton(radio_x, 200, 'Normal')
        self.normal_rad.selected = True
        self.normal_rad.fill_color = (0, 0, 0)
        self.hard_rad = RadioButton(radio_x, 250, 'Hard')
        self.easy_rad.on_clicked = self.on_easy_clicked
        self.normal_rad.on_clicked = self.on_normal_clicked
        self.hard_rad.on_clicked = self.on_hard_clicked

        # Buttons
        self.back_btn = Button(self.x + self.width - 210, self.y + 250, self.font, 'Back')
        self.start_btn = Button(self.x + self.width - 210, self.y + 300, self.font, 'Start')
        self.start_btn.enabled = False
        self.back_btn.on_clicked = self.on_back_btn_clicked
        self.start_btn.on_clicked = self.on_start_btn_clicked

        # Highlightable objects
        self.highlightable.append(self.easy_rad)
        self.highlightable.append(self.normal_rad)
        self.highlightable.append(self.hard_rad)
        self.highlightable.append(self.back_btn)
        self.highlightable.append(self.start_btn)

    def on_back_btn_clicked(self):
        self.manager.pop()

    def on_start_btn_clicked(self):
        self.manager.pop()
        self.manager.push(Gameplay(self.manager))

    def on_easy_clicked(self):
        self.difficulty = 0

    def on_normal_clicked(self):
        self.difficulty = 1

    def on_hard_clicked(self):
        self.difficulty = 2

    def draw(self, screen):
        Menu.draw(self, screen)
        screen.blit(self.img, self.img_pos)

        for obj in self.highlightable:
            obj.draw(screen)
