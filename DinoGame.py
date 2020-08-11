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


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((255, 255, 255))

        pygame.draw.rect(display, (247, 240, 22), (usr_x, usr_y, usr_width, usr_height))

        pygame.display.update()

run_game()

