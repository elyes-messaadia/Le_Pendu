from word_manager import choisir_mot_aleatoire
from constant import *

class Game:
    def __init__(self, difficulte="moyen"):
        self.mot = choisir_mot_aleatoire()
        self.lettres_trouvees = set()
        self.lettres_ratees = set()
        self.difficulte = difficulte
        self.vies = self._get_vies(difficulte)
        self.score = 0
        self.termine = False
        self.gagne = False
    
    def _get_vies(self, difficulte):
        vies_map = {"facile": VIES_FACILE, "moyen": VIES_MOYEN, "difficile": VIES_DIFFICILE}
        return vies_map.get(difficulte, VIES_MOYEN)
    
    def proposer_lettre(self, lettre):
        """Propose une lettre"""
        lettre = lettre.upper()
        if lettre in self.lettres_trouvees or lettre in self.lettres_ratees:
            return False
        
        if lettre in self.mot:
            self.lettres_trouvees.add(lettre)
        else:
            self.lettres_ratees.add(lettre)
            self.vies -= 1
        
        self._verifier_fin()
        return True
    
    def _verifier_fin(self):
        """Vérifie si la partie est terminée"""
        if self.vies <= 0:
            self.termine = True
            self.gagne = False
        elif all(lettre in self.lettres_trouvees for lettre in self.mot):
            self.termine = True
            self.gagne = True
    
    def get_mot_affiche(self):
        """Retourne le mot avec _ pour les lettres non trouvées"""
        return ' '.join([lettre if lettre in self.lettres_trouvees else '_' for lettre in self.mot])