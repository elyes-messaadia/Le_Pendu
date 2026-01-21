import pygame
from pygame.locals import *
from words_management import *
from display import *

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
running=True
background=GRAY
pygame.display.set_caption("Hangman Game")

current_state="MENU"
user_text=""
error=0
guessed_word=[]
list_word=save_words()
secret_word=choose_word(list_word)

while running:
    for event in pygame.event.get():
     if event.type==pygame.QUIT:
         running=False

     if event.type==KEYDOWN:

         if current_state=="MENU":
           if event.key==pygame.K_p:
             current_state="PERSONNALIZE"
           elif event.key==pygame.K_g:
              current_state="GAME"
           elif event.key==pygame.K_s:
              current_state="SCORES"
           
         elif current_state=="GAME":
             randomizer=save_words()
             word=choose_word(randomizer)
             print(word)

         
         elif current_state=="SCORES":
            pass

         elif current_state=="PERSONNALIZE":
            if event.key==pygame.K_RETURN:
             save_new_word(user_text)
             user_text=""
             current_state="MENU"

            elif event.key==pygame.K_BACKSPACE:
             user_text=user_text[:-1]
            
            elif event.key==pygame.K_1:
               reset_words()

            else:
             if len(event.unicode)>0:
              user_text+=event.unicode

    if current_state=="MENU":
         display_menu(screen)

    elif current_state=="GAME":
         display_game(screen, error, guessed_word, secret_word)

    elif current_state=="SCORES":
         display_score(screen)
         
    elif current_state=="PERSONNALIZE":
         display_personnalized(user_text, screen)

    pygame.display.update()

pygame.quit()