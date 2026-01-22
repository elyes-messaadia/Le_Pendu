import pygame
import json
import random

# --- SETTINGS ---
WHITE = (255, 255, 255)
RED = (255, 100, 100)
GRAY = (40, 44, 52)
WIDTH, HEIGHT = 800, 600

# --- DATA LOADING ---
def load_random_word():
    try:
        # Load from JSON as requested
        with open("data/mots.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return random.choice(data["mots"]).upper()
    except:
        return "PYTHON"

# --- INITIALIZATION ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman - Keyboard Test")
font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 24)

# Game State
secret_word = load_random_word()
guessed_letters = []
wrong_letters = []
game_running = True

# --- MAIN LOOP ---
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        
        # Capture keyboard input
        if event.type == pygame.KEYDOWN:
            # event.unicode gets the character of the key pressed
            letter = event.unicode.upper()
            
            if letter.isalpha() and letter not in guessed_letters and letter not in wrong_letters:
                if letter in secret_word:
                    guessed_letters.append(letter) # Correct letter revealed
                else:
                    wrong_letters.append(letter) # Wrong letter recorded

    # --- DRAWING ---
    screen.fill(GRAY)
    
    # 1. Display the word with underscores
    display_str = ""
    for char in secret_word:
        if char in guessed_letters:
            display_str += char + " "
        else:
            display_str += "_ "
    
    word_surface = font.render(display_str, True, WHITE)
    screen.blit(word_surface, (WIDTH//2 - word_surface.get_width()//2, 200))
    
    # 2. Display Wrong Letters (Feedback to see if keys work!)
    wrong_text = "Mistakes: " + ", ".join(wrong_letters)
    wrong_surface = small_font.render(wrong_text, True, RED)
    screen.blit(wrong_surface, (20, 20))

    pygame.display.flip()

pygame.quit()