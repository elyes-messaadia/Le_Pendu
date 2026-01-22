import pygame
from constant import *

def afficher_mot(screen, mot_affiche, y=200):
    """Affiche le mot avec les lettres trouvées"""
    font = pygame.font.Font(None, 72)
    texte = font.render(mot_affiche, True, NOIR)
    rect = texte.get_rect(center=(LARGEUR//2, y))
    screen.blit(texte, rect)

def afficher_lettres_ratees(screen, lettres_ratees, y=400):
    """Affiche les lettres ratées"""
    font = pygame.font.Font(None, 36)
    texte = font.render(f"Lettres ratées: {' '.join(sorted(lettres_ratees))}", True, ROUGE)
    rect = texte.get_rect(center=(LARGEUR//2, y))
    screen.blit(texte, rect)

def afficher_vies(screen, vies, x=50, y=50):
    """Affiche le nombre de vies"""
    font = pygame.font.Font(None, 48)
    texte = font.render(f"Vies: {vies}", True, NOIR)
    screen.blit(texte, (x, y))

def afficher_score(screen, score, x=600, y=50):
    """Affiche le score"""
    font = pygame.font.Font(None, 48)
    texte = font.render(f"Score: {score}", True, NOIR)
    screen.blit(texte, (x, y))