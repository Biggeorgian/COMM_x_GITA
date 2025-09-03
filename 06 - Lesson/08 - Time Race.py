#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   რიცხვის გამოცნობა ტაიმერით

import random
from datetime import datetime, timedelta
import time

start_time = datetime.now()
print(f"🏃‍♂️‍➡️🏃‍➡️ გარბენი დაიწყო {start_time.strftime("%H:%M:%S")}")
time.sleep(2)

player1 = start_time + timedelta(seconds=random.randint(5,20))
player2 = start_time + timedelta(seconds=random.randint(5,20))

if player1 < player2:
    print(f"\n{player1.strftime("%H:%M:%S")} . . . .🏃‍♂️‍➡️. 🏁🏃‍➡️ 🥇")
    print(f"გამარჯვებულია პირველი მორბენალი. ️ ის ფინიშამდე მივიდა {(player1 - start_time).seconds} წამში")
elif player2 < player1:
    print(f"\n{player2.strftime("%H:%M:%S")} . . . . 🏃‍➡️ . . 🏁 🏃‍♂️‍➡️ 🥇")
    print(f"გამარჯვებულია მეორე მორბენალი. 🏃‍♂️‍➡️ ის ფინიშამდე მივიდა {(player2 - start_time).seconds} წამში")
else:
    print(f"\n🥳 ორი გამარჯვებული გვყავს. ორივე მორბენალს ფინიშისთვის {(player1 - start_time).seconds} წამი დასჭირდა")