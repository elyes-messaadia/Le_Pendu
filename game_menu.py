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
   txt_title=font.render("Hangman Game",True,GREEN)
   txt_game=font.render("Tap G to play",True,GREEN)
   txt_scores=font.render("Tap S to see scores",True,GREEN)
   txt_personnalize=font.render("Tap P to add your customized word!",True, GREEN)

   screen.blit(txt_title,(20,20))
   screen.blit(txt_game,(50,50))
   screen.blit(txt_scores,(80,80))
   screen.blit(txt_personnalize,(110,110))

def add_word(current_text, screen):
   screen.fill(RED)
   welcome_word=font.render("Here you can add a personnalized word to the game!",True,GREEN)
   screen.blit(welcome_word,(20,20))
   existant_words=font.render("List of existant words: ",True,GRAY)
   screen.blit(existant_words,(80,80))
   user_input=font.render(current_text,True,BLUE)
   screen.blit(user_input,(50,50))

 
def play_game(screen, error, guessed_word, secret_word):
    screen.fill(GREEN)

    x_start=200
    y_position=400

    for letters in secret_word:
      if letters in guessed_word:
        letter=font.render(letters,True,RED)
      else:
        letter=font.render("_",True,RED)

      screen.blit(letter,(x_start,y_position))
      x_start+=50
      
    poteau=pygame.draw.line(screen, GRAY,(600,300),(600,500),width=5)
    base=pygame.draw.line(screen, GRAY,(550,500),(750,500),width=5)
    poteau_straight=pygame.draw.line(screen, GRAY,(600,301),(700,301),width=5)
    fall_line=pygame.draw.line(screen, GRAY,(700,330),(700,300),width=5)
    traverse = pygame.draw.line(screen, GRAY, (600, 340), (640, 300), width=5)

    if error>=1:
     head = pygame.draw.circle(screen, GRAY, (700, 350), 20, width=5)
    elif error>=2:
     body = pygame.draw.line(screen, GRAY, (700, 370), (700, 410), width=5)
    elif error>=3:
     arm_left = pygame.draw.line(screen, GRAY, (700, 380), (660, 400), width=5)
    elif error>=4:
     arm_right = pygame.draw.line(screen, GRAY, (700, 380), (740, 400), width=5)
    elif error>=5:
     leg_left = pygame.draw.line(screen, GRAY, (700, 410), (680, 460), width=5)
    elif error>=6:
     leg_right = pygame.draw.line(screen, GRAY, (700, 410), (720, 460), width=5)
  
   



def see_score(screen):
   screen.fill(BLUE)

def quit():
   pass

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
         play_game(screen, error, guessed_word, secret_word)
    elif current_state=="SCORES":
         see_score(screen)
    elif current_state=="PERSONNALIZE":
         add_word(user_text, screen)

    pygame.display.update()

pygame.quit()