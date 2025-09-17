class FunnyCalculator():
    def __init__(self, value=0):
        self.value = value
    def __str__(self):
        return "🤡 I’m the funniest calculator in Python!"
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"
    def __sub__(self, other):
        return "Seriously? Substraction is not an attraction..."
    def __mul__(self, other):
        return "Multiplication is too mainstream..."
    def __truediv__(self, other):
        return "ZeroDivisionError? Nah, let’s just say infinity"

def calculator():
    # მი სკუზი, ვერაფრით მოვახერხე, რომ ერთი ობიექტიდან გამომეტანა ეს ტექსტი
    temp = FunnyCalculator()
    print(temp)
    while True:
        try:
            num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
            expr = input("შეიყვანეთ რომელიმე მოქმედება ( + - / *) : ").strip()
            num2 = int(input("შეიყვანეთ პირველი რიცხვი: "))
            calc1 = FunnyCalculator(num1)
            if expr == "+":
                result = calc1 + num2
                print(f"\n{num1} ➕ {num2} 🟰 🤡 {result}")
            elif expr == "-":
                result = calc1 + num2
                print(f"\n{num1} ➖ {num2} 🟰 🤡 {result}")
            elif expr == "*":
                result = calc1 * num2
                print(f"\n{num1} ✖️ {num2} 🟰 🤡 {result}")
            elif expr == "/":
                result = calc1 / num2
                print(f"\n{num1} ➗ {num2} 🟰 🤡 {result}")
            else:
                print(f"\n🚓 ოპელი! '{expr}' აი მოქმედება არატრადიციულია სმნ!")
            continue_choice = input("გსურთ გაგრძელება? "
                                    "(no/anything else): ").lower()
            if continue_choice == "no":
                print("გმადლობთ სარგებლობისთვის!")
                break
            else:
                print(" ")
        except ValueError:
            print(f"\n🚓 ოპელი! ვერ გევიგე რა შეგყავს\n")
calculator()