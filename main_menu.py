from menu import Menu
from button import Button
from radio_button import RadioButton
from rules import Rules
from gameplay import Gameplay
from gameplay import Difficulty


class MainMenu(Menu):
    # Default difficulty: normal
    difficulty = 1

    def __init__(self, manager, is_paused):
        Menu.__init__(self, manager)
        self.is_paused = is_paused

        # Header
        self.head = 'MAIN MENU'
        self.head_img = self.header_font.render(self.head, True, self.txt_color)
        head_img_size = self.head_img.get_size()
        head_img_center = (head_img_size[0] / 2, head_img_size[1] / 2)
        head_img_x = self.rect_center[0] - head_img_center[0]
        head_img_y = self.y + 15
        self.head_img_pos = (head_img_x, head_img_y)

        # Subtitle
        self.sub = 'Please select a difficulty'
        self.sub_img = self.sub_font.render(self.sub, True, self.txt_color)
        sub_img_size = self.sub_img.get_size()
        sub_img_center = (sub_img_size[0] / 2, sub_img_size[1] / 2)
        sub_img_x = self.rect_center[0] - sub_img_center[0]
        sub_img_y = self.y + 50
        self.sub_img_pos = (sub_img_x, sub_img_y)

        # Radio Buttons
        self.easy_rad = RadioButton(self.x + 80, 175, 'Easy')
        self.normal_rad = RadioButton(self.x + 80, 225, 'Normal')
        self.normal_rad.selected = True
        self.normal_rad.fill_color = (0, 0, 0)
        self.hard_rad = RadioButton(self.x + 80, 275, 'Hard')
        self.easy_rad.on_clicked = self.on_easy_clicked
        self.normal_rad.on_clicked = self.on_normal_clicked
        self.hard_rad.on_clicked = self.on_hard_clicked

        # Buttons
        self.rules_btn = Button(self.x + 10, self.y + self.height - 50, self.header_font, 'Rules')
        self.start_btn = Button(self.x + self.width - 140, self.y + self.height - 50, self.header_font, 'Start')

        # Highlightable objects
        self.highlightable.append(self.rules_btn)
        self.highlightable.append(self.start_btn)
        self.highlightable.append(self.easy_rad)
        self.highlightable.append(self.normal_rad)
        self.highlightable.append(self.hard_rad)

        # On-clicked property
        self.rules_btn.on_clicked = self.on_rules_btn_clicked
        self.start_btn.on_clicked = self.on_start_btn_clicked
        self.easy_rad.on_clicked = self.on_easy_clicked
        self.normal_rad.on_clicked = self.on_normal_clicked
        self.hard_rad.on_clicked = self.on_hard_clicked

    def on_easy_clicked(self):
        self.difficulty = Difficulty.EASY

    def on_normal_clicked(self):
        self.difficulty = Difficulty.NORMAL

    def on_hard_clicked(self):
        self.difficulty = Difficulty.HARD

    def on_rules_btn_clicked(self):
        self.manager.push(Rules(self.manager, False))

    def on_start_btn_clicked(self):
        self.manager.pop()
        self.manager.push(Gameplay(self.manager, self.difficulty))

    def process_input(self, event):
        Menu.process_input(self, event)

    def draw(self, screen):
        Menu.draw(self, screen)
        screen.blit(self.head_img, self.head_img_pos)
        screen.blit(self.sub_img, self.sub_img_pos)

        for obj in self.highlightable:
            obj.draw(screen)
