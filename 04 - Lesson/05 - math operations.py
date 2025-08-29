#   Tbilisi Comm School x GITA: Python
#   Lesson 4
#   Giorgi Goderdzishvili
#
#   მომხმარებელს შემოყავს ორი რიცხვი x & y შექმენით ფუნქცია,
#   რომელიც მიიღებს ამ ორ პარამეტრს და დაბეჭდავს ყველა არითმეტიკულ ოპერაციას

def math_operations(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if a != 0 and b != 0:
        print(f"{a} / {b} = {round(a / b, 2)}")
        print(f"{a} // {b} = {a // b}")
        print(f"{a} % {b} = {a % b}")
    else:
        print("\nყურადღება! ნულზე გაყოფა არ შეიძლება.")


print("მოგესალმებით მათემატიკური მოქმედებების დემონსტრაციაში. იმისთვის რომ პროგრამამ იმუშაოს,")
int_a = int(input("შეიყვანეთ პირველი რიცხვი: "))
int_b = int(input("შეიყვანეთ მეორე რიცხვი: "))
print(" ")

math_operations(int_a, int_b)
