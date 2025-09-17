import logging
import random

logging.basicConfig(
    filename="quiz_log_01.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)
math_expressions = "+-*/"
answer = 0
score = 0
i = 0

while i <= 4:
    random_number1 = random.randint(0, 10)
    random_number2 = random.randint(0, 10)
    random_expression = random.choice(math_expressions)
    i += 1

    if random_expression == "/" and random_number1 % random_number2 != 0:
        i -= 1
        continue

    question = f"რამდენია: {random_number1} {random_expression} {random_number2} = "

    try:
        user_input = int(input(question))
        if random_expression == "+":
            answer = random_number1 + random_number2
        elif random_expression == "-":
            answer = random_number1 - random_number2
        elif random_expression == "*":
            answer = random_number1 * random_number2
        elif random_expression == "/":
            answer = random_number1 / random_number2

        if answer == int(user_input):
            score += 10
            logging.info(
                f"კითხვა: {question.strip()} | "
                f"გამოსაცდელის პასუხი: {user_input} სწორია | "
                f"ჯამური ქულა: {score}"
            )
        else:
            logging.info(
                f"კითხვა: {question.strip()} | "
                f"გამოსაცდელის პასუხი: {user_input} მცდარია! | "
                f"ჯამური ქულა: {score}"
            )

    except ValueError:
        print(f"დაშვებულია მხოლოდ რიცხვით მნიშვნელობების შეყვანა")

print(f"{int(score / 10)} სწორი პასუხი: . თქვენ დააგროვეთ {score} ქულა")