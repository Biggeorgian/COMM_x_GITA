#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   პაროლის გენერატორი

import random
import string

def password_generator(password_length, numbers_count, symbols_count):
    letters_count = password_length - numbers_count - symbols_count
    # პუნქტუაციის ნიშნების გამოყენების თავიდან ასარიდებლად ვიყენებ სიმბოლოების უსაფრთხო სიას
    symbols = "!@#$%^&*()?_-+="

    random_letters = "".join(random.choice(string.ascii_letters) for _ in range(letters_count))
    random_numbers = "".join(random.choice(string.digits) for _ in range(numbers_count))
    random_symbols = "".join(random.choice(symbols) for _ in range(symbols_count))

    combined_string = random_letters + random_numbers + random_symbols
    shuffle = random.sample(combined_string, len(combined_string))
    password = "".join(shuffle)
    return password


def print_password():
    generated_password = password_generator(password_length, numbers_count, symbols_count)
    message = str(f"\nთქვენი მოთხოვნით დაგენერირებული პაროლია: {generated_password}")
    return message


print(
    "მოგესალმებით პაროლის გენერატორში!\nმიუთითეთ პაროლის სასურველი სიგრძე და რამდენი რიცხვისა და სპეციალური სიმბოლოს გამოყენება გსურთ.\nთუ მიუთითებთ 0-ს, რიცხვების ან/და სპეციალური სიმბოლოების გამოყენება არ მოხდება.")
while True:
    while True:
        user_input = input("\nრამდენი სიმბოლო იყოს პაროლში? (გთხოვთ მიუთითოთ არანაკლებ 8): ")
        if user_input.isnumeric():
            x = int(user_input)
            if x >= 8:
                password_length = x
                break
            else:
                print("8 სიმბოლოზე მცირე პაროლის გამოყენება არ არის უსაფრთხო")
        else:
            print("გთხოვთ შეიყვანოთ რიცხვითი მნიშვნელობა: ")

    while True:
        user_input = input("რამდენი რიცხვითი სიმბოლო იყოს პაროლში?: ")
        if user_input.isnumeric():
            x = int(user_input)
            if x >= password_length:
                print("ყურადღება! მოთხოვნილია პაროლში არსებულ თავისუფალ სიმბოლოზე მეტი ან ტოლი მნიშვნელობა")
                print(f"რეკომენდებულია მიუთითოთ {password_length // 2} სიმბოლოზე ნაკლები")
            elif x < 0:
                print("ყურადღება! მითითებულია უარყოფითი რიცხვი")
                print(f"გთხოვთ მიუთითოთ 0-დან {password_length // 2} სიმბოლომდე")
            else:
                numbers_count = x
                break
        else:
            print("გთხოვთ შეიყვანოთ რიცხვითი მნიშვნელობა: ")

    while True:
        user_input = input("რამდენი სპეციალური სიმბოლო იყოს პაროლში?: ")
        remaining_space = password_length - numbers_count
        if user_input.isnumeric():
            x = int(user_input)
            if x > remaining_space:
                print("ყურადღება! მოთხოვნილია პაროლში არსებულ თავისუფალ სიმბოლოზე მეტი ან ტოლი მნიშვნელობა")
                print(f"გთხოვთ მიუთითოთ {remaining_space} სიმბოლოზე ნაკლები: ")
            elif x < 0:
                print("ყურადღება! მითითებულია უარყოფითი რიცხვი")
                print(f"გთხოვთ მიუთითოთ 0-დან {remaining_space} სიმბოლომდე: ")
            else:
                symbols_count = x
                break
        else:
            print("გთხოვთ შეიყვანოთ რიცხვითი მნიშვნელობა: ")

    print(print_password())
    decision = input("\nგსურთ პაროლის ხელახლა დაგენერირება იგივე პარამეტრებით? yes / no: ").lower()

    while True:
        if decision.isalpha() and decision == "no":
            break
        elif decision.isalpha() and decision != "yes":
            decision = input("\nდასაშვებია მხოლოდ yes ან no პასუხები: ").lower()
        else:
            print(print_password())
            decision = input("\nგსურთ პაროლის ხელახლა დაგენერირება იგივე პარამეტრებით? yes / no: ").lower()

    final_decision = input("გსურთ პაროლის დაგენერირება ახალი პარამეტრებით? yes / no: ").lower()
    if final_decision.isalpha() and final_decision == "no":
        print(
            "\nმადლობა, რომ სარგებლობთ უსაფრთხო პაროლების გენერატორით\nთქვენივე უსაფრთხოებისთვის, ყოველთვის გამოიყენეთ გრძელი და კომპლექსური პაროლები")
        break
    elif final_decision.isalpha() and final_decision != "yes":
        final_decision = input("\nდასაშვებია მხოლოდ yes ან no პასუხები: ").lower()
