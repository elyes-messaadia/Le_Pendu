from constant import *

def lire_scores(fichier="scores.txt"):
    """Lit les scores depuis le fichier"""
    scores = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                if ',' in ligne:
                    nom, score = ligne.strip().split(',')
                    scores.append((nom, int(score)))
    except FileNotFoundError:
        pass
    return sorted(scores, key=lambda x: x[1], reverse=True)

def sauvegarder_score(nom, score, fichier="scores.txt"):
    """Sauvegarde un nouveau score"""
    with open(fichier, 'a', encoding='utf-8') as f:
        f.write(f"{nom},{score}\n")

def calculer_score(lettres_trouvees, mot_complet, difficulte):
    """Calcule le score en fonction de la difficulté"""
    bonus = {"facile": BONUS_FACILE, "moyen": BONUS_MOYEN, "difficile": BONUS_DIFFICILE}
    score = lettres_trouvees * POINTS_LETTRE
    if mot_complet:
        score += POINTS_MOT_COMPLET
    return int(score * bonus.get(difficulte, 1))