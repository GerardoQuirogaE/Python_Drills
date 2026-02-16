import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RoboX Code")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
test_surface = test_font.render("RoboX Code Interpreter", False, "Black").convert_alpha()

snail_surface = pygame.image.load("graphics/fly/buterfly1.png")
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load("graphics/roboX/robot1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(test_surface, (100,100))

    snail_rect.left -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
