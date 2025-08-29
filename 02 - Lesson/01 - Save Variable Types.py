#   Tbilisi Comm School x GITA: Python
#   Lesson 2
#   Giorgi Goderdzishvili
#
#   ამოცანა 1: შეინახეთ ცვლადებში მათი ტიპები მათ მნიშვნელობის ნაცვლად

var1 = 1
var2 = -1
var3 = True

#  ამოხსნა:
#  1. ვადგენთ ცვლადის ტიპს,
#  2. გადავკასტავთ სტრიქონის ტიპად
#  3. ვაჭრით ზედმეტ სიმბოლოებს

var1 = str(type(var1))[8:11]
var2 = str(type(var2))[8:11]
var3 = str(type(var3))[8:12]
print(f"{var1}, {var2}, {var3}")