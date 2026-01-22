import random

def lire_mots(fichier="mots.txt"):
    """Lit tous les mots du fichier"""
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            mots = [ligne.strip().upper() for ligne in f if ligne.strip()]
        return mots
    except FileNotFoundError:
        return []

def choisir_mot_aleatoire(fichier="mots.txt"):
    """Choisit un mot aléatoire"""
    mots = lire_mots(fichier)
    if mots:
        return random.choice(mots)
    return None

def ajouter_mot(mot, fichier="mots.txt"):
    """Ajoute un mot au fichier"""
    with open(fichier, 'a', encoding='utf-8') as f:
        f.write(mot.strip().upper() + '\n')