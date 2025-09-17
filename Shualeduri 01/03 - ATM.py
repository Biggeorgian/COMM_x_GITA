#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   ბანკომატი

import logging
logging.basicConfig(
    filename="atm_machine.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

logging.info(f"ავტორიზაცია სისტემაში")
balance = 2823.26
print(f"მოგესალმებით ბანკომატში\nთქვენ ნალანსზე არის {balance} ₾")

while True:
    choice = input("აირჩიეთ ოპერაცია: "
                   "B (ბალანსის შემოწმება), "
                   "W (თანხის გატანა), "
                   "А (თანხის შეტანა), "
                   "Exit (გასვლა): ").lower()

    # ვამოწმებთ ბალანსს
    if choice == "b":
        print(f"\nთქვენ ბალანზსე არის {balance} ₾")
        logging.info("ბალანსის შემოწმების ოპერაცია")

    # თანხის გატანის ოპერაცია
    elif choice == "w":
        try:
            user_input = input(f"\nმიუთითეთ რამდენი ლარის გატანა გსურთ: ")
            withdraw_money = float(user_input)
            if 0 < withdraw_money <= balance:
                balance = round(balance - withdraw_money, 2)
                print(f"გთხოვთ აიღოთ თანხა.")
                print(f"თქვენს ბალანზსე დარჩა {balance} ₾\n")
                logging.info(f"მომხმარებელმა გაიტანა {withdraw_money}")
            else:
                print(f"ბალანსზე არსებულ თანხაზე მეტის გატანა შეუძლებელია!\n")
                logging.info("ბალანზე მეტი თანხის გატანის მცდელობა")
        except ValueError:
            print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვითი მნიშვნელობები")
            logging.info("შეყვანის ველის არასწორი ფორმატი")

    # თანხის შეტანის ოპერაცია
    elif choice == "a":
        try:
            user_input = input("\nმიუთითეთ რამდენი ლარის შეტანა გსურთ: ")
            add_money = float(user_input)
            if add_money <= 1000:
                balance = round(balance + add_money, 2)
                print(f"ოპერაცია წარმატებით დასრულდა.")
                print(f"თქვენს ბალანზსე არის {balance} ₾\n")
                logging.info(f"მომხმარებელმა შემოიტანა {add_money} ლარი")
            else:
                print("ერთჯერადად 1000 ლარზე მეტის შეტანა შეუძლებელია\n")
                logging.info("ზედმეტად დიდი თანხის შეტანას მცდელობა")
        except ValueError:
            print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვითი მნიშვნელობები")
            logging.info("შეყვანის ველის არასწორი ფორმატი")

    elif choice == "exit":
        logging.info("მუშაობის დასრულება")
        print(" ." * 20)
        print("მადლობა ბანკომატით სარგებლობისთვის.")
        break

    else:
        logging.info("არარსებული ოპერაციის მოთხოვნა")