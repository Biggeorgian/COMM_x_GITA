arr = [1, 2, 3, 4, 5, 6, 7, 8]

user_input = input("მიუთითეთ სიის რომელი ელემენტის გაგება გსურთ: ")

try:
    val = int(user_input)
    print(f"სიის {val} ელემენტის მნიშვნელობაა {arr[val]}")
except IndexError:
    print(f"შეგეძლოთ მიგეთითებინათ 0-დან {len(arr)}-მდე")
except ValueError:
    print(f"დაშვებულია მხოლოდ რიცხვით მნიშვნელობების შეყვანა")