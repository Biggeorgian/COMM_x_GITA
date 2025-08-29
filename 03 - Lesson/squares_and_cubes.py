#   Tbilisi Comm School x GITA: Python
#   Lesson 3
#   Giorgi Goderdzishvili
#
#   ციკლის მეშვეობით დაითვალეთ მოცემული მასივის: mylist = range(100)
#   კუბური და კვადრატული ხარისხები

my_list = range(100)  # შევქმნათ სია
squares = []  # შევქმნათ კუბური ხარისხის შესანახი სია
cubes = []  # შევქმნათ კვადრატული ხარისხის შესანახი სია

i = 0
while i < len(my_list):  # ვატრიალებთ ციკლს, სანამ i არის სიის სიგრძეზე ნაკლები
    number = my_list[i]  # ვიღებთ რიცხვს
    square = number ** 2  # ვითვლით კვადრატს
    squares.append(square)  # ვინახავთ კვადრატის ხარისხის სიაში
    cube = number ** 3  # ვითვლით კუბს
    cubes.append(cube)  # ვინახავთ კუბის ხარისხის სიაში
    i += 1  # ვზრდით ინდექსს

i = 0
while i < 100:
    number = my_list[i]
    print(str(number) + "² = " + str(squares[i]) + ", " + str(number) + "³ = " + str(cubes[i]))
    i += 1
