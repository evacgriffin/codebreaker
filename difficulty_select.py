from menu import Menu


class DifficultySelect(Menu):
    def __init__(self, manager, is_paused):
        Menu.__init__(self, manager)
        self.is_paused = is_paused
