#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   წავშალოთ ციფრები და სიმბოლოები

import string
dirt = string.digits + string.punctuation

print("მოვაცილოთ ტექსტს რიცხვები და სიმბოლოები!")
message = input("შეიყვანეთ გასაწმენდი ტექსტი: ")
print(". " * 20)

cleaned_message = "".join(char for char in message if char not in dirt)
print(f"გაწმენდილი ტექსტი: {cleaned_message}")