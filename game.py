import parameters as p
from bullet import *
from button import *
from objects import *
from effects import *
from images import *


class Game:
    def __init__(self):
        pygame.display.set_caption('Run Dino! Run!')
        pygame.display.set_icon(icon)

        pygame.mixer.music.load('background.mp3')
        pygame.mixer.music.set_volume(0.3)

        cactus_option = [69, 449, 37, 410, 40, 420]
        img_counter = 0
        health = 2
        make_jump = False
        jump_counter = 30
        scores = 0
        max_scores = 0
        max_above = 0
        cooldown = 0

    def show_menu(self):
        pygame.mixer.music.load('Sounds/sfx7.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        start_btn = Button(288, 70)
        quit_btn = Button(120, 70)

        show = True
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_bckgr, (0, 0))
            start_btn.draw(270, 200, 'Start game', self.start_game, 50)
            quit_btn.draw(358, 300, 'Quit', quit, 50)

            draw_mouse()

            pygame.display.update()
            clock.tick(60)

    def start_game(self):
        # global scores, make_jump, jump_counter, usr_y, health, cooldown

        # pygame.mixer.music.load('Sounds/sfx7.wav')
        # pygame.mixer.music.set_volume(0.3)
        # pygame.mixer.music.play(-1)

        while self.game_cycle():
            self.scores = 0
            self.make_jump = False
            self.jump_counter = 30
            self.usr_y = display_height - usr_height - 100
            self.health = 2
            self.cooldown = 0

    def game_cycle(self):
        game = True
        cactus_arr = []
        create_cactus_arr(cactus_arr)

        stone, cloud = open_random_objects()
        heart = Object(display_width, 280, 30, heart_img, 4)

        all_btn_bullets = []
        all_ms_bullets = []

        bird1 = Bird(-80)
        bird2 = Bird(-49)

        all_birds = [bird1, bird2]

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if keys[pygame.K_SPACE]:
                make_jump = True

            count_scores(cactus_arr)

            display.blit(land, (0, 0))
            print_text('Scores: ' + str(scores), 600, 10)

            draw_array(cactus_arr)
            move_objects(stone, cloud)

            draw_dino()

            if keys[pygame.K_ESCAPE]:
                pause()

            if not cooldown:
                if keys[pygame.K_x]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets.append(Bullet(usr_x + usr_width, usr_y + 28))
                    cooldown = 50
                elif click[0]:
                    pygame.mixer.Sound.play(bullet_sound)
                    add_bullet = Bullet(usr_x + usr_width, usr_y + 28)
                    add_bullet.find_path(mouse[0], mouse[1])

                    all_ms_bullets.append(add_bullet)
                    cooldown = 50
            else:
                print_text('Cooldown time: ' + str(cooldown // 10), 482, 40)
                cooldown -= 1

            for bullet in all_btn_bullets:
                if not bullet.move():
                    all_btn_bullets.remove(bullet)

            for bullet in all_ms_bullets:
                if not bullet.move_to():
                    all_ms_bullets.remove(bullet)

            heart.move()
            hearts_plus(heart)

            if make_jump:
                jump()

            if check_collision(cactus_arr):
                # pygame.mixer.music.stop()
                # pygame.mixer.Sound.play(fall_sound)
                # if not check_health():
                game = False

            show_health()

            # bird1.draw()
            # bird2.draw()

            draw_birds(all_birds)
            check_birds_dmg(all_ms_bullets, all_birds)

            draw_mouse()
            pygame.display.update()
            clock.tick(80)
        return game_over()
