#   Tbilisi Comm School x GITA: Python
#   Lesson 3
#   Giorgi Goderdzishvili
#
#   FOR ციკლის/ციკლების გამოყენებით შექმენი გამრავლების ტაბულა და ტერმინალში გამოიტანე მსგავსი ფორმატით:

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        if result < 10:  # გავათანაბროთ დაშორებები
            print(result, end="   ")
        else:  # გავათანაბროთ დაშორებები
            print(result, end="  ")
    print()
