import pygame as pg
from state import State


class Gameplay(State):
    bg = (210, 180, 140)
    grid = (50, 50, 50)
    empty_guess = (0, 0, 0)

    def __init__(self, screen, width, height, colors, font, rules_font):
        State.__init__(self)
        self.num_rounds = 0
        self.code = None
        self.screen = screen
        self.width = width
        self.height = height
        self.colors = colors
        self.font = font
        self.rules_font = rules_font
        self.pins = []
        self.slots = []
        self.buttons = []
        self.highlightable = []
        self.turns = []
