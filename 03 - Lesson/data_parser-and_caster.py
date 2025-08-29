#   Tbilisi Comm School x GITA: Python
#   Lesson 3
#   Giorgi Goderdzishvili
#
#   დაწერეთ FOR LOOP სადაც მიწვდებით მონაცემებს,
#   თუ მნიშვნელობა არის სტრინგი და შეიცავს მხოლოდ რიცხვს, გამოიყენე კასტინგი და შეინახე,
#   თუ ინთეჯერია შეინახე პირდაპირ,
#   თუ ბულიენია გადააქციე და შეინახე (მხოლოდ True) სხვა ყველა ტიპის მონაცემი გამოტოვე.

transactions = {
    "გიო": "100",
    "ნიკა": 50,
    "აკაკი": "30a",
    "ლევანი": 0,
    "ანა": "70",
    "მარი": True
}

# ვინაიდან აქაც შენახვა წერია და არა და დაჯამება და ამავე დროს
# total წინასწარვე მოცემულია როგორც int, ვამატებ ახალ სიას
item_list = []
total = 0

for name, data in transactions.items():
    if isinstance(data,
                  bool):  # ამას თავში იმიტომ ვამოწმებ, რომ ვერაფრით ვერ მოვახერხე Boolean-ების გამორიცხვა ორჯერ ამატებდა სიაში და ჯამში
        if data is True:
            total += 1  # True-ს წერდა სიაში, ამიტომ თუ ბულის ცვლადი ჭეშმარიტია, პირდაპირ ერთს ვამატებ
            item_list.append(1)
    elif isinstance(data, (int,
                           float)):  # ვამოწმებ, მონაცემი რიცხვია თუ წილადი. კი არ გვაქვს, მაგრამ გავითვალისწინოთ მაინც :)
        if data > 0:  # თუ რიცხვი 0-ზე მეტია ვაჯამებ. დამჭირდა Boolean-ების გამო
            total += data
            item_list.append(data)
    elif isinstance(data, str) and data.isdigit():
        data = int(data)
        total += data
        item_list.append(data)

print("ჯამი: " + str(total))
print("გამოყენებული რიცხვები: " + str(item_list)[1:-1])
