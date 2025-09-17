#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   ბიბლიოღეკა

import logging
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

books = [
    ["დიუნი", "ფრენკ ჰერბერტი", "1965", "ხელმისაწვდომია"],
    ["დიუნის მესია", "ფრენკ ჰერბერტი", "1969", "ხელმისაწვდომია"],
    ["დიუნის შვილები", "ფრენკ ჰერბერტი", "1976", "ხელმისაწვდომია"],
    ["დიუნის ღმერთი-იმპერატორი", "ფრენკ ჰერბერტი", "1981", "ხელმისაწვდომია"],
    ["დიუნის ერეტიკოსები", "ფრენკ ჰერბერტი", "1984", "ხელმისაწვდომია"],
    ["დიუნის კაპიტული", "ფრენკ ჰერბერტი", "1985", "ხელმისაწვდომია"],
    ["ჰიპერიონი", "დენ სიმონსი", "1989", "ხელმისაწვდომია"],
    ["ჰიპერიონის დაცემა", "დენ სიმონსი", "1990", "ხელმისაწვდომია"],
    ["ენდიმიონი", "დენ სიმონსი", "1996", "ხელმისაწვდომია"],
    ["ენდიმიონის აღზევება", "დენ სიმონსი", "1997", "ხელმისაწვდომია"]
]

print("მოგესალმებით ბიბლიოთეკის მართვის სისტემაში")

while True:
    user_input = input("აირჩიეთ ოპერაცია: "
                       "L (სია), "
                       "S (ძებნა), "
                       "G (გატანა), "
                       "A (დამატება), "
                       "Exit (გასვლა): ")
    choice = user_input.lower()

    if choice == "l":
        # დავბეჭდოთ ბიბილიოთეკის წიგნების დანომრილი სია
        print("\nბიბლიოთეკის აქტივშია წიგნები:")
        for index, book in enumerate(books):
            title, author, year, status = book
            print(f"{index + 1}: {title}. ავტორი: {author}.")
        print(" ")

    elif choice == "s":
        search = input("ჩაწერეთ მოსაძებნი წიგნის სათაური: ").lower()
        found = 0
        for i in range(len(books)):
            if search in books[i][0]:
                print(f"{i}: {books[i][0]}. {books[i][1]}")
                found += 1
        if found == 0:
                print("სამწუხაროდ ასეთი წიგნი არ მოიძებნა\n")
        print(" ")

    elif choice == "g":
        wish = input("წიგნის გასატანად ჩაწერეთ მისი სათაური: ")
        # შევამოწმოთ გვაქვს თუ არა წიგნი
        # თუ გვაქვს, გავცეთ და შევუცვალოთ სტატუსი
        for i in range(len(books)):
            if books[i][0] == wish:
                if books[i][3] == "ხელმისაწვდომია":
                    books[i][3] = "გატანილია"
                    title = books[i][0]
                    print(f"✓ თქვენ გაიტანეთ წიგნი: \"{title}\".")
                    logging.info(f"მომხმარებელმა გაიტანა \"{title}\"")
                    break
                elif books[i][0] == wish and books[i][3] == "გატანილია":
                    print("სამწუხაროდ, ეს წიგნი უკვე გატანილია.")
                    break
        else:
            print(f"\n✗ შეცდომა: წიგნი სათაურით \"{wish}\" არ მოიძებნა.")
            logging.info(f"მომხმარებელი ეძებდა წიგნს \"{wish}\"")
        print(" ")

    elif choice == "a":
        book_title = input("შეიყვანეთ წიგნის სათაური: ")
        book_author = input("შეიყვანეთ ავტორი: ")
        book_year = input("შეიყვანეთ წელი: ")
        # ვაერთიანებთ ახალი წიგნის ინფოს და ვამატებთ სიაში
        new_book = [book_title, book_author, book_year, "ხელმისაწვდომია"]
        books.append(new_book)
        print("წიგნი წარმატებით დაემატა\n")
        logging.info(
            f"მომხმარებელმა დაამატა წიგნი "
            f"{book_title}, {book_author}, {book_year}"
        )

    elif choice == "exit":
        print(" ." * 20)
        print("მადლობა ბიბლიოთეკით სარგებლობისთვის.")
        break

    else:
        print("ასეთი ოპერაცია არ არსებობს.")