"""

"""

face_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' , 'A']

clubs = []
diamonds = []
hearts = []
spades = []

for card in face_cards:
    clubs.append(card + 'c')

for card in face_cards:
    diamonds.append(card + 'd')

for card in face_cards:
    hearts.append(card + 'h')

for card in face_cards:
    spades.append(card + 's')

deck1 = clubs + diamonds + hearts + spades
deck2 = clubs + diamonds + hearts + spades

game_deck = deck1 + deck2
