#   Tbilisi Comm School x GITA: Python
#   Lesson 2
#   Giorgi Goderdzishvili
#
#   ამოცანა №6: გადაიყვანეთ 3670 წამი საათებად და წუთებად

seconds = 3670
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = (seconds % 3600) % 60
print(f"ამოცანა №6\n{seconds} წამში არის {hours} საათი, {minutes} წუთი და {sec} წამი\n")