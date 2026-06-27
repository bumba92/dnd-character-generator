def create_character(name, character_class, level):
    return {
        "name": name,
        "class": character_class,
        "level": level
    }

def print_character(character):
    print(f"\n--- Charakter ---")
    print(f"Name: {character['name']}")
    print(f"Klasse: {character['class']}")
    print(f"Level: {character['level']}")

name = input("Charaktername: ")
character_class = input("Charakterklasse: ")
level = int(input("Level: "))

character = create_character(name, character_class, level)
print_character(character)