#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   დავბეჭდოთ რიცხვების პირამიდა

def pyramide(numbers_list):
    pyramide_data = {}
    step = 1
    active_row = numbers_list

    while len(active_row) > 0:
        pyramide_data[str(step)] = active_row
        if len(active_row) == 1:
            break

        next_row = [active_row[i] + active_row[i + 1] for i in range(len(active_row) - 1)]
        active_row = next_row
        step += 1

    return pyramide_data

print("მოდით დავბეჭდოთ რიცხვების პირამიდა!")
user_input = input("გთხოვთ ულიმიტოდ, სიმბოლოს გამოტოვებით, შეიყვანოთ სასურველი რიცხვები: ")
pyramide = pyramide(numbers_list = [int(num) for num in user_input.split()])

for i in range(len(pyramide), 0, -1):
    row = pyramide[str(i)]
    print(" " * i, " ".join(map(str, row)))