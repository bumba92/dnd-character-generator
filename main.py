import json
from fpdf import FPDF

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

def get_level_input():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 20:
                print("Level muss zwischen 1 und 20 liegen!")
            else:
                break
                return level
        except ValueError:
                print("Bitte eine Ganze Zahl eingeben!")
    return level

def create_character_from_input():
    tmp_char = Character(
        input("Name: "),
        select_option(data, "race", "Wähle eine Rasse")["name"],
        select_option(data, "class", "Wähle eine Klasse")["name"],
        get_level_input(),
        select_option(data, "background", "Wähle einen Hintergrund")["name"]
    )
    return tmp_char

def load_data():
    with open("data/Character_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def select_option(data, category, prombt):
    options = data[category]
    n = len(options)

    for i, option in enumerate(options):
        print(f"{i+1}. {option['name']}") 
    while True:
        try:
            choice = int(input(f"{prombt} (1-{n}): "))
            if 1 <= choice <= n:
                return options[choice - 1]
            else:
                print(f"Bitte wähle eine Zahl zwischen 1 und {n}!")
        except ValueError:
            print("Bitte eine Ganze Zahl eingeben!")

def generate_pdf(character):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.cell(text="D&D Charakterbogen")
    pdf.set_font("Helvetica", size=12)
    pdf.ln(10)
    pdf.cell(text=f"Name: {hero_1.name}")
    pdf.ln(10)
    pdf.cell(text=f"Rasse: {hero_1.race}")
    pdf.ln(10)
    pdf.cell(text=f"Klasse: {hero_1.character_class}")
    pdf.ln(10)
    pdf.cell(text=f"Level: {hero_1.level}")
    pdf.ln(10)
    pdf.cell(text=f"Hintergrund: {hero_1.background}")
    pdf.ln(10)
    pdf.cell(text=f"Proficiency Bonus: {hero_1.get_PB()}")

    pdf.output(f"{hero_1.name}_character_sheet.pdf")

data = load_data()
# races = select_option(data, "race", "Wähle eine Rasse")
# classes = select_option(data, "class", "Wähle eine Klasse")
# background = select_option(data, "background", "Wähle einen Hintergrund")




hero_1 = create_character_from_input()
hero_1.describe()
print (f"Proficiency Bonus: {hero_1.get_PB()}")
print("\n")

generate_pdf(hero_1)

