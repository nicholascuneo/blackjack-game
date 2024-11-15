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


# Function to print multiple cards side by side
def print_cards(cards):
    # Create dictionary for suit symbols
    suit_symbols ={
        'c': '♣',
        'd': '♦',
        'h': '♥',
        's': '♠'
    }

    # Convert each card to a formatted string
    card_lines = [""] * 7 # Each card has 7 lines in ASCII format

    for card in cards:
        rank, suit = card[:-1], card[-1]
        suit_symbol = suit_symbols.get(suit, '?')
        card_template = [
            "+---------+",
            f"|{rank:<2}       |",
            "|         |",
            f"|    {suit_symbol}    |",
            "|         |",
            f"|       {rank:>2}|",
            "+---------+"
        ]

        # Append each line of the card to the corresponding line in card_lines
        for i in range(len(card_lines)):
            card_lines[i] += card_template[i] + "  " # Add space between cards
    
    # Print each line of cards side by side
    return "\n".join(card_lines)


# Function to draw additional cards after initial hand
def draw_card(hand, deck):
    hand.append((random.choice(deck)))

    return hand


#def instructions():


#def show_status():


def main():
    #Initialize player bank with 100 bucks
    bank = 100
    num_decks = int(input("Enter the number of decks to play with: "))
    game_deck = create_game_deck(num_decks)

    print("Game deck created with {} cards".format(len(game_deck)))

    
    while bank != 0:

        while True:
            bet = int(input("Enter your bet (min. 5): "))

            if bet < 5:
                print("Bet too low.")
            else:
                bank -= bet
                break
        
        # Dealer and player draw 2 cards to start
        dealer_hand = random.choices(game_deck, k=2)
        player_hand = random.choices(game_deck, k=2)
    
        # Display dealer and player hands
        print("Dealer hand:")
        print(print_cards(dealer_hand))

        print("Player hand:")
        print(print_cards(player_hand))

        # Player move
        player_move = input("Hit or Stay?\n").title()

        while player_move != "Stay":
            # Draw another card and add to player hand
            draw_card(player_hand, game_deck)
            
            # Print dealer hand and updated player hand
            print("Dealer hand:")
            print(print_cards(dealer_hand))
            
            print("Player hand:")
            print(print_cards(player_hand))
            
            player_move = input("Hit or Stay?\n").title()
    

main()