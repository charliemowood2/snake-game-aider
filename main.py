import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(width, height)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction("up")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("down")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("left")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction("right")

            self.snake.move()
            if self.snake.check_collision(self.width, self.height) or self.snake.check_self_collision():
                running = False
            if self.snake.eat(self.food):
                self.food.generate_new_position(self.snake)

            self.screen.fill((0, 0, 0))  # Black background
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(10)  # Adjust speed here

        pygame.quit()

