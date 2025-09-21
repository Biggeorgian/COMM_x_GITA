import itertools

# 1. საწყისი ინგრედიენტები
ingredients = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი", "ჩიტი", "მთვარე", "ვარდი", "ბატი", "ბალიში", "ვაშლის ყვავილი",
               "ყვავილის ფურცელი", "ნავი", "ვაშლის კომპოტი", "თაიგული", "სუნამო", "ზღვა"]

# 2. ვიყენებთ Dictionary Comprehension-ს და itertools-ს, რომ შევქმნათ
#    ყველა შესაძლო რეცეპტის ლექსიკონი.
recipes = {
    # გასაღებად ვიყენებთ frozenset-ს, რადგან წყვილში თანმიმდევრობას მნიშვნელობა არ აქვს
    frozenset(pair): ""
    # ვიღებთ ყველა 2-ელემენტიან კომბინაციას, საკუთარ თავთან გამეორების ჩათვლით
    for pair in itertools.combinations_with_replacement(ingredients, 2)
}

# 3. ვბეჭდავთ შედეგს ლამაზად
print("--- ყველა შესაძლო რეცეპტი ---")
for combination, result in recipes.items():
    # frozenset-ს ვაქცევთ სიად, რომ ლამაზად დავბეჭდოთ
    print(f"frozenset({list(combination)}): \"{result}\",")

print(f"\nსულ შეიქმნა {len(recipes)} უნიკალური რეცეპტი.")