#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   პაროლის საიმედოობის შემოწმება

import string

def check(password):
    length = len(password)
    reccomendations = []
    letters = "".join([char for char in password if char in string.ascii_letters])

    has_lower = any(char in string.ascii_lowercase for char in letters)
    has_upper = any(char in string.ascii_uppercase for char in letters)
    has_digit = any(char in string.digits for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    score = has_lower + has_upper + has_digit + has_symbol

    lowercase = sum(1 for char in letters if char in string.ascii_lowercase)
    uppercase = sum(1 for char in letters if char in string.ascii_uppercase)
    numbers = sum(1 for char in password if char in string.digits)
    symbols = sum(1 for char in password if char in string.punctuation)



    if all(char in string.ascii_letters for char in letters):
        if length >= 12:
            if score <= 2:
                reccomendations.append("ერთად გამოიყენე დიდი და პატარა ასოები, რიცხვები და სპეციალური სიმბოლოები")
                message = "სუსტი"
            elif score <= 3 and lowercase == 0 or uppercase == 0 or numbers == 0 or symbols == 0:
                message = "საშუალო."
                reccomendations.append("პაროლში უნდა იყოს დიდი და პატარა ასოები, რიცხვები და სპეციალური სიმბოლოები")
            elif score == 4 > 0 and numbers > 2 and symbols > 2:
                message = "ძალიან ძლიერი."
            else:
                message = "ძლიერი."
        elif length >= 8:
            reccomendations.append("უმჯობესია, პაროლი გაზარდო 12+ სიმბოლომდე")
            if score <= 2:
                reccomendations.append("ერთად გამოიყენე დიდი და პატარა ასოები, რიცხვები და სპეციალური სიმბოლოები")
                message = "სუსტი"
            elif score <= 3 and lowercase == 0 or uppercase == 0 or numbers == 0 or symbols == 0:
                message = "საშუალო."
                reccomendations.append("პაროლში უნდა იყოს დიდი და პატარა ასოები, რიცხვები და სპეციალური სიმბოლოები")
            elif score == 4 > 0 and numbers > 1 and symbols > 1:
                message = "ძალიან ძლიერი."
            else:
                message = "ძლიერი."
        else:
            reccomendations.append("უმჯობესია, პაროლი გაზარდო 12+ სიმბოლომდე")
            reccomendations.append("ერთად გამოიყენე დიდი და პატარა ასოები, რიცხვები და სპეციალური სიმბოლოები")
            message = "სუსტი"
    else:
        message = "დაუშვებელი!"
        reccomendations.append("პაროლში ყოველთვის გამოიყენე მხოლოდ დიდი და პატარა რეგისტრის ლათინური ასოები")
        reccomendations.append("ამჟამად უსაფრთხო პაროლის სიგრძე არ უნდა იყოს 12 სიმბოლოზე ნაკლები")
        reccomendations.append("ლათინურ ამბანთან ერთად, აუცილებლად გამოიყენე რიცხვები და სპეციალური სიმბოლოები")

    print(score)
    return message, reccomendations

print("მოგესალმებით პაროლის საიმედოობის შემოწმების ინსტრუმენტში.")
password = input("გთხოვთ, შეიყვანოთ შესამოწმებელი პაროლი: ")
message, reccomendations = check(password)

print(f"\nშენი შეყვანილი პაროლი \"{password}\" არის {message}")
if reccomendations:
    print("რეკომენდაციები პაროლის გასაუმჯობესებლად:")
    for text in reccomendations:
        print(f" • {text}")

