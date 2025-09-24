import itertools
ingredients = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]
recipes = {
    frozenset(pair): ""
    for pair in itertools.combinations_with_replacement(ingredients, 2)
}
for combination, result in recipes.items():
    print(f"frozenset({list(combination)}): \"{result}\",")
