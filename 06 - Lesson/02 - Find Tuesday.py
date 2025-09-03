#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   იპოვნეთ შემდეგი სამშაბათი

from datetime import datetime, timedelta

today = datetime.today().date()

for i in range(7):
    day = today + timedelta(days = i)
    if day.weekday() == 1:
        print(f"შემდეგი სამშაბათია: {day.strftime("%d %B %Y")}")
        break