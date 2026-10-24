import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Battle Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 30)

# Player & Enemy Stats
player_health = 100
enemy_health = 100

# Function to draw health bars
def draw_health_bar(x, y, health, max_health):
    pygame.draw.rect(screen, RED, (x, y, 150, 20))
    pygame.draw.rect(screen, GREEN, (x, y, max(0, 150 * (health / max_health)), 20))

# Function to display text on screen
def draw_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Game loop
running = True
player_turn = True

while running:
    screen.fill(BLACK)

    # Draw health bars
    draw_health_bar(50, 50, player_health, 100)
    draw_health_bar(400, 50, enemy_health, 100)

    # Display player and enemy info
    draw_text("Player", 90, 20)
    draw_text("Enemy", 450, 20)
    draw_text(f"Player HP: {player_health}", 50, 80)
    draw_text(f"Enemy HP: {enemy_health}", 400, 80)

    if player_turn:
        draw_text("Your Turn! Press 1: Attack, 2: Heavy Attack", 50, 300)
    else:
        draw_text("Enemy is attacking...", 50, 300)

    # Check for game over
    if player_health <= 0:
        draw_text("You Lost! Press R to Restart", 200, 200, RED)
    elif enemy_health <= 0:
        draw_text("You Won! Press R to Restart", 200, 200, GREEN)

    pygame.display.flip()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player action (attack choices)
        if player_turn and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Light Attack
                damage = random.randint(5, 15)
                enemy_health -= damage
                player_turn = False
            elif event.key == pygame.K_2:  # Heavy Attack (Risky but stronger)
                damage = random.randint(10, 25)
                enemy_health -= damage
                player_turn = False

        # Restart game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            player_health = 100
            enemy_health = 100
            player_turn = True

    # Enemy Turn
    if not player_turn and enemy_health > 0:
        pygame.time.delay(1000)  # Delay for attack effect
        enemy_damage = random.randint(5, 20)
        player_health -= enemy_damage
        player_turn = True  # Switch back to player turn

    pygame.time.delay(100)  # Game speed control

pygame.quit()