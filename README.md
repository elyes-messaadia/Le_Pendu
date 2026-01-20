# 🎮 Le Pendu - Projet Bar à Jeux

## 📝 Description
Ce projet est né d'un constat simple : lors de soirées entre amis, jouer au pendu sur un bout de papier déchiré manque de raffinement. En tant que passionné de jeux de société, ce programme a été développé pour offrir une expérience numérique élégante à vos invités.

L'objectif est de deviner un mot choisi aléatoirement parmi une liste. À chaque erreur, un élément du pendu est dessiné. Le jeu se termine quand le mot est trouvé ou que le dessin est complet.

## ✨ Fonctionnalités principales
* **Interface Graphique :** Développée avec la bibliothèque **Pygame**.
* **Gestion de Mots :** Lecture aléatoire depuis `mots.txt` (contenant au minimum 15 mots).
* **Menu Interactif :** Choix entre jouer ou insérer un nouveau mot dans le dictionnaire.
* **Système de Score :** Calcul des points et enregistrement dans un fichier `scores.txt` avec le nom du joueur.
* **Niveaux de Difficulté :** Possibilité de choisir la difficulté de la partie.
* **Tableau des Scores :** Affichage des meilleurs scores directement depuis le menu.

## 🛠️ Installation et Lancement

### Prérequis
* **Python 3.x**
* Bibliothèque **Pygame**

### Installation
1. Clonez le dépôt public :
   ```bash
   git clone [https://github.com/votre-nom/pendu.git](https://github.com/votre-nom/pendu.git)

   Installez Pygame : 
   ```
   pip install pygame
   ```