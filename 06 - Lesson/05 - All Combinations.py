#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   დაბეჭდეთ 1, 2, 3, 4, 5 ყველა შესაძლო კომბინაცია

from itertools import combinations

num_list = [1, 2, 3, 4, 5]
comb_list = list(combinations(num_list, 3))

print(f"სულ {num_list} სიის გამოყენებით შესაძლოა {len(comb_list)} სამწევრიანი კომბინაციის დაგენერირება")
print(comb_list)
