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
