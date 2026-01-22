import pygame
from constant import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_titre = pygame.font.Font(None, 74)
        self.font_option = pygame.font.Font(None, 48)
    
    def afficher_menu_principal(self):
        """Affiche le menu principal et retourne le choix"""
        options = ["Jouer", "Ajouter un mot", "Scores", "Quitter"]
        return self._afficher_menu("JEU DU PENDU", options)
    
    def afficher_menu_difficulte(self):
        """Affiche le menu de sélection de difficulté"""
        options = ["Facile", "Moyen", "Difficile", "Retour"]
        return self._afficher_menu("Choisissez la difficulté", options)
    
    def _afficher_menu(self, titre, options):
        """Méthode générique pour afficher un menu"""
        selection = 0
        while True:
            self.screen.fill(BLANC)
            
            # Titre
            texte_titre = self.font_titre.render(titre, True, BLEU)
            rect_titre = texte_titre.get_rect(center=(LARGEUR//2, 100))
            self.screen.blit(texte_titre, rect_titre)
            
            # Options
            for i, option in enumerate(options):
                couleur = VERT if i == selection else NOIR
                texte = self.font_option.render(option, True, couleur)
                rect = texte.get_rect(center=(LARGEUR//2, 250 + i*60))
                self.screen.blit(texte, rect)
            
            pygame.display.flip()
            
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quitter"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selection = (selection - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selection = (selection + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        return options[selection].lower()