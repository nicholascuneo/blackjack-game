"""

"""
import random as random

# Form a complete suit of cards
def generate_suit(card_ranks, suit_initial):
    return [rank + suit_initial for rank in card_ranks]

# Create main gameplay deck based on player preferred number of standard decks
def create_game_deck(num_decks=2):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

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

# Function to return realistic looking cards
def print_card(rank, suit):
    # Create dictionary for suit symbols
    suit_symbols = {
        'c': '♣',
        'd': '♦',
        'h': '♥',
        's': '♠'

    }

    # Default to '?' is suit is not found
    suit_symbol = suit_symbols.get(suit, '?')

    # Format card layout
    card_template = """
    +---------+
    |{0:<2}       |
    |         |
    |    {1}    |
    |         |
    |       {0:>2}|
    +---------+
    """.format(rank, suit_symbol)

    return card_template

def main():
    #Initialize player bank with 100 bucks
    bank = 100
    num_decks = 2 #int(input("How many decks would you like to play with? "))
    game_deck = create_game_deck(num_decks)

    #print(game_deck)
    #print("Game deck created with {} decks of cards".format(num_decks))
    #print("Game deck created with {} number of cards".format(len(game_deck)))
#FIXME
    dealer_hand = random.choices(game_deck, k=2)
    dealer_card1 = dealer_hand[0]
    dealer_card2 = dealer_hand[1]
    card1_suit = dealer_card1[-1]
    card1_rank = dealer_card1[:-1]
    card2_suit = dealer_card2[-1]
    card2_rank = dealer_card2[:-1]
#FIXME
    player_hand = random.choices(game_deck, k=2)
    player_card1 = player_hand[0]
    player_card2 = player_hand[1]
    pcard1_suit = player_card1[-1]
    pcard1_rank = player_card1[:-1]
    pcard2_suit = player_card2[-1]
    pcard2_rank = player_card2[:-1]



    #print(dealer_card1)
    #print(dealer_card2)
    #print(card1_suit)
    #print(card1_rank)
    #print_card(card1_rank, card1_suit)
#FIXME
    print("Dealer hand: |{}| |X|".format(dealer_hand[1]))
    print("Dealer hand: {}".format(print_card(card1_rank, card1_suit)))
    print(dealer_hand)

    #player_hand = random.choices(game_deck, k=2)
    #print("Your hand: |{}| |{}|".format(player_hand[1], player_hand[0]))


main()