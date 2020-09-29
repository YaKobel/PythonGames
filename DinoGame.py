import pygame
import random

pygame.init()






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