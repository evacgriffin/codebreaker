from collections import Counter


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
        self.selected_slot = None

        # Set slot group
        for s in self.slots:
            s.group = self.slots

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

    def end_turn(self):
        for slot in self.slots:
            slot.enabled = False

    def resolve(self, code):
        self.lock_guess()
        self.check_guess(code)
        self.end_turn()
