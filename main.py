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

class Character:
    def __init__(self, name, race, character_class, level, background):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.background = background

    def describe(self):
        print(
            f"Name: {self.name}\n"
            f"Rasse: {self.race}\n"
            f"Klasse: {self.character_class}\n"
            f"Level: {self.level}\n"
            f"Hintergrund: {self.background}"
        )

    def get_PB(self):
        return (self.level - 1) // 4 + 2
    
hero_1 = Character("Aragorn", "Mensch", "Krieger", 5, "König von Gondor")
hero_2 = Character("Gandalf", "Maia", "Zauberer", 20, "Weiser Mentor")

hero_1.describe()
print (f"Proficiency Bonus: {hero_1.get_PB()}")
print("\n")
hero_2.describe()
print (f"Proficiency Bonus: {hero_2.get_PB()}")

