import pygame

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Run Dino! Run!')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 100

cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100


clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


def run_game():
    global make_jump
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()


        display.fill((255, 255, 255))
        draw_cactus()

        pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))

        pygame.display.update()
        clock.tick(60)


def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False

def draw_cactus():
    global cactus_x, cactus_y, cactus_width, cactus_height

    if cactus_x >= -cactus_width:
        pygame.draw.rect(display, (224, 44, 64), (cactus_x, cactus_y, cactus_width, cactus_height))
        cactus_x -= 4
    else:
        cactus_x = display_width - 50



run_game()

