import gc

class Person:
    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.birth_year = year

    def __del__(self):
        print(f"Person \"{self.name}\" has removed")

human1 = Person("გომეზ", "ადამსი", 1980)
human2 = Person("მორტიშა","ადამსი", 1990 )

del human2

unused = gc.collect()
print(f"ნაგვის მანქანამ გადაყარა {unused} ობიექტი")