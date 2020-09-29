import pygame

pygame.init()

icon = pygame.image.load('Background/icon.png')
menu_bckgr = pygame.image.load('Background/test_menu.jpg')

land = pygame.image.load(r'Background/Land.jpg')

cactus_img = [pygame.image.load('Objects/Cactus0.png'), pygame.image.load('Objects/Cactus1.png'),
              pygame.image.load('Objects/Cactus2.png')]

stone_img = [pygame.image.load('Objects/Stone0.png'), pygame.image.load('Objects/Stone1.png')]
cloud_img = [pygame.image.load('Objects/Cloud0.png'), pygame.image.load('Objects/Cloud1.png')]
cloud_img[0] = pygame.transform.scale(cloud_img[0], (93, 51))
cloud_img[1] = pygame.transform.scale(cloud_img[1], (120, 56))

dino_img = [pygame.image.load('Dino/Dino0.png'), pygame.image.load('Dino/Dino1.png'), pygame.image.load('Dino/Dino2.png'),
            pygame.image.load('Dino/Dino3.png'), pygame.image.load('Dino/Dino4.png')]

bird_img = [pygame.image.load('Bird/Bird0.png'), pygame.image.load('Bird/Bird1.png'), pygame.image.load('Bird/Bird2.png'),
            pygame.image.load('Bird/Bird3.png'), pygame.image.load('Bird/Bird4.png')]

heart_img = pygame.image.load('Effects/heart.png')
heart_img = pygame.transform.scale(heart_img, (30, 30))

bullet_img = pygame.image.load('Effects/shot.png')
bullet_img = pygame.transform.scale(bullet_img, (30, 9))

light_img = [pygame.image.load('Effects/sq1.png'), pygame.image.load('Effects/sq2.png'), pygame.image.load('Effects/sq3.png'),
             pygame.image.load('Effects/sq4.png'), pygame.image.load('Effects/sq5.png'), pygame.image.load('Effects/sq6.png'),
             pygame.image.load('Effects/sq7.png'), pygame.image.load('Effects/sq8.png'), pygame.image.load('Effects/sq9.png'),
             pygame.image.load('Effects/sq10.png')]
