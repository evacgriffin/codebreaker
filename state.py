import pygame as pg


class State:
    # Handles hover, select, and click functionality
    def __init__(self, manager):
        self.manager = manager
        self.highlightable = []
        self.curr_hovered_obj = None
        self.curr_selected_obj = None
        self.curr_selected_slot = None
        self.curr_selected_pin = None

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

        # QUESTION: Put the code specific to buttons/radio buttons in main_menu?
        if event.type == pg.MOUSEBUTTONDOWN:
            if hasattr(hovered_obj, 'on_clicked'):
                if hasattr(hovered_obj, 'type') and hovered_obj.type == 'radio':
                    for h in self.highlightable:
                        if hasattr(h, 'selected') and h.selected:
                            self.curr_selected_obj = h

                    if hovered_obj.selected:
                        self.curr_selected_obj = hovered_obj

                    elif self.curr_selected_obj:
                        self.curr_selected_obj.fill_color = None
                        self.curr_selected_obj.selected = False

                    self.curr_selected_obj = hovered_obj
                    self.curr_selected_obj.fill_color = (0, 0, 0)

                hovered_obj.on_clicked()

            if hasattr(hovered_obj, 'type') and hovered_obj.type == 'slot' and hovered_obj.enabled:
                if self.curr_selected_slot:
                    self.curr_selected_slot.selected = False
                # Get object under mouse
                hovered_obj = self.get_obj_under_mouse()

                if hasattr(hovered_obj, 'selected'):
                    if self.curr_selected_slot:
                        self.curr_selected_slot.selected = False
                    self.curr_selected_slot = hovered_obj
                    self.curr_selected_slot.selected = True

            if hasattr(hovered_obj, 'type') and hovered_obj.type == 'pin':
                if self.curr_selected_pin:
                    self.curr_selected_pin.selected = False
                # Get object under mouse
                hovered_obj = self.get_obj_under_mouse()

                if hasattr(hovered_obj, 'selected'):
                    if self.curr_selected_pin:
                        self.curr_selected_pin.selected = False
                    self.curr_selected_pin = hovered_obj
                    self.curr_selected_pin.selected = True

            if (self.curr_selected_pin and self.curr_selected_slot) and self.curr_selected_slot.enabled:
                self.curr_selected_slot.color = self.curr_selected_pin.color
                self.curr_selected_slot.selected = False
                self.curr_selected_pin.selected = False
                self.curr_selected_slot = None
                self.curr_selected_pin = None

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

        if self.curr_selected_obj:
            self.curr_selected_obj.selected = False
        self.curr_selected_obj = None

    def destroy(self):
        pass
