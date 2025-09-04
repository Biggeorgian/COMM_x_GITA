#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   რამდენი დღე დარჩა შემდეგ დაბადების დღემდე

from datetime import datetime, date

now = date.today()
print(now)

print("მოდით გავიგოთ, რამდენი დღ დარჩე თქვენ დაბადების დღემდე.")
print("სწორი გამოთვლისთვის გთხოვ მიუთითოთ შემდეგი ფორმატით: რიცხვი, თვე, წელი.")
user_input = input("\nმიუთითეთ დაბადების თარიღი: ")

user_bday = datetime.strptime(user_input, "%d, %m, %Y").date()
current_bday = date(now.year, user_bday.month, user_bday.day)

if current_bday < now:
    next_bday = date(now.year + 1, user_bday.month, user_bday.day)
else:
    next_bday = current_bday

days_left = (next_bday - now).days

if days_left == 0:
    print("\n🎉 გილოცავთ! დღეს თქვენი დაბადების დღეა!")
else:
    print(f"\nთქვენს შემდეგ დაბადების დღემდე დარჩა {days_left} დღე.")