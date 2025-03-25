import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simple Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake initial position and size
snake_x = window_width / 2
snake_y = window_height / 2
snake_size = 10
snake_list = []
snake_length = 1

# Food initial position
food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

# Game variables
game_over = False
x_change = 0
y_change = 0
clock = pygame.time.Clock()
snake_speed = 15


def display_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, green, [x, y, snake_size, snake_size])


# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_size
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_size
                x_change = 0

    # Check for boundaries
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    snake_x += x_change
    snake_y += y_change

    window.fill(black)
    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    display_snake(snake_list)

    pygame.display.update()

    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

pygame.quit()
quit()
