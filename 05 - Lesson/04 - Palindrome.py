#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   პალინდრომის შემოწმება

def palindrome(user_input):
    inverted_word = user_input[::-1]
    return inverted_word

def suggestion(user_input, inverted_word):
    list1 = list(user_input)
    list2 = list(inverted_word)

    mismatches_list = []
    mismatch_count = 0
    word_length = len(list1)

    for i in range(word_length):
        if list1[i] != list2[i]:
            mismatches_list.append(i)
            mismatch_count += 1

    fixable = False
    is_even = (word_length % 2 == 0)

    if is_even and mismatch_count <= 3:
        fixable = True
    elif not is_even and mismatch_count <= 2:
        fixable = True

    if fixable:
        display = []
        for i, char in enumerate(user_input):
            if i in mismatches_list:
                display.append(f"░")
            else:
                display.append(char)
        print("\nპალინდრომი მიიღება გაფერადებული უჯრების ცვლილებით:")
        print(display)
    else:
        print("\nშედეგი: ერთი ცვლილებით პალინდრომი არ მიიღება.")
    # print(f"fixable = {fixable}")
    # print(f"is even = {is_even}")
    # print(f"mismatches_list = {mismatches_list}")
    # print(f"mismatch_count  = {mismatch_count}")
    return

print("ამ პროგრამაში ვეცდებით შევამოწმოთ, შეყვანილი სიტყვა პალინდრომია თუ არა")

while True:
    user_input = input("შეიყვანეთ შესამოწმებელი სიტყვა: ")
    word_count = len(user_input.split())
    if user_input.isalpha() and word_count == 1:
        if user_input == palindrome(user_input):
            print("ეს სიტყვა პალინდრომია")
            break
        else:
            print("ეს სიტყვა პალინდრომი არ არის")
            suggestion(user_input, palindrome(user_input))
            break
    else:
        print("გთხოვთ შეიყვანოთ მხოლოდ ერთი სიტყვა.\n")

