import pygame, sys
from pygame.locals import QUIT
import box

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

# Alusta Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sokoban, Kodarit kesäohjelma 2024")



#Tehdään seinäpalikka
wall_img = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
wall_img.fill("#00556f")

#Lataa kuvat
##Pelaaja
player_img = pygame.image.load("dino.png")
player_img = pygame.transform.scale(player_img, (BLOCK_SIZE, BLOCK_SIZE))

##Maali
goal_img = pygame.image.load("Dinoegg.png")
goal_img = pygame.transform.scale(goal_img, (BLOCK_SIZE, BLOCK_SIZE))

#Boxin eli laatikoiden kuvan lataus muuttujaan
box_img = pygame.image.load("box.png")
box_img = pygame.transform.scale(box_img, (BLOCK_SIZE, BLOCK_SIZE))


#tähän kerätään kentällä olevien maalien tiedot
goals = []
#tähän kerätään kentällä olevien boxien tiedot
boxes = []

# Piirrä kenttä
def draw_floor_and_walls():
    screen.fill("#a6c6d5")
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if MAP[y][x] == 1:
                screen.blit(wall_img, (x * BLOCK_SIZE, y * BLOCK_SIZE))
#Luo Maalit
def create_goals():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
           if MAP[y][x] == 2:
                goal_rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                goals.append(goal_rect)
                #screen.blit(goal_img, goal_rect)
#Piirrä maalit
def draw_goals():
    for goal in goals:
        screen.blit(goal_img, goal)

#Luo Boxit
def create_boxes():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if MAP[y][x] == 3:
                box_obj = box.Box(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE)
                boxes.append(box_obj)
#Piirrä Boxit
def draw_boxes():
    for box in boxes:
        screen.blit(box_img, box)           


#Alusta pelaaja ja pelajaan aloituspaikka
player_pos = [1, 1]  
player = pygame.Rect(player_pos[0] * BLOCK_SIZE, player_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

create_goals()
create_boxes()

#peliluuppi 
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_pressed = "left"
                if MAP[player_pos[1]][player_pos[0] - 1] != 1:
                    player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                key_pressed = "right"
                if MAP[player_pos[1]][player_pos[0] + 1] != 1:
                    player_pos[0] += 1
            elif event.key == pygame.K_UP:
                key_pressed = "up"
                if MAP[player_pos[1] - 1][player_pos[0]] != 1:
                    player_pos[1] -= 1 
            elif event.key == pygame.K_DOWN:
                key_pressed = "down"
                if MAP[player_pos[1] + 1][player_pos[0]] != 1:
                    player_pos[1] += 1



            player = pygame.Rect(player_pos[0] * BLOCK_SIZE, player_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)




    #HOX piirtojärjestys  
    draw_floor_and_walls()
    draw_goals()
    draw_boxes()
    screen.blit(player_img, player)
    pygame.display.update()


