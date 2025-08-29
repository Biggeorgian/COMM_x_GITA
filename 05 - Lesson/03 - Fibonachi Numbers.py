#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   ფიბონაჩის რიცხვი

def fibonacci(fibonacci_length):
    a, b = 0, 1
    fibonacci_list = []

    for _ in range(fibonacci_length):
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

print("მოგესალმებით ფიბონაჩის რიცხვების გენერატორში")
while True:
    user_input = input("გთხოვთ მიუთითოთ, რამდენი რიცხვი უნდა დაგენერირდეს ფობონაჩის მწკრივში: ")
    if user_input.isnumeric():
        x = int(user_input)
        if x >= 1001:
            print("\nნუ მამკლავ ბაბუ, რამე პატარა რიცხვი მიუთითე...")
        else:
            fibonacci_length = x
            break
    else:
        print("\nუარყოფითი რიცხვებისა და სიმბოლოების დამუშავება შეუძლებელია.\nშეიყვანოთ მხოლოდ დადებითი რიცხვითი მნიშვნელობა!")

print(f"\n{fibonacci_length} ელემენტიანი ფიბონაჩის მწკრივია: {fibonacci(fibonacci_length)}")