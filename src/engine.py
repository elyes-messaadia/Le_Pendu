import json
import random
import os

# --- FILE PATHS ---
# Since engine.py is in src/, we point to the data folder
WORDS_FILE = "data/mots.json"
SCORES_FILE = "data/scores.json"

def load_random_word():
    """Selects a random word from the JSON database."""
    try:
        with open(WORDS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return random.choice(data["mots"]).upper()
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback if the file is missing or empty
        return "PYTHON"

def add_new_word(new_word):
    """Adds a new word to the dictionary as required by the menu."""
    new_word = new_word.strip().upper()
    try:
        with open(WORDS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if new_word not in data["mots"]:
            data["mots"].append(new_word)
            with open(WORDS_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True
    except FileNotFoundError:
        return False
    return False

def save_score(player_name, score):
    """Saves the player's name and score in scores.json."""
    try:
        if os.path.exists(SCORES_FILE):
            with open(SCORES_FILE, "r", encoding="utf-8") as f:
                scores = json.load(f)
        else:
            scores = []

        scores.append({"name": player_name, "score": score})
        
        with open(SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, indent=4)
    except Exception as e:
        print(f"Error saving score: {e}")