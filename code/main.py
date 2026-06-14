// code
import pygame
import random
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Game Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20

# Colors (RGB)
BACKGROUND_COLOR = (30, 30, 30)
SNAKE_COLOR = (46, 204, 113)
FOOD_COLOR = (231, 76, 60)
TEXT_COLOR = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# 3. Game State Variables
snake = [(100, 100), (80, 100), (60, 100)]  # List of coordinates for snake segments
direction = (GRID_SIZE, 0)                  # Starting direction (moving right)
score = 0

def spawn_food():
    while True:
        x = random.randint(0, (SCREEN_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        if (x, y) not in snake:
            return (x, y)

food = spawn_food()
font = pygame.font.SysFont("arial", 24)

# 4. Main Game Loop
while True:
    # --- Event Handling (Inputs) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # --- Game Logic ---
    # Calculate new head position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions (Walls or Self)
    if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
        new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT or
        new_head in snake):
        print(f"Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    # Insert new head
    snake.insert(0, new_head)

    # Check if snake ate the food
    if new_head == food:
        score += 10
        food = spawn_food()
    else:
        # Remove the tail segment if it didn't eat food (keeps length the same)
        snake.pop()

    # --- Drawing Elements ---
    screen.fill(BACKGROUND_COLOR)

    # Draw Snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], GRID_SIZE - 2, GRID_SIZE - 2))

    # Draw Food
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food[0], food[1], GRID_SIZE - 2, GRID_SIZE - 2))

    # Draw Score
    score_surface = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_surface, (10, 10))

    # Update screen & set game speed (FPS)
    pygame.display.flip()
    clock.tick(10)  # Controls how fast the snake moves (10 frames per second)
