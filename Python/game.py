import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and Food
snake = [(100, 100), (90, 100), (80, 100)]  # Initial position
food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

direction = "RIGHT"
change_to = direction
clock = pygame.time.Clock()

# Game Over function
def game_over():
    font = pygame.font.SysFont(None, 35)
    text = font.render("Game Over! Press R to Restart", True, RED)
    screen.blit(text, (WIDTH // 10, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

# Main Game Loop
running = True
while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_r:  # Restart on "R"
                snake = [(100, 100), (90, 100), (80, 100)]
                direction = "RIGHT"
                change_to = direction

    # Update direction
    direction = change_to

    # Move the snake
    x, y = snake[0]
    if direction == "UP":
        y -= GRID_SIZE
    elif direction == "DOWN":
        y += GRID_SIZE
    elif direction == "LEFT":
        x -= GRID_SIZE
    elif direction == "RIGHT":
        x += GRID_SIZE

    # New head position
    new_head = (x, y)

    # Check for collisions
    if new_head in snake or x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        game_over()
        snake = [(100, 100), (90, 100), (80, 100)]  # Reset snake
        direction = "RIGHT"
        change_to = direction
        food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
    
    # Move snake forward
    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == food:
        food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
    else:
        snake.pop()  # Remove tail if no food is eaten

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Refresh screen
    pygame.display.flip()
    clock.tick(10)  # Adjust speed

pygame.quit()