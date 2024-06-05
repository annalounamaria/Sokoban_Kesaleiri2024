#tehdään seinäpalikka
wall_img = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
wall_img.fill("#00556f")

#piirretään pelialueen seinää ja lattiaa
def draw_floor_and_walls():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if MAP[y][x] == 1:
                screen.blit(wall_img, (x * BLOCK_SIZE, y * BLOCK_SIZE))
