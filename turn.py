from collections import Counter
import pygame as pg


class Turn:

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    empty = (210, 180, 140)

    def __init__(self, slots, curr_turn):
        self.slots = slots
        self.guess = []
        self.hint = []
        self.curr_turn = curr_turn

    def begin_turn(self):
        for slot in self.slots:
            slot.enabled = True

    def lock_guess(self):
        for slot in self.slots:
            self.guess.append(slot.color)

    def check_guess(self, code):
        zipped = list(zip(code, self.guess))

        # Find exact matches
        for c, g in zipped.copy():
            if c == g:
                self.hint.append('black')
                zipped.remove((c, g))

        new_code = [i for i, j in zipped]
        new_guess = [j for i, j in zipped]

        # User intersection of the remaining code and guess to find matches in incorrect spots
        intersection = list((Counter(new_code) & Counter(new_guess)).elements())

        for j in range(0, len(intersection)):
            self.hint.append('white')

        while len(self.hint) < 4:
            self.hint.append('empty')

    def show_hint(self, screen):
        for y in range(self.curr_turn*2, self.curr_turn*2 + 2):
            for x in range(0, 2):
                if self.hint[2*y+x-self.curr_turn*4] == 'black':
                    pg.draw.circle(screen, self.black, (312.5 + x * 25, 12.5 + y * 25), 5)
                elif self.hint[2*y+x-self.curr_turn*4] == 'white':
                    pg.draw.circle(screen, self.white, (312.5 + x * 25, 12.5 + y * 25), 5)
                elif self.hint[2*y+x-self.curr_turn*4] == 'empty':
                    pg.draw.circle(screen, self.empty, (312.5 + x * 25, 12.5 + y * 25), 5)

    def end_turn(self):
        for slot in self.slots:
            slot.submitted = True
            slot.enabled = False

    def resolve(self, code, screen):
        self.lock_guess()
        self.check_guess(code)
        self.show_hint(screen)
        self.end_turn()
