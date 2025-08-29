#   Tbilisi Comm School x GITA: Python
#   Lesson 4
#   Giorgi Goderdzishvili
#
#   დაწერეთ ციკლი რომელიც დაბეჭდავს ლისტში მყოფ უდიდეს 3 რიცხვს და მათ ინდექსებს

# შემოვიტანოთ random და დავაგენერიროთ შემთხვევითი სია
import random

my_list = [random.randint(1, 20) for _ in range(10)]

# შევქმნათ ახალი სია, რომელშიც შევინახავთ რიცხვებისა და თავისი ინდექსების წყვილს
indexed_list = list(enumerate(my_list))

# ახალ სიაში დავალაგოთ ეს წყვილები მეორე ელემენტის კლებადობის მიხედვით.
# დახარისხების წესისთვის გამოვიყენოთ ანონიმური ფუნქცია lambda
sorted_list = sorted(indexed_list, key=lambda x: x[1], reverse=True)

print(f"დაგენერირდა სია: {str(my_list)[1:-1]}. რომლის სამი უდიდესი რიცხვია:")
for index, number in sorted_list[:3]:
    print(f"→  რიცხვი {number}, ინდექსით {index}")
