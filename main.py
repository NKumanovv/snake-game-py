import pygame
import random
from models import Snake

def main():
    pygame.init()
    
    width = 800
    height = 600
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    
    clock = pygame.time.Clock()
    block_size = 10
    snake_speed = 15

    snake = Snake(block_size, (width, height))
    
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    running = True
    game_over = False

    while running:
        while game_over:
            display.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 40)
            msg = font.render("Game Over! Press Q to Quit or C to Play Again", True, (255, 0, 0))
            display.blit(msg, [width / 10, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False
                    if event.key == pygame.K_c:
                        main()
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        snake.move()

        if snake.check_collision():
            game_over = True

        head_x, head_y = snake.body[0]
        if head_x == food_x and head_y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        else:
            snake.body.pop()

        display.fill((0, 0, 0))
        pygame.draw.rect(display, (0, 255, 0), [food_x, food_y, block_size, block_size])
        
        for block in snake.body:
            pygame.draw.rect(display, (255, 255, 255), [block[0], block[1], block_size, block_size])

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    main()