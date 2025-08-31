#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   სორტირება
import random

print("მოგესალმებით რიცხვების დახარისხების პროგრამაში.")
user_input = input("გთხოვთ ულიმიტოდ, სიმბოლოს გამოტოვებით, შეიყვანოთ სასურველი რიცხვები: ")
numbers_list = [int(num) for num in user_input.split()]

while True:
    user_answer = input("აირჩიეთ როგორ დავახარისხოთ სია: აღმავალი = A, დაღმავალი = D, შემთხვევით = R: ")
    if user_answer.isalpha():
        if user_answer.lower() == "a":
            print(f"\nაღმავალი დახარისხება: {sorted(numbers_list, reverse=False)}")
            break
        elif user_answer.lower() == "d":
            print(f"\nდაღმავალი დახარისხება: {sorted(numbers_list, reverse=True)[0:-1]}")
            break
        elif user_answer.lower() == "r":
            random.shuffle(numbers_list)
            print(f"არეული სია: {numbers_list}")
            break
        else:
            print("დახარისხების ეს მეთოდი ჩემთვის უცნობია.")
    else:
        print("გთხოვთ შეიყვანოთ დახარისხების შესაძლო ვარიანტებიდან ერთ-ერთი.")