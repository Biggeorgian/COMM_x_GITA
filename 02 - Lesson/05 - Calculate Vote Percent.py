#   Tbilisi Comm School x GITA: Python
#   Lesson 2
#   Giorgi Goderdzishvili
#
# ამოცანა №5: გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე(შეეცადეთ დაამრგვალოთ პროცენტები მეასედებამდე)

yes = int(input("მიუთითეთ მომხრეთა რაოდენობა: "))
no = int(input("მიუთითეთ მოწინააღმდეგეთა რაოდენობა: "))
one_percent = (yes + no) * 0.01
print(f"Yes = {round(yes / one_percent, 2)}% / No = {round(no / one_percent, 2)}%\n")