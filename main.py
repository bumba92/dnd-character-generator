character = {
    "name": "Thorin",
    "class": "Fighter",
    "Level": 5,
    "race": "Dwarf",
    "languages": ["Common", "Dwarvish"],
    "equipment": ["Battleaxe", "Shield", "Chainmail"],
}

#Werte abrufen:

print(character["languages"])  # Ausgabe: ['Common', 'Dwarvish']

print(character["equipment"][0])

for item in character["equipment"]:
    print(f"-{item}")