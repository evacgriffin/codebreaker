class Manager:
    def __init__(self):
        self.states = []

    def process_input(self, event):
        self.states[-1].process_input(event)

    def update(self):
        self.states[-1].update()

    def draw(self, screen):
        self.states[-1].draw(screen)

    def push(self, state):
        if self.states:
            self.states[-1].deactivate()
        self.states.append(state)

    def pop(self):
        self.states[-1].deactivate()
        self.states.pop()

    def clear(self):
        # Remove all states from the list
        pass
