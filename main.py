import pygame
import random

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = "right"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "right":
            new_head = (head_x + 10, head_y)
        elif self.direction == "left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "down":
            new_head = (head_x, head_y + 10)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, new_direction):
        if (self.direction == "right" and new_direction != "left") or \
           (self.direction == "left" and new_direction != "right") or \
           (self.direction == "up" and new_direction != "down") or \
           (self.direction == "down" and new_direction != "up"):
            self.direction = new_direction

    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= width or head_y < 0 or head_y >= height

    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def eat(self, food):
        return self.body[0] == food.position

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))


class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate_new_position()

    def generate_new_position(self, snake):
        while True:
            self.position = (random.randint(0, self.width - 10) // 10 * 10, random.randint(0, self.height - 10) // 10 * 10)
            if self.position not in snake.body:
                break

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], 10, 10))


class Game:
    def __init__(self, width=400, height=400):
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

            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
