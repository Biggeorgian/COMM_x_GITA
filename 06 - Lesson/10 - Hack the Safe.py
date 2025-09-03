#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   გავტეხოთ სეიფის 4 ციფრიანი კომბინაცია

import random
the_code = "".join([str(random.randint(1, 6)) for _ in range(4)])
tries = []

print("თქვენს წინაშეა სეიფი, რომელსაც აქვს ოთხ ციფრიანი კოდი, თითოეული ციფრის მაქსიმალური მნიშვნელობაა 6")
print("შეგიძლიათ ულიმიტოდ სცადოთ ვარიანტები, სანამ სეიფი არ გაიხსნება")
print(the_code)

while True:
    user_input = input("სცადეთ კომბინაციის გამოცნობა: ")
    if user_input == the_code:
        tries.append(user_input)
        print("\nყოჩაღ! თქვენ გამოიცანით სწორი კომბინაცია 🥳")
        print("სეიფის გასახსნელად თქვენ სცადეთ შემდეგი კომბინაციების გამოყენება:")
        for i in range(len(tries)):
            print(f"{i + 1}: {tries[i]}")
        break
    elif user_input.isdigit():
        tries.append(user_input)
        print("სამწუხაროდ, ვერ გამოიცანით...\n")
    elif user_input.isalnum():
        tries.append(user_input)
        print("კოდი შედგება მხოლოდ რიცხვებისგან!\n")

