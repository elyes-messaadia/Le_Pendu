import pygame

pygame.font.init()

BLACK=(0,0,0)
RED=(255,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
WIDTH,HEIGHT=800,800

font_titles=pygame.font.Font("chalk.ttf",60)
font_text=pygame.font.Font("chalk.ttf",40)

background=pygame.image.load("background.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
font=pygame.font.SysFont(None, 30)

def display_menu(screen):
   screen.blit(background,(0,0))
   txt_title=font_titles.render("HANGMAN GAME",True,BLUE)
   txt_game=font_text.render("[G] TO PLAY",True,GREEN)
   txt_scores=font_text.render("[S] TO SEE SCORES",True,BLACK)
   txt_personnalize=font_text.render("[P] TO ADD CUSTOMIZED WORDS",True, WHITE)

   screen.blit(txt_title,(100,80))
   screen.blit(txt_game,(100,200))
   screen.blit(txt_scores,(100,300))
   screen.blit(txt_personnalize,(100,400))

def display_game(screen, error, guessed_word, secret_word):
    screen.blit(background,(0,0))

    pygame.draw.line(screen, BLACK,(600,300),(600,500),width=5)
    pygame.draw.line(screen, BLACK,(550,500),(750,500),width=5)
    pygame.draw.line(screen, BLACK,(600,301),(700,301),width=5)
    pygame.draw.line(screen, BLACK,(700,330),(700,300),width=5)
    pygame.draw.line(screen, BLACK, (600, 340), (640, 300), width=5)
 
    x_start=200
    y_position=400

    for letters in secret_word:
      if letters in guessed_word:
        letter=font.render(letters,True,WHITE)
      else:
        letter=font.render("_",True,WHITE)

      screen.blit(letter,(x_start,y_position))
      x_start+=50
      
    if error>=1:
     pygame.draw.circle(screen, BLACK, (700, 350), 20, width=5)
    if error>=2:
     pygame.draw.line(screen, BLACK, (700, 370), (700, 410), width=5)
    if error>=3:
     pygame.draw.line(screen, BLACK, (700, 380), (660, 400), width=5)
    if error>=4:
     pygame.draw.line(screen, BLACK, (700, 380), (740, 400), width=5)
    if error>=5:
     pygame.draw.line(screen, BLACK, (700, 410), (680, 460), width=5)
    if error>=6:
     pygame.draw.line(screen, BLACK, (700, 410), (720, 460), width=5)


def display_victory(screen):
  screen.blit(background,(0,0))
  victory_word=font_titles.render("YOU WON!",True,GREEN)
  screen.blit(victory_word,(200,80))

def display_game_over(screen,secret_word):
  screen.blit(background,(0,0))
  game_over_word=font_titles.render("YOU LOST!",True,RED)
  screen.blit(game_over_word,(200,80))
  hidden_word=font_text.render(f"THE WORD WAS: {secret_word}",True,GREEN)
  screen.blit(hidden_word,(20,200))

def display_personnalized(current_text, screen):
   screen.blit(background,(0,0))
   welcome_word=font_text.render("HERE YOU CAN ADD WORDS!",True,GREEN)
   screen.blit(welcome_word,(100,80))
   existant_words=font_text.render("LIST OF EXISTANT WORDS: ",True,BLUE)
   screen.blit(existant_words,(50,200))
   user_input=font_titles.render(current_text,True,WHITE)
   screen.blit(user_input,(50,50))

def display_score(screen):
    screen.blit(background,(0,0))
    scores_titles=font_titles.render("YOUR SCORE: ",True,BLACK)
    screen.blit(scores_titles,(50,100))


