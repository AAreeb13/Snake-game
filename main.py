# main.py
import pygame
import os
from snake import Snake
from snake import BLOCK_SIZE
import random


WIDTH, HEIGHT = 1024, 512
FPS = 10
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Areeb's Snake Game")

main_snake = Snake(WIDTH//2, HEIGHT//2)
APPLE_DIMENSION = (32, 32)


ORANGE = (255, 200, 100)
DARK_GREEN = (0, 40, 0)
GREEN = (0, 120, 0)

def spawn_apple() -> (int, int):
    return (random.randint(0, WIDTH - APPLE_DIMENSION[0]), random.randint(0, HEIGHT - APPLE_DIMENSION[1]))

APPLE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Photos', 'apple.png')), APPLE_DIMENSION)

def touches_apple(main_snake, apple_coordinate, APPLE_DIMENSION):
    head = main_snake.snakeBlocks[0]
    apple_x = apple_coordinate[0]
    apple_y = apple_coordinate[1]
    if head.x < apple_x + APPLE_DIMENSION[0] and \
        head.x + BLOCK_SIZE > apple_x and \
        head.y < apple_y + APPLE_DIMENSION[1] and \
        head.y + BLOCK_SIZE > apple_y:

        main_snake.increaseLength = True
        apple_x, apple_y = spawn_apple()
        return True
    return False

def draw_window(apple_coordinate):
    WIN.fill(DARK_GREEN)
    WIN.blit(APPLE_IMAGE, apple_coordinate)
    #DRAWING SNAKE
    for block in main_snake.snakeBlocks:
        pygame.draw.rect(WIN, GREEN, (block.x, block.y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

def key_stroke_handler(e) -> None:
    if e.key == pygame.K_UP:
        main_snake.change_direction('U')
    elif e.key == pygame.K_DOWN:
        main_snake.change_direction('D')
    elif e.key == pygame.K_LEFT:
        main_snake.change_direction('L')
    elif e.key == pygame.K_RIGHT:
        main_snake.change_direction('R')



def main():
    running = True
    clock = pygame.time.Clock()
    apple_coordinate = spawn_apple()
    while running:
        clock.tick(FPS)
        if touches_apple(main_snake, apple_coordinate,APPLE_DIMENSION):
            apple_coordinate = spawn_apple()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_stroke_handler(event)
        head = main_snake.snakeBlocks[0]
        for i in range(3, len(main_snake.snakeBlocks), 1):
            block = main_snake.snakeBlocks[i]
            if head.x == block.x and head.y == block.y:
                # Snake has collided with itself
                print("Game Over - Snake collided with itself!")
                running = False
        main_snake.update()
        
        draw_window(apple_coordinate)
    pygame.quit()


if __name__ == "__main__":
    main()