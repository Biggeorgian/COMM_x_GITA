#   Tbilisi Comm School x GITA: Python
#   Lesson 4
#   Giorgi Goderdzishvili
#
#   შექმენი ფსევდო Hungman თამაში

# სიიდან სიტყვის შემთხვევითი პრინციპით ასარჩევად, შემოვიტანოთ შემტხვევითი რიცხვის გენერატორი
import random

# გავაკეთოთ სიტყვების სია
words = ["Mta", "Tbilisi", "Georgia", "Piano", "Auto", "Plane", "Europe", "Sea", "Khinkali", "Nabadi", "Ludi", "Metro",
         "Taxi", "Magazia"]
# ვაგენერირებთ შემთხვევით რიცხვს და სიიდან ვიღბთ შესაბამისი ინდექსის სიტყვას
rand = random.randint(0, len(words) - 1)
word_to_guess = words[rand]
# ეს ტრანსფორმაციები მჭირდება რეგისტრზე მგრძნობელობის მოსახსნელად და შედარებებისთვის
word_lower = word_to_guess.lower()
word_length = len(word_to_guess)
# სეტს ვიყენებ იმიტომ, რომ შეიძლება სიტყვაში რამდენიმე ერთნაირი სიმბოლო იყოს და ხელახლს რომ არ მოუწიოს გამოცნობა
# თან სეტის დაცლას გამოვიყენებ სიტყვის გამოცნობის ინდიკატორად
char_set = set(word_to_guess.lower())
# ეს კიდევ ჩაფიქრებული სიტყვის დასამასკად მჭირდება
masked_word = ["░"] * word_length
tries = 0


# პროგრესის მაჩვენებელი გავიტანე ფუნქციაში, რომ დავინახო რა სიტყვას ვიცნობ
def display_progress(word_lower, user_input, masked_word, word_to_guess):
    for index, char in enumerate(word_lower):
        if char == user_input:
            masked_word[index] = word_to_guess[index]
    current_progress = "".join(masked_word)
    print(f"\nმიმდინარე მდგომარეობა: {current_progress}")


print(
    "მოდით ვითამაშოთ გამოცნობანა! ჩაფიქრებული სიტყვის გამოსაცნობად გაქვთ 10 მცდელობა.\nშეგიძლიათ როგორც ცალ-ცალკე ასოების ჩაწერა, ასევე მთლიანი სიტყვის მითითებაც.\n")
# print(words)
print(f"ჩაფიქრებული სიტყვა {''.join(masked_word)} შედგება {word_length} ასოსგან. გისურვებთ წარმატებას!")

while tries <= 9:
    tries += 1
    user_input = input("გთხოვთ, მიუთითოთ ასო ან მთლიანი სიტყვა: ").lower()

    if word_lower == user_input:
        print(f"\nგილოცავთ! თქვენ გამოიცანით ჩაფიქრებული სიტყვა {tries} მცდელობით 🎉")
        break

    elif user_input.isdigit() or len(user_input) > 1 or user_input == "":
        display_progress(word_lower, user_input, masked_word, word_to_guess)
        print(f"თქვენ შეიყვანეთ არასწორი სიტყვა, სიმბოლო ან მნიშვნელობა. დარჩენილია {10 - tries} მცდელობა!")

    elif user_input.isalpha() and len(user_input) == 1:
        if user_input in char_set:
            char_set.remove(user_input)
            display_progress(word_lower, user_input, masked_word, word_to_guess)
            print(f"ყოჩაღ, არის ასეთი ასო! თქვენ დაგრჩათ {10 - tries} მცდელობა")
            if not char_set:
                print(f"გილოცავთ! თქვენ გამოიცანით ჩაფიქრებული სიტყვა {tries} მცდელობით 🎉")
                break
        elif user_input not in char_set:
            display_progress(word_lower, word_to_guess, user_input, masked_word)
            print(f"სამწუხაროდ ჩაფიქრებულ სიტყვაში ასეთი ასო არ არის. დარჩენილია {10 - tries} მცდელობა...")
    elif tries <= 9:
        print(
            f"\nსამწუხაროდ თქვენ ვერ შეძელით სიტყვის 10 ცდაში გამოცნობა. \nმაგრამ არ დანებდეთ, გთხოვთ სცადოთ კიდევ ერთხელ!")

if tries == 10 and char_set:
    print(f"\nსამწუხაროდ თქვენ ვერ შეძელით სიტყვის 10 ცდაში გამოცნობა. 😔")
    print(f"ჩაფიქრებული სიტყვა იყო: {word_to_guess}")
