#   Tbilisi Comm School x GITA: Python
#   Lesson 6
#   Giorgi Goderdzishvili
#
#   დაადგინეთ რამდენი კვირაა დარჩენილი ახალ წლამდე

from datetime import datetime

today = datetime.now().today()
new_year = datetime(today.year + 1, 1, 1)
weeks_until_ny = (new_year - today).days // 7

print(f"ახალ წლამდე დარჩენილია {weeks_until_ny} კვირა")
