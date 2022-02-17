import pygame as pg


class State:
    def __init__(self, manager):
        self.manager = manager
        self.highlightable = []
        self.current_hovered_obj = None

    def process_input(self, event):
        # Get object under mouse
        #hovered_obj = self.get_object_under_mouse()
        #if hasattr(hovered_obj, 'hovered'):
            #if self.current_hovered_obj:
            #    self.current_hovered_obj.hovered = False
            #self.current_hovered_obj = hovered_obj
            #self.current_hovered_obj.hovered = True

        #if event.type == CLICKED and hasattr(hovered_obj, 'on_clicked'):
        #    hovered_obj.on_clicked()
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

    # Handles hover, select, and click functionality
