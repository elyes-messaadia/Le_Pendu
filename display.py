import pygame

pygame.font.init()

GRAY=(127,127,127)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WIDTH,HEIGHT=800,800

font=pygame.font.SysFont(None, 30)

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

def display_game(screen, error, guessed_word, secret_word):
    screen.fill(GREEN)

    pygame.draw.line(screen, GRAY,(600,300),(600,500),width=5)
    pygame.draw.line(screen, GRAY,(550,500),(750,500),width=5)
    pygame.draw.line(screen, GRAY,(600,301),(700,301),width=5)
    pygame.draw.line(screen, GRAY,(700,330),(700,300),width=5)
    pygame.draw.line(screen, GRAY, (600, 340), (640, 300), width=5)
 
    x_start=200
    y_position=400

    for letters in secret_word:
      if letters in guessed_word:
        letter=font.render(letters,True,RED)
      else:
        letter=font.render("_",True,RED)

      screen.blit(letter,(x_start,y_position))
      x_start+=50
      
    if error>=1:
     pygame.draw.circle(screen, GRAY, (700, 350), 20, width=5)
    if error>=2:
     pygame.draw.line(screen, GRAY, (700, 370), (700, 410), width=5)
    if error>=3:
     pygame.draw.line(screen, GRAY, (700, 380), (660, 400), width=5)
    if error>=4:
     pygame.draw.line(screen, GRAY, (700, 380), (740, 400), width=5)
    if error>=5:
     pygame.draw.line(screen, GRAY, (700, 410), (680, 460), width=5)
    if error>=6:
     pygame.draw.line(screen, GRAY, (700, 410), (720, 460), width=5)


def display_personnalized(current_text, screen):
   screen.fill(RED)
   welcome_word=font.render("Here you can add a personnalized word to the game!",True,GREEN)
   screen.blit(welcome_word,(20,20))
   existant_words=font.render("List of existant words: ",True,GRAY)
   screen.blit(existant_words,(80,80))
   user_input=font.render(current_text,True,BLUE)
   screen.blit(user_input,(50,50))

def display_score(screen):
   screen.fill(BLUE)

