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

        self.cactus_option = [69, 449, 37, 410, 40, 420]
        self.img_counter = 0
        self.health = 2
        self.make_jump = False
        self.jump_counter = 30
        self.scores = 0
        self.max_scores = 0
        self.max_above = 0
        self.cooldown = 0

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
            p.usr_y = p.display_height - p.usr_height - 100
            self.health = 2
            self.cooldown = 0

    def game_cycle(self):
        game = True
        cactus_arr = []
        self.create_cactus_arr(cactus_arr)

        stone, cloud = self.open_random_objects()
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
                self.make_jump = True

            if self.make_jump:
                self.jump()

            self.count_scores(cactus_arr)

            display.blit(land, (0, 0))
            print_text('Scores: ' + str(self.scores), 600, 10)

            self.draw_array(cactus_arr)
            self.move_objects(stone, cloud)

            self.draw_dino()

            if keys[pygame.K_ESCAPE]:
                self.pause()

            if not self.cooldown:
                if keys[pygame.K_x]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets.append(Bullet(p.usr_x + p.usr_width, p.usr_y + 28))
                    self.cooldown = 50
                elif click[0]:
                    pygame.mixer.Sound.play(bullet_sound)
                    add_bullet = Bullet(p.usr_x + p.usr_width, p.usr_y + 28)
                    add_bullet.find_path(mouse[0], mouse[1])

                    all_ms_bullets.append(add_bullet)
                    self.cooldown = 50
            else:
                print_text('Cooldown time: ' + str(self.cooldown // 10), 482, 40)
                self.cooldown -= 1

            for bullet in all_btn_bullets:
                if not bullet.move():
                    all_btn_bullets.remove(bullet)

            for bullet in all_ms_bullets:
                if not bullet.move_to():
                    all_ms_bullets.remove(bullet)

            heart.move()
            self.hearts_plus(heart)

            if self.check_collision(cactus_arr):
                # pygame.mixer.music.stop()
                # pygame.mixer.Sound.play(fall_sound)
                # if not check_health():
                game = False

            self.show_health()

            # bird1.draw()
            # bird2.draw()

            self.draw_birds(all_birds)
            self.check_birds_dmg(all_ms_bullets, all_birds)

            draw_mouse()
            pygame.display.update()
            clock.tick(80)
        return self.game_over()

    def game_over(self):
        if self.scores > self.max_scores:
            self.max_scores = self.scores

        stopped = True
        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Game Over. Press Enter to play again, Esc to exit', 50, 300)
            print_text('Max Scores: ' + str(self.max_scores), 300, 350)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return False
            if keys[pygame.K_ESCAPE]:
                return False

            pygame.display.update()
            clock.tick(15)

    @staticmethod
    def pause():
        paused = True
        pygame.mixer.music.pause()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Paused. Press enter to continue', 160, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            pygame.display.update()
            clock.tick(15)

        pygame.mixer.music.unpause()

    def draw_dino(self):
        if self.img_counter == 25:
            self.img_counter = 0

        display.blit(dino_img[self.img_counter // 5], (usr_x, usr_y))
        self.img_counter += 1

    def create_cactus_arr(self, array):
        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]
        array.append(Object(display_width + 20, height, width, img, 4))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]
        array.append(Object(display_width + 300, height, width, img, 4))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]
        array.append(Object(display_width + 600, height, width, img, 4))

    def draw_array(self, array):
        for cactus in array:
            check = cactus.move()
            if not check:
                self.object_return(array, cactus)

    def check_collision(self, barriers):
        for barrier in barriers:
            if barrier.y == 449:  # Little cactus
                if not self.make_jump:
                    if barrier.x <= p.usr_x + p.usr_width - 30 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter >= 0:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 30 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                else:
                    if p.usr_y + p.usr_height - 10 >= barrier.y:
                        if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
            else:
                if not self.make_jump:
                    if barrier.x <= p.usr_x + p.usr_width - 2 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter >= 10:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 5 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.jump_counter >= -1:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 30 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                else:
                    if p.usr_y + p.usr_height - 8 >= barrier.y:
                        if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
            return False

    def object_return(self, objects, obj):
        radius = self.find_radius(objects)

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_option[choice * 2]
        height = self.cactus_option[choice * 2 + 1]

        obj.return_self(radius, height, width, img)

    @staticmethod
    def find_radius(array):
        maximum = max(array[0].x, array[1].x, array[2].x)

        if maximum < display_width:
            radius = display_width
            if radius - maximum < 50:
                radius += 280
        else:
            radius = maximum

        choice = random.randrange(0, 5)
        if choice == 0:
            radius += random.randrange(10, 15)
        else:
            radius += random.randrange(250, 400)

        return radius

    @staticmethod
    def open_random_objects():
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]

        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]

        stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
        cloud = Object(display_width, 80, 70, img_of_cloud, 2)

        return stone, cloud

    def jump(self):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pygame.mixer.Sound.play(jump_sound)
            if self.jump_sound == -26:
                pygame.mixer.Sound.play(fall_sound)

            p.usr_y -= self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            self.jump_counter = 30
            self.make_jump = False

    @staticmethod
    def move_objects(stone, cloud):
        check = stone.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_stone = stone_img[choice]
            stone.return_self(display_width, 500 + random.randrange(10, 80), stone.width, img_of_stone)

        check = cloud.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_cloud = cloud_img[choice]
            cloud.return_self(display_width, random.randrange(10, 200), cloud.width, img_of_cloud)
