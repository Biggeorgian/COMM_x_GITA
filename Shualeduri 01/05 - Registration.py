import string
name = ""
nickname = "Aristafan"
email = "somemail@mailservice.com"
password = "D^d?we$dr4K_#z"

while True:
    name = input("შეიყვანეთ თქვენი სახელი (პატარა ლათინური შრიფტით): ")

    if not name:
        print("✗: ეს ველი არ შეიძლება იყოს ცარიელი!")
        continue
    if not name.isascii():
        print("✗: სახელი უნდა შეიცავდეს მხოლოდ ლათინურ ასოებს.")
        continue

    lett = any(char.isalpha() for char in name)
    dig = any(char.isdigit() for char in name)
    spec = any(char in string.punctuation or char.isspace() for char in name)

    # პირობები უკუკავშირისთვის
    if dig and spec:
        print("✗: სახელი არ უნდა შეიცავდეს ციფრებს და სპეციალურ სიმბოლოებს.")
    elif dig and lett:
        print("✗: სახელი არ უნდა შეიცავდეს ციფრებს.")
    elif spec:
        print("✗: სახელი არ უნდა შეიცავდეს სპეციალურ სიმბოლოებს ან ჰარებს.")
    elif lett:
        print("\nრეგისტრაცია დასრულებულია:")
        print(f"სახელი: {name}")
        print(f"მეტსახელი {nickname}")
        print(f"ელფოსტა {email}")
        print(f"პაროლი {password}")
        break
    else:
        print("✗: გთხოვთ, შეიყვანოთ მხოლოდ ლათინური ასოები.")