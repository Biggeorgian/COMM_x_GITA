#   Tbilisi Comm School x GITA: Python
#   Lesson 4
#   Giorgi Goderdzishvili
#
#   დაწერეთ ფუნქცია რომელიც დაბეჭდავს ოთხუთხედს “#” მოცემული სიმაღლისა და სიგანის მიხედვით

def square(width, height):
    for _ in range(height):
        for _ in range(width):
            print("#", end="")
        print()


print("მოგესალმებით ოთხკუთხედის ხატვის დემონსტრაციაში. იმისთვის რომ პროგრამამ იმუშაოს,")
a = int(input("შეიყვანეთ სიგრძე: "))
b = int(input("შეიყვანეთ სიგანე: "))
print(" ")

square(a, b)
