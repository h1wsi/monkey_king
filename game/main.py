
import os
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

timer = pg.time.Clock()
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# определение высоты и ширины секций платформ, а также угол наклона
section_width = WINDOW_WIDTH // 32
section_height = WINDOW_HEIGHT // 32

incline = section_height // 8

# класс для создания платформы
class Platform():
    def __init__(self, x_position, y_position, length):

        self.x_position = x_position * section_width
        self.y_position = y_position
        self.length = length
        self.top = self.draw()

    def draw(self):
        line_width = 7
        platform_color = (225, 51, 129)

        for i in range(self.length):  

            # определение координат границ прямоугольника
            bottom_coordinate = self.y_position + section_height 
            left_coordinate = self.x_position + (section_width * i) 
            right_coordinate = left_coordinate + section_width 
            top_coordinate = self.y_position
            # создание изображения платформы
            pg.draw.rect(screen, platform_color, (left_coordinate, top_coordinate, right_coordinate - left_coordinate, bottom_coordinate - top_coordinate))
            # определение линии, по которой будет передвигаться персонаж
            top_line = pg.rect.Rect((self.x_position, self.y_position), (self.length * section_width, 2))
        
        return top_line

# функция изображения игрового поля
def draw_field():
    platforms = [(5, 500, 5)]
    ladders = []
    platform_objs = []

    for platform in platforms:
        platform_objs.append(Platform(*platform))


# игровой loop
run_game = True

while run_game:
    screen.fill('black')
    timer.tick(FPS)

    draw_field()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:

            run_game = False

    pg.display.flip()

pg.quit()



