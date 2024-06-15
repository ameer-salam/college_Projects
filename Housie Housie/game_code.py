import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Housie Housie Number Display")

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
white = (255, 255, 255)
grey = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 48)  # Increased font size for numbers
small_font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 48)
subtitle_font = pygame.font.Font(None, 24)

# Grid dimensions
cols = 10
rows = 9

def calculate_cell_size(screen_width, screen_height):
    cell_width = screen_width // cols
    cell_height = (screen_height - 200) // rows  # Adjusted to make space for input and prompt
    return cell_width, cell_height

cell_width, cell_height = calculate_cell_size(screen_width, screen_height)

# Generate numbers
numbers = list(range(1, 91))

# Store the status of each number
called_numbers = set()
history = []  # For undo/redo functionality
redo_stack = []

# Function to draw the grid and numbers
def draw_grid():
    for i in range(rows):
        for j in range(cols):
            number = i * cols + j + 1
            rect = pygame.Rect(j * cell_width, i * cell_height + 100, cell_width, cell_height)
            if number in called_numbers:
                pygame.draw.rect(screen, green, rect)
                text = font.render(str(number), True, black)
            else:
                pygame.draw.rect(screen, yellow, rect)
                text = font.render(str(number), True, red)
            pygame.draw.rect(screen, red, rect, 2)
            screen.blit(text, text.get_rect(center=rect.center))

# Function to draw the input box and prompt
def draw_input_box(input_text, prompt_text):
    input_box = pygame.Rect(10, screen_height - 80, screen_width - 20, 30)
    pygame.draw.rect(screen, white, input_box)
    pygame.draw.rect(screen, black, input_box, 2)
    input_text_surface = small_font.render(input_text, True, black)
    screen.blit(input_text_surface, (input_box.x + 5, input_box.y + 5))
    
    prompt_surface = small_font.render(prompt_text, True, white)
    screen.blit(prompt_surface, (10, screen_height - 120))

# Function to draw the title
def draw_title():
    title_surface = title_font.render("IEEE Housie Housie", True, white)
    screen.blit(title_surface, (10, 10))
    
    subtitle_surface = subtitle_font.render("Game developed by Ameer Salam", True, white)
    screen.blit(subtitle_surface, (10, 50))

# Main loop
running = True
input_number = ""
prompt_text = "Enter a number: "
awaiting_confirmation = False
number_to_confirm = None

while running:
    screen.fill(black)
    draw_title()
    draw_grid()
    draw_input_box(input_number, prompt_text)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            cell_width, cell_height = calculate_cell_size(screen_width, screen_height)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not awaiting_confirmation:
                    try:
                        num = int(input_number)
                        if 1 <= num <= 90:
                            number_to_confirm = num
                            prompt_text = f"Should I change the color of the box number {num}? (y/n)"
                            awaiting_confirmation = True
                        input_number = ""
                    except ValueError:
                        input_number = ""
                else:
                    if input_number.lower() == 'y':
                        if number_to_confirm not in called_numbers:
                            called_numbers.add(number_to_confirm)
                            history.append(number_to_confirm)
                            redo_stack.clear()
                    prompt_text = "Enter a number: "
                    awaiting_confirmation = False
                    input_number = ""
            elif event.key == pygame.K_BACKSPACE:
                input_number = input_number[:-1]
            elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if history:
                    num = history.pop()
                    called_numbers.remove(num)
                    redo_stack.append(num)
            elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if redo_stack:
                    num = redo_stack.pop()
                    called_numbers.add(num)
                    history.append(num)
            else:
                input_number += event.unicode

pygame.quit()
sys.exit()
