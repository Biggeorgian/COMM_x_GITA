def analyze_near_palindrome(char_list: list):
    """
    ასრულებს თქვენს მიერ მოთხოვნილ 4 ეტაპს:
    1. აბრუნებს სიას.
    2. ადარებს სიებს და პოულობს შეუსაბამო ინდექსებს.
    3. ამოწმებს შეუსაბამობების რაოდენობას სიის სიგრძის მიხედვით.
    4. ბეჭდავს "გაფერადებულ" სიას, თუ პირობა სრულდება.
    """
    if not char_list:
        print("სია ცარიელია.")
        return

    # 1. ვქმნით შებრუნებულ სიას
    reversed_list = char_list[::-1]

    # 2. ვპოულობთ ინდექსებს, სადაც ელემენტები არ ემთხვევა
    mismatch_indices = []
    for i in range(len(char_list)):
        if char_list[i] != reversed_list[i]:
            mismatch_indices.append(i)

    # 3. ვამოწმებთ შეუსაბამობების რაოდენობას
    list_len = len(char_list)
    mismatches_count = len(mismatch_indices)

    is_list_even = (list_len % 2 == 0)

    # 3.1 განვსაზღვროთ, დასაშვებია თუ არა ცვლილება
    is_fixable = False
    if is_list_even and mismatches_count <= 2:
        # ლუწი სიგრძის სიაში დასაშვებია 0 ან 2 შეუსაბამობა
        is_fixable = True
    elif not is_list_even and mismatches_count <= 1:
        # კენტი სიგრძის სიაში დასაშვებია 0 ან 1 შეუსაბამობა
        is_fixable = True

    # --- შედეგის გამოტანა ---
    print(f"საწყისი სია: {char_list}")
    print(f"შებრუნებული სია: {reversed_list}")
    print(f"შეუსაბამო ინდექსები: {mismatch_indices} (სულ {mismatches_count} ცალი)")

    if is_fixable:
        # 3.3 ვქმნით "გაფერადებულ" სიას
        highlighted_list = []
        for i, char in enumerate(char_list):
            if i in mismatch_indices:
                # თუ ინდექსი შეუსაბამოა, ვამატებთ "გაფერადებულ" ელემენტს
                highlighted_list.append(f"░{char}░")
            else:
                # თუ არა, ვამატებთ ჩვეულებრივ ელემენტს
                highlighted_list.append(char)
        print("\nშედეგი: პალინდრომი მიიღება. გაფერადებულია შესაცვლელი ელემენტები:")
        print(highlighted_list)
    else:
        # 3.2 თუ პირობა არ სრულდება
        print("\nშედეგი: ერთი ცვლილებით პალინდრომი არ მიიღება.")


# --- მაგალითების ტესტირება ---

# ლუწი სიგრძის სია, 2 შეუსაბამობით (გამოსწორებადი)
print("--- მაგალითი 1 (ლუწი) ---")
analyze_near_palindrome(["ქ", "ა", "რ", "ზ", "ა", "ქ"])

print("\n" + "=" * 30 + "\n")

# კენტი სიგრძის სია, 1 შეუსაბამობით (გამოსწორებადი)
print("--- მაგალითი 2 (კენტი) ---")
analyze_near_palindrome(["r", "a", "d", "a", "r"])  # შეცდომა 'd'-ში

print("\n" + "=" * 30 + "\n")

# ლუწი სიგრძის სია, 4 შეუსაბამობით (გამოუსწორებელი)
print("--- მაგალითი 3 (გამოუსწორებელი) ---")
analyze_near_palindrome(["h", "e", "l", "l", "o", "w"])