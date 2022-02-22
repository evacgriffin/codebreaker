from menu import Menu
from button import Button


class EndGame(Menu):
    def __init__(self, manager, text, difficulty):
        Menu.__init__(self, manager)
        self.difficulty = difficulty

        # Header
        self.head = text
        self.head_img = self.header_font.render(self.head, True, self.txt_color)
        head_img_size = self.head_img.get_size()
        head_img_center = (head_img_size[0] / 2, head_img_size[1] / 2)
        head_img_x = self.rect_center[0] - head_img_center[0]
        head_img_y = self.y + 100
        self.head_img_pos = (head_img_x, head_img_y)

        # Buttons
        self.replay_btn = Button(self.x + 10, self.y + self.height - 50, self.header_font, 'Replay')
        self.menu_btn = Button(self.x + self.width - 140, self.y + self.height - 50, self.header_font, 'Menu')

        # Highlightable objects
        self.highlightable.append(self.replay_btn)
        self.highlightable.append(self.menu_btn)

        # On-clicked property
        self.replay_btn.on_clicked = self.on_replay_btn_clicked
        self.menu_btn.on_clicked = self.on_menu_btn_clicked

    def on_replay_btn_clicked(self):
        # Starts new game with same difficulty
        from gameplay import Gameplay
        self.manager.pop()
        self.manager.push(Gameplay(self.manager, self.difficulty))

    def on_menu_btn_clicked(self):
        # Resets game, opens up main menu
        from main_menu import MainMenu
        self.manager.clear()
        self.manager.push(MainMenu(self.manager))

    def process_input(self, event):
        Menu.process_input(self, event)

    def draw(self, screen):
        Menu.draw(self, screen)
        screen.blit(self.head_img, self.head_img_pos)

        for obj in self.highlightable:
            obj.draw(screen)
