#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   ვითვლით სიტყვების სიტატისტიკას

word_stats = {}

print("მოდით დავთვალოთ გამოყენებული სიტყვების სტატისტიკა!")
user_input = input("გთხოვთ შეიყვანოთ გასაანალიზებელი ტექსტი: ")
normalized_list = sorted(list(user_input.lower().split()))

for word in normalized_list:
    word_stats[word] = word_stats.get(word, 0) + 1

for word, count in word_stats.items():
    if count > 1:
        print(f"სიტყვა \"{word}\" გვხვდება {count}-ჯერ")