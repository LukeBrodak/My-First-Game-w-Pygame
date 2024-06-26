import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Graphics\Font\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Graphics\sky.png').convert()
ground_surface = pygame.image.load('Graphics\purple_floor2.png').convert()
text_surface = test_font.render('Cosmic Cartwheels', False, 'Purple2').convert()

snail_surface = pygame.image.load('Graphics\slimeWalk1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('Graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,285))
    screen.blit(text_surface,(280,50))
    snail_x_pos += -3
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,265))
    if player_rect <= -100: player_rect = 600
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)