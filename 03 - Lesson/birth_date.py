#   Tbilisi Comm School x GITA: Python
#   Lesson 3
#   Giorgi Goderdzishvili
#
#   დაწერეთ ციკლი, რომელიც მოითხოვს მომხმარებლისგან ასაკის შეყვანას,
#   თუ შეყვანილი მონაცემი არ იქნება რიცხვური ტიპის, მაშინ ციკლი დატრიალდეს და თავიდან კითხოს,
#   სხვაგვარად დაუანგარიშოს დაბადების თარიღი.

from datetime import datetime

print("🧙‍♂️ ახლა მე ვეცდები თქვენი დაბადების თარიღის გამოცნობას")
print("თუ თამაშის შეწყვეტა მოგინდებათ, აკრიფეთ სიტყვა \"exit\"\n")

while True:
    user_input = input("გთხოვთ, მიუთითოთ რამდენი წლის ბრძანდებით: ")
    if user_input.isdigit():
        age = int(user_input)
        if age > 0 and age < 120:
            current_year = datetime.now().year
            birth_year = str(current_year - age)
            print("\nთქვენ დაიბადეთ " + birth_year + " წელს")
            break

        else:
            print("\nრა თქმა უნდა დიდხანს სიცოცხლეს გისურვებთ,")
            print("მაგრამ ნაკლებად სავარაუდოა, რომ თქვენი ასაკი იყოს " + str(user_input))

    elif user_input == "exit" or user_input == "EXIT":
        print("\nამჯერად გემშვიდობებით, მაგრამ თუ დაბადების წლის გამოთვლა დაგჭირდებათ, იცოდეთ რომ აქ ვართ ❤️")
        break

    else:
        print("\nგთხოვთ მიუთითოთ რიცხვითი მნიშვნელობა,")
        print("ან, თუ თამაში მოგბეზრდათ, აკრიფოთ სიტყვა \"exit\"")
