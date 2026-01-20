import random
DEFAULTS_WORDS=["Banane", "Chocolat", "Fraise", "Clafoutis", "Tartelette", 
    "Opéra", "Charlotte", "Meringue", "Macarons", "Rose", 
    "Sirop", "Tiramisu", "Café", "Cannelle", "Vanille"
]

def save_words():
 try:
    clean_word=[]
    with open("mots.txt", "r",encoding="utf-8") as file:
     for lines in file:
       clean_words=lines.strip()
       if clean_words:
          clean_word.append(clean_words)
 except FileNotFoundError:
   print("Error, No such files 'mots.txt'")
   return ["ERROR"]
 return clean_word

def reset_words():
  try:
    with open("mots.txt","w",encoding="utf-8") as file:
      for words in DEFAULTS_WORDS:
        file.write(words+"\n")
  except IOError:
    print("Failed to reinitialize")
    
         
    
def choose_word(lists):
   if lists:
    return random.choice(lists)
   return "NOTHING"

def save_new_word(new_word):
   with open("mots.txt", "a", encoding="utf-8") as file:
      file.write("\n"+new_word)
      
