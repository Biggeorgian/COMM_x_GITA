import random
decision = True
ranks = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
}
suits = ["♠", "♣", "♥", "♦"]

# შევქმნათ ფუნქცია დასტის ლექსიკონის გენერაციისთვის
def create_deck():
    return {f"{suit}{rank}": value for suit in suits for rank, value
            in ranks.items()}
# გავაკეთოთ დარიგების იმიტაცია და ამოვშალოთ დასტიდან გამოყენებული კარტი
def deal_cards(deck, hand, num_cards=1):
    drawn_cards = random.sample(list(deck.items()), num_cards)
    hand.update(drawn_cards)
    for key, value in drawn_cards:
        if key in deck:
            del deck[key]
# დავთვალოთ ქულები
def calculate_score(hand):
    return sum(hand.values())
# დავბეჭდოთ რა კარტი გვიჭირავს და რამდენი ქულაა
def display(hand, name):
    score = calculate_score(hand)
    cards_str = ", ".join(hand.keys())
    print(f"{name} კარტები: [{cards_str}] (ქულათა ჯამი: {score})")

def show_winner(player_score, comp_score):
    if player_score > 21:
        return "შენ 21 ქულაზე მეტი გაქვს, ამიტომ წააგე..."
    elif comp_score > 21:
        return "შენ მოიგე! კომპიუტერის ქულა გადაცდა 21"
    elif player_score > comp_score:
        return "გილოცავთ, თქვენ მოიგეთ!"
    elif comp_score > player_score:
        return "სამწუხაროდ მოიგო კომპიუტერმა..."
    else:
        return "რა ლამაზი დღე-ააა, იმიტომ რომ ფრე-ააააა!"
# გავუშვათ თამაში
while decision:
    # ყოველი ახალი თამაშისთვის გავანულოთ ცვლადები და დავაგენერიროთ ახალი დასტა
    cards = create_deck()
    player_moves = {}
    comp_moves = {}
    game_over = False
    print("\nმოიგებს ის, ვინც შეაგროვებს მაქსიმალურ ქულას, მაგრამ არ გადაცდება 21 ქულას")
    # დავარიგოთ 2-2 კარტი
    deal_cards(cards, player_moves, 2)
    deal_cards(cards, comp_moves, 2)

    while not game_over:
        display(player_moves, "თქვენი")
        choice = input("\nდაამატებთ კარტს (add) თუ საკმარისია (stop)? ").lower()
        if choice == "add":
            deal_cards(cards, player_moves, 1)
            # დავასრულოთ თამაში თუ მოთამაშემ 21-ზე მეტი დააგროვა
            if calculate_score(player_moves) > 21:
                game_over = True
        elif choice == "stop":
            # სანამ კომპს 17 ქულაზე ნაკლები აქვს, იმატებს კარტებს
            while calculate_score(comp_moves) < 17:
                print("ახლა კომპიუტერის სვლაა...")
                deal_cards(cards, comp_moves, 1)
            game_over = True
        else:
            print("არასწორი ბრძანება, სცადეთ თავიდან.")

    final_player_score = calculate_score(player_moves)
    final_comp_score = calculate_score(comp_moves)
    print(" ")
    display(player_moves, "თქვენი")
    display(comp_moves, "კომპიუტერის")

    # ვიძახებთ გამარჯვებულის გამომვლენ ფუნქციას
    winner_message = show_winner(final_player_score, final_comp_score)
    print(f"\n{winner_message}")

    user_choice = input("\nგინდა ხელახლა ითამაშო? yes / no : ")
    if user_choice == "yes":
        decision = True
    else:
        decision = False