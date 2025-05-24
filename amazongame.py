import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Game by Sanket Kokate")

# Fonts and Colors
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Show text on screen
def show_message(message, color, y_offset=0):
    text = big_font.render(message, True, color)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, rect)
    pygame.display.flip()

# Main game loop
def play_game():
    screen.fill(BLACK)
    show_message("Wait for GREEN...", WHITE)
    pygame.display.flip()
    pygame.time.wait(random.randint(2000, 5000))

    screen.fill(GREEN)
    pygame.display.flip()
    start_time = time.time()

    reacted = False
    while not reacted:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                reaction_time = time.time() - start_time
                screen.fill(BLACK)
                show_message(f"Time: {reaction_time:.3f} sec", WHITE)
                pygame.time.wait(2000)
                reacted = True

# Main loop
running = True
while running:
    screen.fill(BLACK)
    show_message("Press SPACE to Start", WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_game()

pygame.quit()