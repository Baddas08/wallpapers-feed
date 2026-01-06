import json
import requests
from PIL import Image
from io import BytesIO
import os
import random

# Quelques fonds d’écran libres de droits (JPEG par défaut)
wallpapers = [
    {"title": "Ciel étoilé", "url": "https://images.unsplash.com/photo-1506748686214-1"},
    {"title": "Ville cyberpunk", "url": "https://images.pexels.com/photos/313782/pexels-photo-313782.jpeg"},
    {"title": "Plage tropicale", "url": "https://images.unsplash.com/photo-1507525428034-1"}
]

# Choisir une image au hasard
image = random.choice(wallpapers)

# Télécharger l’image
response = requests.get(image["url"])
img = Image.open(BytesIO(response.content))

# Redimensionner en portrait 1080x1920
img = img.resize((1080, 1920))

# Créer dossier wallpapers si inexistant
os.makedirs("wallpapers", exist_ok=True)

# Sauvegarder en PNG
filename = f"wallpapers/{image['title'].replace(' ', '_').lower()}.png"
img.save(filename, "PNG")

# Charger le fichier JSON existant
with open("images.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ajouter l’image au flux
data.append({"title": image["title"], "url": filename})

# Sauvegarder le JSON mis à jour
with open("images.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Image ajoutée :", image["title"])
