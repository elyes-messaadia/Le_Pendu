<div align="center">

# 🎮 Le Pendu - Projet Bar à Jeux

### *Une expérience numérique élégante pour vos soirées entre amis*

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-required-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

---

</div>

## 📖 À Propos

Ce projet est né d'un constat simple : lors de soirées entre amis, jouer au pendu sur un bout de papier déchiré manque de raffinement. En tant que passionné de jeux de société, ce programme a été développé pour offrir une **expérience numérique élégante** à vos invités.

### 🎯 Objectif du Jeu

Devinez un mot choisi aléatoirement parmi une liste. À chaque erreur, un élément du pendu est dessiné. Le jeu se termine quand :
- ✅ Le mot est trouvé (victoire !)
- ❌ Le dessin du pendu est complet (défaite)

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| 🖼️ **Interface Graphique** | Interface moderne développée avec **Pygame** |
| 📚 **Gestion de Mots** | Lecture aléatoire depuis `mots.txt` (15+ mots) |
| 🎯 **Menu Interactif** | Jouer ou ajouter de nouveaux mots facilement |
| 🏆 **Système de Score** | Enregistrement des scores avec nom du joueur |
| 📊 **Niveaux de Difficulté** | Adaptez le challenge à votre niveau |
| 📈 **Tableau des Scores** | Consultez les meilleurs performances |

---

## 🚀 Installation et Lancement

### 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :
- **Python 3.x** installé sur votre système
- La bibliothèque **Pygame**

### 📥 Installation

1. **Clonez le dépôt**
   ```bash
   git clone https://github.com/elyes-messaadia/Le_Pendu.git
   cd Le_Pendu
   ```

2. **Installez les dépendances**
   ```bash
   pip install pygame
   ```

### ▶️ Lancement

Démarrez le jeu avec la commande suivante :

```bash
python main.py
```

---

## 📂 Structure du Projet

```
Le_Pendu/
│
├── 📄 main.py              # Point d'entrée et boucle de jeu principale
├── 📄 README.md            # Documentation du projet
│
├── 📁 assets/              # Ressources graphiques
│   ├── fonts/              # Polices de caractères
│   └── images/             # Images et sprites
│
├── 📁 data/                # Données du jeu
│   ├── mots.txt            # Liste des mots à deviner
│   └── scores.txt          # Archive des scores des joueurs
│
└── 📁 src/                 # Code source
    ├── engine.py           # Logique métier du jeu
    └── ui.py               # Interface utilisateur
```

---

## 🎯 Compétences Développées

Ce projet permet de travailler sur :

- ⚙️ **Configuration d'environnement** : Mise en place d'un environnement de développement Python
- 🎨 **Interfaces graphiques** : Développement d'UI avec Pygame
- 💼 **Logique métier** : Gestion de fichiers, algorithmes de jeu
- 📊 **Gestion de données** : Lecture/écriture de fichiers, persistence des scores
- 🏗️ **Architecture logicielle** : Organisation modulaire du code

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- 🐛 Signaler des bugs
- 💡 Proposer de nouvelles fonctionnalités
- 🔧 Soumettre des pull requests

---

## 📜 License

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.

---

<div align="center">

**Développé avec ❤️ pour des soirées jeux inoubliables**

⭐ Si vous aimez ce projet, n'hésitez pas à lui donner une étoile !

</div>