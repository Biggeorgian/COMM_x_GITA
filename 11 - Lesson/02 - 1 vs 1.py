import random

charachter_stats = [
    {
        "name": "გიგანტი",
        "health": 110,
        "abilities": [
            {"name": "მუშტი", "power": 30},
            {"name": "კომბალი", "power": 27},
            {"name": "წიხლი", "power": 25}
        ]
    },
    {
        "name": "სწრაფი",
        "health": 90,
        "abilities": [
            {"name": "სილა", "power": 29},
            {"name": "შალაბანი", "power": 32},
            {"name": "ქვიშა თვალებში", "power": 18}
        ]
    },
    {
        "name": "მოქნილი",
        "health": 90,
        "abilities": [
            {"name": "შპაგატიდან არტყმა", "power": 35},
            {"name": "ჭიტლაყი", "power": 20},
            {"name": "ყურში ჩაფეთება", "power": 15}
        ]
    },
    {
        "name": "აქილევსი",
        "health": 100,
        "abilities": [
            {"name": "კეფაში მოდება", "power": 20},
            {"name": "წვინტლის ბურთულა", "power": 35},
            {"name": "ცხვირის გაბრტყელება", "power": 30}
        ]
    },
    {
        "name": "გველაძუა",
        "health": 90,
        "abilities": [
            {"name": "თვალში ტუკვება", "power": 25},
            {"name": "წვივში ძგერება", "power": 29},
            {"name": "ბურნუთის შეყრა", "power": 15}
        ]
    }
]


class Character:
    def __init__(self, name, health, abilities):
        self.name = name
        self.health = health
        self.abilities = abilities

    def __repr__(self):
        return f"{self.name} (Health: {self.health})"

    def display_abilities(self):
        print(f"{self.name}-ის შესაძლებლობები ---")
        for i, ability in enumerate(self.abilities, 1):
            print(f"{i}. {ability['name']} (ძალა: {ability['power']})")

    def attack(self, opponent, ability_choice):
        chosen_ability = self.abilities[ability_choice - 1]
        ability_name = chosen_ability['name']
        base_power = chosen_ability['power']

        damage = round(random.uniform(1, 1.5) * base_power)
        opponent.health -= damage

        print(f"⚔️ {self.name}-მა გამოიყენა '{ability_name}' და {opponent.name}-ს მიაყენა {damage} ზიანი!")
        if opponent.health < 0:
            opponent.health = 0

    def is_alive(self):
        return self.health > 0

def select_character(player_num):
    for i, char_data in enumerate(charachter_stats, 1):
        ability_names = [ability['name'] for ability in char_data['abilities']]
        print(f"{i}. {char_data['name']}: (შესაძლებლობები: {', '.join(ability_names)})")

    while True:
        try:
            choice = int(input(f"მოთამაშე #{player_num}, მიუთითეთ ნომერი: "))
            print(" ")
            if 1 <= choice <= len(charachter_stats):
                selected_data = charachter_stats[choice - 1]
                return Character(
                    name=selected_data['name'],
                    health=selected_data['health'],
                    abilities=selected_data['abilities']
                )
            else:
                print("არასწორი ნომერი, სცადეთ თავიდან.")
        except ValueError:
            print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")

def battle(player1, player2):
    print(f"💥 ბრძოლა იწყება: {player1.name} vs {player2.name}! 💥")

    attacker, defender = player1, player2
    while player1.is_alive() and player2.is_alive():
        print(f"მიმდინარე მდგომარეობა: {player1} | {player2}\n")
        attacker.display_abilities()

        while True:
            try:
                ability_choice = int(input(f"\n{attacker.name}-ის სვლა. აირჩიეთ შეტევა: "))
                if 1 <= ability_choice <= len(attacker.abilities):
                    break
                else:
                    print("არასწორი ნომერი.")
            except ValueError:
                print("გთხოვთ, შეიყვანოთ რიცხვი.")

        attacker.attack(defender, ability_choice)
        attacker, defender = defender, attacker

    print("\n" + "=" * 30)
    winner = player1 if player1.is_alive() else player2
    print(f"🎉 ბრძოლა დასრულდა! გამარჯვებულია {winner.name}! 🎉")

player1 = select_character(1)
player2 = select_character(2)
battle(player1, player2)