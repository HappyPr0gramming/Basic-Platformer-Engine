import pygame
import time
gravity = 1

red = 255, 0, 0
blue = 0, 0, 225
col = red

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 150, 50, 50))
platform = pygame.Rect((300, 300, 200, 20))

pygame.mouse.set_visible(False)

run = True
while run :

    key = pygame.key.get_pressed()

    screen.fill((0, 200, 0))

    if player.colliderect(platform) == False:
        player.move_ip(0, gravity)
        time.sleep(0.01)
        gravity = gravity + 0.001
    if key[pygame.K_d] == True:
        for x in range(2):
            player.move_ip(1, 0)
            time.sleep(0.001)
    if key[pygame.K_a] == True:
        for x in range(2):
            player.move_ip(-1, 0)
            time.sleep(0.001)
    if player.colliderect(platform) == True:
        if 1 > gravity:
            gravity = gravity - 0.01
        elif key[pygame.K_w] == True:
            for x in range(100):
                player.move_ip(0, -1)
                time.sleep(0.001)


    pygame.draw.rect(screen, (col), player)
    pygame.draw.rect(screen, (0, 0, 0), platform)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()