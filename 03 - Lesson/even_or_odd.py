#   Tbilisi Comm School x GITA: Python
#   Lesson 3
#   Giorgi Goderdzishvili
#
#   While loop და FOR LOOP-ის გამოყენებით დაწერეთ ციკლი,
#   რომელიც დაბეჭდავს რიცხვებს 1-დან 20-ის ჩათვლით
#   და რიცხვის გასწვრივ დაწერს ლუწია თუ კენტი.

print("მიუთითე, რომელი ციკლის გამოყენებით გსურს 1-დან 20-ის დიაპაზონში რიცხვების შემოწმება")

while True:
    user_input = input("აირჩიე \"while\" ან \"for\": ")
    if user_input == "while" or user_input == "WHILE":
        i = 1
        while i <= 20:
            if i == 0:
                print(i)
            elif i % 2 == 0:
                print(f"{i} - ლუწია")
            else:
                print(f"{i} - კენტია")
            i += 1
        print("მოცემული შემოწმება შესრულდა while ციკლის გამოყენებით.")
        print("პროგრამის დასასრულებლად ჩაწერე \"exit\"\n")

    elif user_input == "for" or user_input == "FOR":
        for i in range(1, 21):
            if i % 2 == 0:
                print(f"{i} - ლუწია")
            else:
                print(f"{i} - კენტია")
        print("მოცემული შემოწმება შესრულდა for ციკლის გამოყენებით.")
        print("პროგრამის დასასრულებლად ჩაწერე \"exit\"\n")

    elif user_input == "exit" or user_input == "EXIT":
        print("თუ არ გაინტერესებს, არც დაგაძალებ. ნახვამდის")
        break

    else:
        print("გთხოვთ მიუთითოთ მხოლოდ \"while\" ან \"for\", წინააღმდეგ შემთხვევაში სკრიპტი არ იმუშავებს")
