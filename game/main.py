
import os
import random
import pygame as pg

# вывод окна в центре экрана
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()

inf = pg.display.Info()

# значения ширины и высоты текущего экрана
SCREEN_WIDTH, SCREEN_HEIGHT = inf.current_w, inf.current_h
# значения ширины и высоты игрового окна
WINDOW_WIDTH, WINDOW_HEIGHT = SCREEN_WIDTH - 800, SCREEN_HEIGHT - 150

FPS = 60

pg.display.set_caption("Monkey King")
timer = pg.time.Clock()

screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# определение высоты и ширины платформ, а также угол наклона
section_width = WINDOW_WIDTH // 32
section_height = WINDOW_HEIGHT // 32

incline = section_height // 8

# игровой loop
run_game = True
while run_game:
    screen.fill('black')
    timer.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:

            run_game = False

    pg.display.flip()

pg.quit()



