#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   ვადგენთ სიტყვების სიგრძეს

word_stats = {}

print("მოდით დავთვალოთ გამოყენებული სიტყვების სიგრძე!")
user_input = input("გთხოვთ შეიყვანოთ გასაანალიზებელი ტექსტი: ")
print(" ." * 20)

normalized_list = list(user_input.lower().split())
for word in sorted(normalized_list, key = len, reverse=True):
    word_stats[word] = word_stats.get(word, len(word))

print(" ")
print(f"{word_stats}\n")

for word, length in word_stats.items():
    print(f"სიტყვა \"{word}\" შედგება {length} სიმბოლოსგან")

