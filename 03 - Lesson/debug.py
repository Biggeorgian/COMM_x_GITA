#   Tbilisi Comm School x GITA: Python
#   Lesson 3
#   Giorgi Goderdzishvili
#
#   გააანალიზე კოდის ფრაგმენტი და შემდეგ გაასწორე შეცდომები, ასევე დაწერე ახსნა:

#   numbers = ["1", "2", "3", "4"]
#   total = 0
#   for n in numbers:
#       total += n
#   print("Total:", total)

numbers = ["1", "2", "3", "4"]
total = 0
for n in numbers:
    total += int(n)
print(total)

# ამოხსნა:
# numbers არის სტრიქონების სია, რის გამოც ვერ ხერხდებოდა რიცხვების შეკრება
# int(n) სტრიქონს გადაკასტავს ინტეჯერად, რის შემდეგაც შესაძლებელი ხდება სიის ელემენტების შეკრება
