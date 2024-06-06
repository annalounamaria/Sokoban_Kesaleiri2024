def create_goals():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
           if MAP[y][x] == 2:
                goal_rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                goals.append(goal_rect)

