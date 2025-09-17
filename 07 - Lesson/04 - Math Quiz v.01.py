import logging
logging.basicConfig(
    filename="quiz_log_01.log",
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

question_list = {
    "3 * 7": "21",
    "22 - 11": "11",
    "16 / 2": "8",
    "21 + 31": "52",
    "72 / 3": "24"
}

questions = len(question_list)
score = 0

for question, correct_answer in question_list.items():
    try:
        user_input = int(input(f"გამოთვალე {question} = "))
        if user_input == int(float(correct_answer)):
            score += 10
            logging.info(
                f"გამოთვლა: {question} = "
                f"{user_input} სწორია | "
                f"ჯამური ქულა: {score}"
            )
        else:
            logging.info(
                f"გამოთვლა: {question.strip()} = "
                f"{user_input} მცდარია! | "
                f"ჯამური ქულა: {score}"
            )

    except ValueError:
        print("დაშვებულია მხოლოდ რიცხვების შეყვანა!")

print(f"{int(score / 10)} სწორი პასუხი: თქვენ დააგროვეთ {score} ქულა")