import random
import logging
logging.basicConfig(
    filename="lottery.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)
prize = 1000000
prize_multipliers = {
    5: 0.6,
    4: 0.4,
    3: 0.2
}

lucky_numbers = set(random.sample(range(1, 47), 6))
logging.info(f"ბედნიერი რიცხვებია: {lucky_numbers}")
# print(lucky_set)

user_input = input(f"ჰარის გამოტოვებით შეიყვანეთ 6 რიცხვი "
                   f"1-დან 46-ის ჩათვლით: ")
user_ticket = set([int(num) for num in user_input.split()])
logging.info(f"მომხმარებლის ბილეთია: {user_ticket}")

matching_numbers = lucky_numbers.intersection(user_ticket)
matching_ratio = len(matching_numbers)
logging.info(f"დაემთხვა {matching_ratio} რიცხვი")

if matching_ratio == 6:
    winnings = prize
    print(f"გილოცავთ! თქვენ მოიგეთ ჯეკპოტი {winnings}₾")
    logging.info(f"მომხმარებელმა მოიგო: {winnings}₾")
elif matching_ratio in prize_multipliers:
    multiplier = prize_multipliers[matching_ratio]
    winnings = prize * multiplier
    print(f"გილოცავთ! თქვენ გამოიცანით {matching_ratio} რიცხვი "
          f"და მოიგეთ {winnings}₾")
    logging.info(f"მომხმარებელმა მოიგო: {winnings}₾")
else:
    print(f"დაემთხვა {matching_ratio} რიცხვი. სამწუხაროდ, თქვენ ვერაფერი მოიგეთ")
    logging.info(f"გათამაშება დასრულდა მოგების გარეშე")