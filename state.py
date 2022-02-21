import pygame as pg


class State:
    # Handles hover, select, and click functionality
    def __init__(self, manager):
        self.manager = manager
        self.highlightable = []
        self.curr_hovered_obj = None
        self.curr_selected_radio = None

    def process_input(self, event):
        if self.curr_hovered_obj:
            self.curr_hovered_obj.hovered = False
        # Get object under mouse
        hovered_obj = self.get_obj_under_mouse()

        if hasattr(hovered_obj, 'hovered'):
            if self.curr_hovered_obj:
                self.curr_hovered_obj.hovered = False
            self.curr_hovered_obj = hovered_obj
            self.curr_hovered_obj.hovered = True

        if event.type == pg.MOUSEBUTTONDOWN and hasattr(hovered_obj, 'on_clicked'):
            hovered_obj.on_clicked()

            if hasattr(hovered_obj, 'type') and hovered_obj.type == 'radio':
                if hovered_obj.selected:
                    self.curr_selected_radio = hovered_obj

                elif self.curr_selected_radio:
                    self.curr_selected_radio.fill_color = None
                    self.curr_selected_radio.selected = False

                self.curr_selected_radio = hovered_obj
                self.curr_selected_radio.fill_color = (0, 0, 0)

    def get_obj_under_mouse(self):
        mouse_pos = pg.mouse.get_pos()

        for h in self.highlightable:
            if h.hitbox[0] <= mouse_pos[0] <= h.hitbox[1] and h.hitbox[2] <= mouse_pos[1] <= h.hitbox[3]:
                return h

    def update(self):
        pass

    def draw(self, screen):
        pass

    def deactivate(self):
        if self.curr_hovered_obj:
            self.curr_hovered_obj.hovered = False
        self.curr_hovered_obj = None
