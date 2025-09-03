#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   დაბეჭდეთ 1, 2, 3, 4, 5 ყველა შესაძლო კომბინაცია

from itertools import combinations

string_to_analyze = "XYZ"
comb_list = []
i = 1

while i < 4:
    comb_list.extend(list(combinations(string_to_analyze, i)))
    i += 1

print(f"სულ {string_to_analyze} სტრიქონით შესაძლოა {len(comb_list)} კომბინაციის დაგენერირება")
print(comb_list)