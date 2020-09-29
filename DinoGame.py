import pygame
import random

pygame.init()

pygame.display.set_caption('Run Dino! Run!')

pygame.display.set_icon(icon)

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.set_volume(0.3)

cactus_option = [69, 449, 37, 410, 40, 420]

img_counter = 0
health = 2

cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100


make_jump = False
jump_counter = 30

scores = 0
max_scores = 0
max_above = 0

cooldown = 0


def show_menu():
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
        start_btn.draw(270, 200, 'Start game', start_game, 50)
        quit_btn.draw(358, 300, 'Quit', quit, 50)

        draw_mouse()

        pygame.display.update()
        clock.tick(60)


def start_game():
    global scores, make_jump, jump_counter, usr_y, health, cooldown

    pygame.mixer.music.load('sfx7.wav')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    while game_cycle():
        scores = 0
        make_jump = False
        jump_counter = 30
        usr_y = display_height - usr_height - 100
        health = 2
        cooldown = 0


def game_cycle():
    global make_jump, cooldown

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


def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        if jump_counter == 30:
            pygame.mixer.Sound.play(jump_sound)
        if jump_sound == -26:
            pygame.mixer.Sound.play(fall_sound)

        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_cactus_arr(array):
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_option[choice * 2]
    height = cactus_option[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_option[choice * 2]
    height = cactus_option[choice * 2 + 1]
    array.append(Object(display_width + 300, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_option[choice * 2]
    height = cactus_option[choice * 2 + 1]
    array.append(Object(display_width + 600, height, width, img, 4))


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


def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array, cactus)


def object_return(objects, obj):
    radius = find_radius(objects)

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_option[choice * 2]
    height = cactus_option[choice * 2 + 1]

    obj.return_self(radius, height, width, img)


def open_random_objects():
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
    cloud = Object(display_width, 80, 70, img_of_cloud, 2)

    return stone, cloud


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


def draw_dino():
    global img_counter
    if img_counter == 25:
        img_counter = 0

    display.blit(dino_img[img_counter // 5], (usr_x, usr_y))
    img_counter += 1





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


def check_collision(barriers):
    for barrier in barriers:
        if barrier.y == 449:  # Little cactus
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter >= 0:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            else:
                if usr_y + usr_height - 10 >= barrier.y:
                    if barrier.x <= usr_x <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
        else:
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 2 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter >= 10:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            elif jump_counter >= -1:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            else:
                if usr_y + usr_height - 8 >= barrier.y:
                    if barrier.x <= usr_x <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
        return False


def count_scores(barriers):
    global scores, max_above
    above_cactus = 0

    if -20 <= jump_counter < 25:
        for barrier in barriers:
            if usr_y + usr_height - 5 <= barrier.y:
                if barrier.x <= usr_x <= barrier.x + barrier.width:
                    above_cactus += 1
                elif barrier.x <= usr_x + usr_width <= barrier.x + barrier.width:
                    above_cactus += 1

        max_above = max(max_above, above_cactus)
    else:
        if jump_counter == -30:
            scores += max_above
            max_above = 0


def game_over():
    global scores, max_scores
    if scores > max_scores:
        max_scores = scores

    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Game Over. Press Enter to play again, Esc to exit', 50, 300)
        print_text('Max Scores: ' + str(max_scores), 300, 350)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return False
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(15)


def show_health():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(heart_img, (x, 20))
        x += 40
        show += 1


def check_health():
    global health
    health -= 1
    if health == 0:
        pygame.mixer.Sound.play(loss_sound)
        return False
    else:
        pygame.mixer.Sound.play(fall_sound)
        return True


def hearts_plus(heart):
    global health, usr_x, usr_y, usr_width, usr_height

    if heart.x <= -heart.width:
        radius = display_width + random.randrange(500, 1700)
        heart.return_self(radius, heart.y, heart.width, heart.image)

    if usr_x <= heart.x <= usr_x + usr_width:
        if usr_y <= heart.y <= usr_y + usr_height:
            pygame.mixer.Sound.play(heart_plus_sound)
            if health < 5:
                health += 1

            radius = display_width + random.randrange(500, 1700)
            heart.return_self(radius, heart.y, heart.width, heart.image)


def draw_birds(birds):
    for bird in birds:
        action = bird.draw()
        if action == 1:
            bird.show()
        elif action == 2:
            bird.hide()
        else:
            bird.shoot()

def check_birds_dmg(bullets, birds):
    for bird in birds:
        for bullet in bullets:
            bird.check_dmg(bullet)


show_menu()
pygame.quit()
quit()

# pygame