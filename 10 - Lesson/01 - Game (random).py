import random
import time

class Charachter:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, enemy):
        damage = random.uniform(0.6, 1.0) * self.strength
        damage = round(damage)
        enemy.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

class Warrior(Charachter):
    def __init__(self):
        super().__init__(name="ვაჟა", health=100, strength=30)
    def attack(self, enemy):
        damage = super().attack(enemy)
        print(f"⚔️ {self.name}მ ხმალი მოიქნია და "
              f"{enemy.name}ს {damage} სიცოცხლე აათალა!")

class Mage(Charachter):
    def __init__(self):
        super().__init__(name="ლუიზა", health=85, strength=35)
    def attack(self, enemy):
        damage = super().attack(enemy)
        print(f"✨ {self.name}მ {enemy.name} დაწყევლა "
              f"და {damage} ზიანი მიაყენა!")

class Archer(Charachter):
    def __init__(self):
        super().__init__(name="ნოდარი", health=70, strength=43)
    def attack(self, enemy):
        damage = super().attack(enemy)
        print(f"🏹 {self.name}ს ნასროლმა ისარმა {enemy.name}ს "
              f"{damage} სიცოცხლე მოაკლო!")

characters = [Warrior(), Archer(), Mage()]
enemy1, enemy2 = random.sample(characters, 2)

print(f"დღეს ერთმანეთს ებრძვიან: {enemy1.name} და {enemy2.name}!\n")

while enemy1.is_alive() and enemy2.is_alive():
    enemy1.attack(enemy2)
    enemy2.attack(enemy1)
    print(" ")
    time.sleep(0.75)

if enemy1.is_alive():
    winner = enemy1
else:
    winner = enemy2

print(f"🎉 გამარჯვებულია {winner.name}!")