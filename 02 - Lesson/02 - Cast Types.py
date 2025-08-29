#   Tbilisi Comm School x GITA: Python
#   Lesson 2
#   Giorgi Goderdzishvili
#
#   ამოცანა 2: შეცვალეთ ცვლადების ტიპები (type casting-ის მეშვეობით)

# გადაიყვანეთ Float -ში
var4 = False
# გადაიყვანეთ Float -ში
var5 = 3
# გადაიყვანეთ list -ში
var6 = {"key": "value", "key1": "value", "key3": "value"}

var4 = float(var4)
var5 = float(var5)
var6 = list(var6.items())
print(f"{var4}, {var5}, {var6}")