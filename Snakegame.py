import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set display dimensions
width = 600
height = 400

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Set up font
font = pygame.font.SysFont(None, 25)

# Define the snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[300, 200]]
        self.radius = 10
        self.dx = 0
        self.dy = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, white, element, self.radius)

    def move(self):
        if self.size > 1:
            for i in range(self.size - 1, 0, -1):
                self.elements[i] = list(self.elements[i - 1])
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat_food(self):
        self.size += 1
        self.elements.append(self.elements[-1].copy())  # Append a copy of the last element

    def check_collision(self, box_x, box_y, box_width, box_height):
        head_x, head_y = self.elements[0]
        if head_x < box_x or head_x > box_x + box_width - 2*self.radius:
            return True
        if head_y < box_y or head_y > box_y + box_height - 2*self.radius:
            return True
        return False

# Define the food class
class Food:
    def __init__(self, box_x, box_y, box_width, box_height):
        self.position = [random.randint(box_x + 20, box_x + box_width - 20), random.randint(box_y + 20, box_y + box_height - 20)]
        self.is_on_screen = True

    def draw(self):
        pygame.draw.circle(screen, red, self.position, 5)

# Function to display the score
def show_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

# Function to display message
def message_display(text):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.update()

# Main game loop
def game_loop():
    
    # Set box parameters
    box_width = width // 2
    box_height = height // 2
    box_x = (width - box_width) // 2
    box_y = (height - box_height) // 2

    # Create snake and food objects
    snake = Snake()
    food = Food(box_x, box_y, box_width, box_height)

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                quit()
                # return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.dx = -10
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake.dx = 10
                    snake.dy = 0
                elif event.key == pygame.K_UP:
                    snake.dy = -10
                    snake.dx = 0
                elif event.key == pygame.K_DOWN:
                    snake.dy = 10
                    snake.dx = 0

        # Move snake
        snake.move()

        # Check if snake collides with the box
        if snake.check_collision(box_x, box_y, box_width, box_height):
            screen.fill(black)
            message_display("Game Over! Press C to Retry or Q to Quit")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # pygame.quit()
                        quit()
                        # return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            game_loop()
                        elif event.key == pygame.K_q:
                            # pygame.quit()
                            quit()
                            # return 

        # Check for collision with food
        if abs(snake.elements[0][0] - food.position[0]) < snake.radius + 5 and abs(snake.elements[0][1] - food.position[1]) < snake.radius + 5:
            snake.eat_food()
            food.position = [random.randint(box_x + 20, box_x + box_width - 20), random.randint(box_y + 20, box_y + box_height - 20)]

        # Draw everything
        screen.fill(black)
        pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 2)
        snake.draw()
        food.draw()
        show_score(snake.size - 1)

        pygame.display.update()
        clock.tick(20)
    return
    # Return to the calling function
    