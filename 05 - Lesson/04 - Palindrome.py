#   Tbilisi Comm School x GITA: Python
#   Lesson 5
#   Giorgi Goderdzishvili
#
#   პალინდრომის შემოწმება

def palindrome(user_input):
    inverted_word = user_input[::-1]
    return inverted_word

def suggestion(user_input):
    list1 = list(user_input)
    word_length = len(list1)
    mismatches_list = []
    mismatch_count = 0

    is_even = (word_length % 2 == 0)

    if is_even:
        user_word_half = word_length // 2
        temp_list = list1[:user_word_half]
        reversed_list = temp_list[::-1]
        list2 = temp_list + reversed_list
    else:
        user_word_half = word_length % 2 + word_length // 2
        temp_list = list1[:user_word_half]
        reversed_list = temp_list[::-1]
        list2 = temp_list[:-1] + reversed_list

    for i in range(word_length):
        if list1[i] != list2[i]:
            mismatches_list.append(i)
            mismatch_count += 1

    if mismatch_count == 1:
        display = []
        for i, char in enumerate(user_input):
            if i in mismatches_list:
                display.append(f"░")
            else:
                display.append(char)

        print("\nპალინდრომი მიიღება გაფერადებული უჯრის ცვლილებით:")
        print(f" Input:  {" ".join(list1)}")
        print(f"Change:  {" ".join(display)}")
        print(f"Result:  {" ".join(list2)}")
    else:
        print("სამწუხაროდ ერთი ცვლილებით პალინდრომი არ მიიღება.")


print("ამ პროგრამაში ვეცდებით შევამოწმოთ, შეყვანილი სიტყვა პალინდრომია თუ არა")
while True:
    user_input = (input("შეიყვანეთ შესამოწმებელი სიტყვა: ").lower())
    word_count = len(user_input.split())
    if user_input.isalpha() and word_count == 1:
        if user_input == palindrome(user_input):
            print("ეს სიტყვა პალინდრომია")
            break
        else:
            print("ეს სიტყვა პალინდრომი არ არის")
            suggestion(user_input)
            break
    else:
        print("გთხოვთ შეიყვანოთ მხოლოდ ერთი სიტყვა.\n")

