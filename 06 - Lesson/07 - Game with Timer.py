#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   რიცხვის გამოცნობა ტაიმერით

import random
from datetime import datetime, timedelta

random_number = random.randint(0, 20)
start_time = datetime.now()
end_time = start_time + timedelta(seconds=5)

# print(random_number)

print(f"მე ჩავიფიქრე რიცხვი 0-დან 20-ის დიაპაზონში, გამოსაცნობად გაქვს 5 წამი.")
while (datetime.now() < end_time):
    user_input = int(input("მიუთითეთ თქვენი ვარაუდი: "))
    timer = (datetime.now() - start_time).total_seconds()

    if not (0 <= user_input <= 20):
        user_input = int(input("გთხოვთ მიუთითოთ რიცხვი 0-დან 20-ის ჩათვლით: "))

    elif random_number == user_input and timer < 5:
            print(f"ყოჩაღ, შენ მოახერხე ჩაფიქრებული რიცხვის {timer:.2f} წამში გამოცნობა")
            break

    elif random_number != user_input:
        print("სამწუხაროდ, ვერ გამოიცანით.")
        user_input = int(input("სცადეთ კიდევ ერთხელ: "))
else:
    print("სამწუხაროდ, გამოსაცნობად გამოყოფილი დრო ამოიწურა...")
    print(f"ჩაფიქრებული იყო რიცხვი {random_number}")