import pygame as pg
import random
from state import State
from pin import Pin
from slot import Slot
from button import Button
from turn import Turn
from pause_menu import PauseMenu
from enum import Enum
from end_game import EndGame


class Difficulty(Enum):
    EASY = 0
    NORMAL = 1
    HARD = 2


class Gameplay(State):
    # Dimensions
    width = 350
    height = 650

    # Colors
    bg = (210, 180, 140)
    grid = (50, 50, 50)
    empty_guess = (0, 0, 0)

    CODE_COLORS = ['red', 'yellow', 'green', 'blue', 'black', 'white']
    SONGS = ['sound/Gameplay1.ogg', 'sound/Gameplay2.ogg', 'sound/Gameplay3.ogg', 'sound/Gameplay4.ogg']

    # Initialize turn variables
    curr_turn = 0
    curr_hint = []

    def __init__(self, manager, difficulty, mixer):
        State.__init__(self, manager)
        self.num_rounds = 0
        self.code = None
        self.font = pg.font.SysFont('Calibri', 30)
        self.difficulty = difficulty

        # Game objects
        self.pins = []
        self.slots = []
        self.buttons = []
        self.highlightable = []
        self.turns = []
        self.curr_selected_slot = None
        self.curr_selected_pin = None

        # Define mixer
        self.mixer = mixer
        self.mixer.music.set_volume(0.025)
        # Start playing first song
        self.play_next_song()

        # Set number of rounds
        if self.difficulty == Difficulty.EASY or self.difficulty == Difficulty.NORMAL:
            self.num_rounds = 12
        elif self.difficulty == Difficulty.HARD:
            self.num_rounds = 8

        # Generate code
        if self.difficulty == Difficulty.EASY:
            self.code = (random.sample(self.CODE_COLORS, 4))
        elif self.difficulty == Difficulty.NORMAL or self.difficulty == Difficulty.HARD:
            self.code = random.choices(self.CODE_COLORS, k=4)

        # Create pins
        for y in range(0, 6):
            pin = Pin(y, self.CODE_COLORS[y])
            self.pins.append(pin)
            self.highlightable.append(pin)

        for p in self.pins:
            p.group = self.pins

        # Create slots
        for y in range(0, 12):
            for x in range(0, 4):
                slot = Slot(x, y)
                self.slots.append(slot)
                self.highlightable.append(slot)

        # Create turns
        i = 0
        if difficulty == Difficulty.EASY or difficulty == Difficulty.NORMAL:
            for row in range(0, len(self.slots), 4):
                turn = Turn(self.slots[row:row + 4], i)
                self.turns.append(turn)
                i += 1
        elif difficulty == Difficulty.HARD:
            for row in range(0, len(self.slots) - 16, 4):
                turn = Turn(self.slots[row:row + 4], i)
                self.turns.append(turn)
                i += 1

        # Create buttons
        border = 20
        top = 610
        btn_width = 130

        self.submit_btn = Button(border, top, self.font, 'Submit')
        self.submit_btn.enabled = False
        self.buttons.append(self.submit_btn)
        self.highlightable.append(self.submit_btn)

        self.pause_btn = Button(self.width - border - btn_width, top, self.font, 'Pause')
        self.buttons.append(self.pause_btn)
        self.highlightable.append(self.pause_btn)

        # On-clicked property
        self.submit_btn.on_clicked = self.on_submit_btn_clicked
        self.pause_btn.on_clicked = self.on_pause_btn_clicked

        # Enable slots for first turn
        self.turns[self.curr_turn].begin_turn()

    def on_submit_btn_clicked(self):
        self.turns[self.curr_turn].resolve(self.code)
        self.submit_btn.enabled = False
        self.check_end()

    def on_pause_btn_clicked(self):
        self.manager.push(PauseMenu(self.manager, self.mixer))

    def process_input(self, event):
        State.process_input(self, event)

        for p in self.pins:
            if p.selected:
                self.curr_selected_pin = p

        for s in self.turns[self.curr_turn].slots:
            if s.selected:
                self.curr_selected_slot = s

        if self.curr_selected_pin and self.curr_selected_slot:
            self.curr_selected_slot.color = self.curr_selected_pin.color
            self.curr_selected_slot.selected = False
            self.curr_selected_pin.selected = False
            self.curr_selected_slot = None
            self.curr_selected_pin = None

    def update(self):
        if self.curr_turn < self.num_rounds:
            colors_filled = 0
            for s in self.turns[self.curr_turn].slots:
                if s.color:
                    colors_filled += 1

            if colors_filled == 4:
                self.submit_btn.enabled = True

        if not self.mixer.music.get_busy():
            self.play_next_song()

    def play_next_song(self):
        curr_song = self.SONGS[0]
        self.mixer.music.load(curr_song)
        self.mixer.music.play()
        self.SONGS = self.SONGS[1:]
        self.SONGS.append(curr_song)

    def draw(self, screen):
        screen.fill(self.bg)

        # Draw grid lines
        for x in range(1, 12):
            pg.draw.line(screen, self.grid, (50, x * 50), (self.width, x * 50))

        pg.draw.line(screen, self.grid, (0, 600), (self.width, 600))
        pg.draw.line(screen, self.grid, (50, 0), (50, 600))
        pg.draw.line(screen, self.grid, (300, 0), (300, 600))

        # Draw pins
        for p in self.pins:
            p.draw(screen)

        # Draw slots
        if self.num_rounds == 8:
            for i in range(len(self.slots) - 16):
                self.slots[i].draw(screen)
        else:
            for s in self.slots:
                s.draw(screen)

        # Display buttons
        for b in self.buttons:
            b.draw(screen)

        # Display previous hints
        for t in self.turns:
            if 'black' in t.hint or 'white' in t.hint:
                for y in range(t.curr_turn * 2, t.curr_turn * 2 + 2):
                    for x in range(0, 2):
                        if t.hint[2 * y + x - t.curr_turn * 4] == 'black':
                            pg.draw.circle(screen, t.black, (312.5 + x * 25, 12.5 + y * 25), 5)
                        elif t.hint[2 * y + x - t.curr_turn * 4] == 'white':
                            pg.draw.circle(screen, t.white, (312.5 + x * 25, 12.5 + y * 25), 5)
                        elif t.hint[2 * y + x - t.curr_turn * 4] == 'empty':
                            pg.draw.circle(screen, t.empty, (312.5 + x * 25, 12.5 + y * 25), 5)

    def check_end(self):
        if len(self.turns[self.curr_turn].hint) == 4 and 'white' not in self.turns[self.curr_turn].hint \
                and 'empty' not in self.turns[self.curr_turn].hint:
            self.destroy()
            self.manager.push(EndGame(self.manager, 'YOU WIN', self.difficulty, self.mixer, self.code))
        elif self.curr_turn == self.num_rounds - 1:
            self.destroy()
            self.manager.push(EndGame(self.manager, 'GAME OVER', self.difficulty, self.mixer, self.code))
        else:
            self.curr_turn += 1
            self.turns[self.curr_turn].begin_turn()

    def destroy(self):
        self.mixer.music.stop()
