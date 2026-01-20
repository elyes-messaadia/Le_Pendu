import pygame
from pygame.locals import *
from words_management import *

pygame.init()

GRAY=(127,127,127)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WIDTH,HEIGHT=800,800

screen=pygame.display.set_mode((WIDTH,HEIGHT))
running=True
background=GRAY
font=pygame.font.SysFont(None, 30)
pygame.display.set_caption("Hangman Game")


def display_menu(screen):
   screen.fill(GRAY)

def add_word(current_text, screen):
   save_words()
   screen.fill(RED)
   welcome_word=font.render("Here you can add a personnalized word to the game!",True,GREEN)
   screen.blit(welcome_word,(20,20))
   existant_words=font.render("List of existant words: ",True,GRAY)
   screen.blit(existant_words,(80,80))
   user_input=font.render(current_text,True,BLUE)
   screen.blit(user_input,(50,50))

 
def play_game(screen):
   screen.fill(GREEN)
def see_score(screen):
   screen.fill(BLUE)
def quit():
   pass

current_state="MENU"
user_text=""
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
            pass
         
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
         play_game(screen)
    elif current_state=="SCORES":
         see_score(screen)
    elif current_state=="PERSONNALIZE":
         add_word(user_text, screen)

    pygame.display.update()

pygame.quit()