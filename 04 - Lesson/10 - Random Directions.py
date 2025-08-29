#   Tbilisi Comm School x GITA: Python
#   Lesson 4
#   Giorgi Goderdzishvili
#
#   შექმენი ფსევდო ჰაიკინგის თამაში 5 საფეხურით

# შემოვიტანოთ random ბიბლიოთეკა და დავაგენერიროთ შემთხვევითი ბილიკი
import random

random_direqctions = [random.choice(["l", "r"]) for _ in range(5)]
# ცვლადები იტერაციისა და ქულებისთვის
user_input = ""
steps = 0
score = 0

print(f"ახლა მოდით ვითამაშოთ. თუ დროზე ადრე მოგბეზრდათ, უბრალოდ აკრიფეთ exit.")
print(f"წარმოიდგინეთ, რომ გზაზე მიდიხართ და უცბად გზაჯვარედინზე აღმოჩნდით.")

while steps < 5:
    steps += 1
    user_input = input("საით გაუხვევთ მარცხნივ: l თუ მარჯვნივ: r ? ")
    if user_input.lower() == "l" or user_input.lower() == "r":
        if user_input == random_direqctions[steps - 1]:
            score += 1
            print("კარგია, კარგია, კარგიააააა...")
            print("\nწინ კიდევ ერთი გზაგასაყარია")
        else:
            print("ფრთხილად, ფეხი არაფერში ჩაადგა...")
            print("\nწინ კიდევ ერთი გზაგასაყარია")
    elif user_input.lower() == "exit":
        print("ამ მოსახვევში გემშვიდობებით 🥺")
        break
    else:
        print("ამ თამაშში დასაშვებია მხოლოდ l ან r შეყვანა.\nთუ თამაში მოგბეზრდათ, უბრალოდ აკრიფეთ exit.")

if score == 5:
    print("\nყოჩაღ! ცხოვრების გზაზე შენ სწორედ იარე 😂🎉")
elif user_input.lower() == "exit":
    print("კარგად...")
else:
    print("\nსამწუხაროდ ცხოვრების ლაბირინთში დაიკარგე 🥺")
    print("მაგრამ, ჯერ კიდევ გაქვს შანსი, სცადო ხელახლა 🗺")
