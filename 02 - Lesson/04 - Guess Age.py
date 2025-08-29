#   Tbilisi Comm School x GITA: Python
#   Lesson 2
#   Giorgi Goderdzishvili
#
# ამოცანა 4: დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი
#
#    birth_year = 1970 # ჩაწერეთ წელი
#    name = ‘სახელი’ #  ჩაწერეთ სახელი
#    surname = ‘გვარი’ # ჩაწერე გვარი
#    current_year = ‘2025’
#
# უნდა მიიღოთ შემდეგი წინადადება - მე ‘სახელი’ ‘გვარი’ დავიბადე ‘ამ წელს’ შესაბამისად ვარ ‘ამდენი წლის’

birth_year = int(input("მიუთითეთ თქვენი დაბადების წელი: "))
name = input("მიუთითეთ თქვენი სახელი: ")
surname = input("მიუთითეთ თქვენი გვარი: ")
current_year = int(input("მიუთითეთ მიმრინარე წელი: "))
print(f"მე ვარ {name} {surname}. დავიბადე {birth_year} წელს. შესაბამისად, ახლა ვარ {current_year - birth_year} წლის\n")