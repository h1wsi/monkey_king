
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

# определение высоты рядов платформ
row1_y = WINDOW_HEIGHT - 2 * section_height * 2    # высота начальной платформы
row2_y = row1_y - 4 * section_height
row3_y = row2_y - 7 * incline - 3 * section_height
row4_y = row3_y - 4 * section_height
row5_y = row4_y - 7 * incline - 3 * section_height
row6_y = row5_y - 4 * section_height

# определение высоты верхних границ платформ
row1_top = row1_y - 5 * incline
row2_top = row2_y - 8 * incline
row3_top = row3_y - 8 * incline
row4_top = row4_y - 8 * incline
row5_top = row5_y - 8 * incline
row6_top = row6_y - 4 * incline

current_level = 0
# элементы игры - первое значение кортежа: x левого верхнего угла,
# y - левого верхнего угла, длина платформы в секциях
levels = [{'platforms': [(1, row1_y, 15), (16, row1_y - incline, 3),
                       (19, row1_y - 2 * incline, 3), (22, row1_y - 3 * incline, 3),
                       (25, row1_y - 4 * incline, 3), (28, row1_y - 5 * incline, 3),
                       (25, row2_y, 3), (22, row2_y - incline, 3),
                       (19, row2_y - 2 * incline, 3), (16, row2_y - 3 * incline, 3),
                       (13, row2_y - 4 * incline, 3), (10, row2_y - 5 * incline, 3),
                       (7, row2_y - 6 * incline, 3), (4, row2_y - 7 * incline, 3),
                       (2, row2_y - 8 * incline, 2), (4, row3_y, 3),
                       (7, row3_y - incline, 3), (10, row3_y - 2 * incline, 3),
                       (13, row3_y - 3 * incline, 3), (16, row3_y - 4 * incline, 3),
                       (19, row3_y - 5 * incline, 3), (22, row3_y - 6 * incline, 3),
                       (25, row3_y - 7 * incline, 3), (28, row3_y - 8 * incline, 2),
                       (25, row4_y, 3), (22, row4_y - incline, 3),
                       (19, row4_y - 2 * incline, 3), (16, row4_y - 3 * incline, 3),
                       (13, row4_y - 4 * incline, 3), (10, row4_y - 5 * incline, 3),
                       (7, row4_y - 6 * incline, 3), (4, row4_y - 7 * incline, 3),
                       (2, row4_y - 8 * incline, 2), (4, row5_y, 3),
                       (7, row5_y - incline, 3), (10, row5_y - 2 * incline, 3),
                       (13, row5_y - 3 * incline, 3), (16, row5_y - 4 * incline, 3),
                       (19, row5_y - 5 * incline, 3), (22, row5_y - 6 * incline, 3),
                       (25, row5_y - 7 * incline, 3), (28, row5_y - 8 * incline, 2),
                       (25, row6_y, 3), (22, row6_y - incline, 3),
                       (19, row6_y - 2 * incline, 3), (16, row6_y - 3 * incline, 3),
                       (2, row6_y - 4 * incline, 14), (13, row6_y - 4 * section_height, 6)],
    # Создание канатов
           'ropes': [(12, row2_y + 6 * incline, 2), (12, row2_y + 26 * incline, 2),
                       (25, row2_y + 11 * incline, 4), (6, row3_y + 11 * incline, 3),
                       (14, row3_y + 8 * incline, 4), (10, row4_y + 6 * incline, 1),
                       (10, row4_y + 24 * incline, 2), (16, row4_y + 6 * incline, 5),
                       (25, row4_y + 9 * incline, 4), (6, row5_y + 11 * incline, 3),
                       (11, row5_y + 8 * incline, 4), (23, row5_y + 4 * incline, 1),
                       (23, row5_y + 24 * incline, 2), (25, row6_y + 9 * incline, 4),
                       (13, row6_y + 5 * incline, 2), (13, row6_y + 25 * incline, 2),
                       (18, row6_y - 27 * incline, 4), (12, row6_y - 17 * incline, 2),
                       (10, row6_y - 17 * incline, 2), (12, -5, 13), (10, -5, 13)],
            
           'target': (13, row6_y - 4 * section_height, 3)}]

# класс для создания платформы
class Platform():
    def __init__(self, x_position, y_position, length):

        self.x_position = x_position * section_width
        self.y_position = y_position
        self.length = length
        self.top = self.draw()

    def draw(self):
        # line_width = 7
        platform_color = ('blue')

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
    
    ropes = []
    platform_objs = []
    blocks = []

    ropes = levels[current_level]['ropes']
    platforms = levels[current_level]['platforms']

    for platform in platforms:
        platform_objs.append(Platform(*platform))
        blocks.append(platform_objs[-1].top)

    return blocks


# игровой loop
run_game = True

while run_game:
    screen.fill('black')
    timer.tick(FPS)

    field = draw_field()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:

            run_game = False

    pg.display.flip()

pg.quit()



