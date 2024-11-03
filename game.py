"""

"""
def generate_suit(card_ranks, suit_symbol):
    return [rank + suit_symbol for rank in card_ranks]

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' , 'A']

clubs = generate_suit(ranks, 'c')
diamonds = generate_suit(ranks, 'd')
hearts = generate_suit(ranks, 'h')
spades = generate_suit(ranks, 's')

#for card in face_cards:
#    clubs.append(card + 'c')


deck1 = clubs + diamonds + hearts + spades
deck2 = clubs + diamonds + hearts + spades

game_deck = deck1 + deck2
