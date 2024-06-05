import pygame, sys

# Määritä kenttä (0 = tyhjä, 1 = seinä, 2 = maali 3=laatikko)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 3, 0, 0, 1, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 2, 1, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Määritä ruudun koko ja kentän leveys ja korkeus
BLOCK_SIZE = 75
MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)

# Määritä pelinäkymän koko
SCREEN_WIDTH = BLOCK_SIZE * MAP_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * MAP_HEIGHT

#Alusta pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sokobun_kesäleiri2024")

