#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   დაადგინეთ შეყვანილი წელიწადი ნაკიანია თუ არა

import calendar

print("მოდით დავადგინოთ წელი ნაკიანია თუ არა")
user_input = int(input("შეიყვანეთ წელიწადი: "))

if calendar.isleap(user_input):
    print(f"{user_input} წელი ნაკიანია.")
else:
    print(f"{user_input} წელი არ არის ნაკიანი.")