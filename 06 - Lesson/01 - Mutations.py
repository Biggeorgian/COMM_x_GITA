#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   დაბეჭდეთ ABCD ყველა შესაძლო ვარიანტი

from itertools import permutations

word = "ABCD"
###################### მოკლე და კონკრეტული ვერსია
print("1 ვერსია:")
print(f"შესაძლოა {len(list(permutations(word)))} მუტაცია\n")

####################### ვრცელი ვერსია
print("2 ვერსია:")
word_len = len(word)
case_sensitive_mutations = len(list(permutations(word)))
total_permutations = case_sensitive_mutations * (word_len**2)

print(f"მხოლოდ ზედა რეგისტრის შემთხვევაში შესაძლოა {case_sensitive_mutations} მუტაცია")
print(f"მხოლოდ ქვედა რეგისტრის შემთხვევაში შესაძლოა {case_sensitive_mutations} მუტაცია")
print(f"რეგისტრების შერევის შემთხვევაში შესაძლოა {total_permutations} მუტაცია")
