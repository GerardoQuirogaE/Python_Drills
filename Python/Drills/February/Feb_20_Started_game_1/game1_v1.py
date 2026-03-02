import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}",False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

def game_text_centered(text_to_display,x,y):
        text_surface = test_font.render(f"{text_to_display}",False,(64,64,64))
        text_rect = text_surface.get_rect(center = (x,y))
        screen.blit(text_surface,text_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Spinosaurus Run")
clock = pygame.time.Clock()
test_font = pygame.font.Font("../Feb 16 pygame v1/font/Pixeltype.ttf",50)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load("../Feb 16 pygame v1/graphics/Sky.png").convert()
ground_surface = pygame.image.load("../Feb 16 pygame v1/graphics/ground.png").convert()

# score_surf = test_font.render("RoboX Code Interpreter", False, (64,64,64)).convert_alpha()
# score_rec = score_surf.get_rect(center = (400, 50))

snail_surface = pygame.image.load("../Feb 16 pygame v1/graphics/terminal/closed/frame0.png")
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_tail_1 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-4.png").convert_alpha()
player_tail_2 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-5.png").convert_alpha()
player_tail_3 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-6.png").convert_alpha()
player_tail_4 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-7.png").convert_alpha()
player_tail_5 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-8.png").convert_alpha()
player_tail_6 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-9.png").convert_alpha()
player_tail_7 = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/tail/pixil-frame-10.png").convert_alpha()

player_tails = [player_tail_1, player_tail_2,player_tail_3, player_tail_4, player_tail_5, player_tail_6,player_tail_7]

player_index = 0

# player_surf = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/base_dino.png").convert_alpha()

player_surf = player_tails[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro Sreen
player_stand = pygame.image.load("../../../Data/graphics/game_1/Spinosaurus/base_dino.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render("Pixel Runner",False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press space to run",False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400, 330))

player_animation_timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        # Score
        # pygame.draw.rect(screen, "#c0e8ec", score_rec)
        # pygame.draw.rect(screen, "#c0e8ec", score_rec,10)
        # screen.blit(score_surf, score_rec)

        score = display_score()

        snail_rect.left -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f"Your score: {score}", False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)



    pygame.display.update()
    clock.tick(60)
