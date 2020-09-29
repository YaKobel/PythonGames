from parameters import *
from images import light_img


def print_text(message, x, y, font_color=(0, 0, 0),  font_type='Background/PingPong.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def draw_mouse():
    global mouse_counter, need_draw_click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    mouse_size = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32]

    if click[0] or click[1]:
        need_draw_click = True

    if need_draw_click:
        draw_x = mouse[0] - mouse_size[mouse_counter] // 2
        draw_y = mouse[1] - mouse_size[mouse_counter] // 2

        display.blit(light_img[mouse_counter], (draw_x, draw_y))
        mouse_counter += 1

        if mouse_counter == 10:
            mouse_counter = 0
            need_draw_click = False