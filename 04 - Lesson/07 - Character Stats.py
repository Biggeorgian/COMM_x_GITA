#   Tbilisi Comm School x GITA: Python
#   Lesson 4
#   Giorgi Goderdzishvili
#
#   დაწერეთ ფუნქია, რომელიც მიიღებს 2 პარამეტრს: სტრიქონს და სიმბოლოს
#   ფუნქციამ უნდა დაითვალოს თუ რამდენჯერ გვხვდება სიმბოლო სტიქონში.

def text_analyzer(text, symbol):
    # გავხადოთ გასაანალიზებელი ტექსტი და სიმბოლო რეგისტრზე დამოუკიდებელი
    lower_text = text.lower()
    lower_symbol = symbol.lower()

    # დავითვალოთ სიმბოლოების რაოდენობა
    stats = lower_text.count(lower_symbol)

    # დავბეჭდოთ მონაცემები
    if stats == 0:
        print(f"თქვენ მიერ მითითებულ ტექსტში \"{symbol}\" სიმბოლო არ აღმოჩნდა.")
    else:
        print(f"თქვენ მიერ მითითებულ ტექსტში \"{symbol}\" სიმბოლო აღმოჩნდა {stats}-ჯერ.")


print("მოგესალმებით ტექსტის ანალიზატორში. იმისთვის, რომ პროგრამამ იმუშაოს,")
text = input("შეიყვანეთ გასაანალიზებელი ტექსტი: ")
symbol = input("მიუთითეთ, რომელი სიმბოლოს სტატისტიკა გაინტერესებთ: ")
print(" ")
text_analyzer(text, symbol)
