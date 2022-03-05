import pygame as pg
from pygame import mixer
from manager import Manager
from main_menu import MainMenu

pg.mixer.pre_init(44100, -16, 2, 512)
pg.mixer.init()
pg.init()

# Define game variables
KEY_COLORS = ['black', 'white']
DIFFICULTIES = ['easy', 'normal', 'hard']

screen_width = 350
screen_height = 650
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Codebreaker')

clock = pg.time.Clock()
fps = 60

manager = Manager()
manager.push(MainMenu(manager, mixer))

run = True
while run:

    # Event handlers
    for event in pg.event.get():
        # QUIT
        if event.type == pg.QUIT:
            run = False
        manager.process_input(event)

    manager.update()

    screen.fill((210, 180, 140))
    manager.draw(screen)
    pg.display.update()

    clock.tick(fps)

pg.quit()
