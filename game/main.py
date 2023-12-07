
import os
import random
import pygame as pg

import game.constants as c

pg.init()

inf = pg.display.Info()
pg.display.set_caption("Monkey King")
timer = pg.time.Clock()

screen = pg.display.set_mode([c.WINDOW_WIDTH, c.WINDOW_HEIGHT])

section_width = c.WINDOW_WIDTH // 32
section_height = c.WINDOW_HEIGHT // 32

incline = section_height // 8

run_game = True

while run_game:
    screen.fill('black')
    timer.tick(c.FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:

            run_game = False

    pg.display.flip()

pg.quit()



