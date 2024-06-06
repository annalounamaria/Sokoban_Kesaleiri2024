                for box in boxes:
                    if(pygame.Rect.colliderect(player, box.rect)):
                        if(key_pressed == "right"):
                            box.move(BLOCK_SIZE,0)
                        elif(key_pressed == "left"):
                            box.move(-BLOCK_SIZE,0)
                        elif(key_pressed == "down"):
                            box.move(0,BLOCK_SIZE)
                        elif(key_pressed == "up"):
                            box.move(0, -BLOCK_SIZE)
