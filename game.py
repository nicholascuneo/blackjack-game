"""

"""
# Form a complete suit of cards
def generate_suit(card_ranks, suit_symbol):
    return [rank + suit_symbol for rank in card_ranks]

# Create main gameplay deck based on player preferred number of standard decks
def create_game_deck(card_ranks, num_decks=1):
    # Generate all suits for a single deck
    clubs = generate_suit(ranks, 'c')
    diamonds = generate_suit(ranks, 'd')
    hearts = generate_suit(ranks, 'h')
    spades = generate_suit(ranks, 's')

    # Combine all suits to form a single complete deck
    single_deck = clubs + diamonds + hearts + spades

    # Form complete game deck based on num_decks
    game_deck = single_deck * num_decks

    return game_deck

#for card in face_cards:
#    clubs.append(card + 'c')

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' , 'A']
