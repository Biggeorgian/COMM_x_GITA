import random

class Monster:
    def __init__(self, name: str, health: int, strength: int):
        self.name = name
        self.health = health
        self.strength = strength

    def __repr__(self):
        return (f"{self.name}: სიცოცხლე = {self.health}, "
                f"ძალა = {self.strength}")

    @classmethod
    def create_from_level(cls, m_name:str, level):
        name = m_name
        base_health = 20
        base_strength = 5
        health = base_health + int(round(8.9 * (level - 1)))
        strength = base_strength + int(round(3.9 * (level - 1)))
        return cls(name, health, strength)

    # @classmethod
    # def create_monster(cls, m_name:str):
    #     name = m_name
    #     health = random.randint(30, 60)
    #     strength = random.randint(5, 15)
    #     return cls(name, health, strength)

name_list = [
    "ამირანი", "დალი", "ოჩოპინტრე", "დევი", "ფასკუნჯი",
    "ყურშა", "კოპალა", "იახსარი", "არმაზი", "ზადენი", "ალი",
    "ბაყბაყ-დევი", "თეთრი გიორგი", "ბარბალე", "ტყაშმაფა",
    "აინინა", "დანინა", "გაცი", "გაიმი", "გა"
]

monsters_random = {}
unique_names = random.sample(name_list, 10)

# დავალების შესაბამისად, სხვადასხვა დონის მონსტრების შექმნა
monsters_from_level = {}
for i, name in enumerate(unique_names, 1):
    new_monster = Monster.create_from_level(name, i)
    monsters_from_level[f"{i} დონის მონსტრი"] = new_monster

for key, monster in monsters_from_level.items():
    print(f"{key}: {monster}")

# უბრალოდ რენდომ მახასიათებლების მონსტრების შექმნა
# for i, name in enumerate(unique_names, 1):
#     new_monster = Monster.create_monster(name)
#     monsters_random[f"Monster_{i}"] = new_monster
# for key, monster in monsters_random.items():
#     print(f"{key}: {monster}")
# print()