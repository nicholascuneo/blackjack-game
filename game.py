"""

"""
import random as random
import os
import platform

# Clear screen to avoid clutter
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

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

# Assign integer value to face cards
def card_value(card):
    rank = card[:-1]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank) # Convert rank to integer for numeric cards

 # Calculate total value of hand
def calculate_hand_value(hand):
    values = [card_value(card) for card in hand]
    total   = sum(values)
    # Adjust for aces if total exceeds 21
    ace_count = values.count(11)
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total


# Function to draw additional cards after initial hand
def draw_card(hand, deck):
    card = deck.pop() # Remove top card from deck
    hand.append(card) # Add card to hand
    
    return hand


def display_hands(dealer, player, hide_dealer_first_card=True):
    print("Dealer hand:")
    if hide_dealer_first_card:
        # Hide the dealer's first card
        hidden_hand = dealer[:1] + ["??"]
        print(print_cards(hidden_hand))
        dealer_total = "??" # Hide total when first card is hidden
    else:
        # Show dealer's full hand
        print(print_cards(dealer))
        dealer_total = calculate_hand_value(dealer)

    #print(f"DEALER TOTAL: {dealer_total}")
    print("Player hand:")
    print(print_cards(player))
    #print(f"YOUR TOTAL: {calculate_hand_value(player)}")
    print(f"DEALER TOTAL: {dealer_total} | YOUR TOTAL: {calculate_hand_value(player)}")


def instructions():
    print("Objective: Draw cards to beat the Dealer's hand without going over 21.\n"
          "\nHit: Type 'Hit' to draw another card.\n"
          "Stay: Type Stay to hold your total and let the dealer play their turn.\n"
          "Help: Type h or help to display these instructions again.\n"
          "Quit: Type q or exit to quit the game.")


#def show_status():


def main():
    #Initialize player bank with 100 bucks
    bank = 100
    bet = 0
    
    print("WELCOME TO BLACKJACK")
    instructions()
    input("\nPress Enter to continue...")
    clear_screen()

    num_decks = int(input("\nEnter the number of decks to play with: "))
    game_deck = create_game_deck(num_decks)
    random.shuffle(game_deck) # Shuffle game deck

    print("Game deck created with {} cards".format(len(game_deck)))

    
    while bank > 0:
        print("Bank: ${}".format(bank))

        #Input validation for betting
        while True:
            action = input("Enter you bet (min. 5) or 'q' to quit: ").lower()
            if action == 'q':
                print("Thanks for playing!")
                return # Exit main() completely and end game
            if not action.isdigit():
                print("Please enter a valid number.")
                continue
            # Convert valid bet to integer
            bet = int(action)
            if (bet < 5) or (bet > bank):
                print("Invalid bet.")
                continue
            # Valid bet, exit validation loop
            break

        bank -= bet
        
        # Dealer and player draw 2 cards to start
        dealer_hand = []
        player_hand = []
        for c in range(2):
            draw_card(dealer_hand, game_deck)
            draw_card(player_hand, game_deck)
    
        # Display dealer and player hands
        display_hands(dealer_hand, player_hand, hide_dealer_first_card=True)
        print("Bank: ${}  Bet: ${}".format(bank, bet))

        # Player move
        while calculate_hand_value(player_hand) <= 21:
            player_move = input("Hit or Stay?\n").title()
            if player_move == "Stay":
                break
            elif player_move == "Hit":
                # Draw another card and add to player hand
                draw_card(player_hand, game_deck)
                # Print dealer hand and updated player hand
                display_hands(dealer_hand, player_hand, hide_dealer_first_card=True)
            else:
                print("Invalid input.")
            
        if calculate_hand_value(player_hand) > 21:
            print("You busted!")
            continue

        # Once player holds, reveal dealer's full hand
        display_hands(dealer_hand, player_hand, hide_dealer_first_card=False)
        input("\nPress Enter to continue...")

        # Dealer stands on hard 17
        while calculate_hand_value(dealer_hand) < 17:
            draw_card(dealer_hand, game_deck)
            
        display_hands(dealer_hand, player_hand, hide_dealer_first_card=False)
        dealer_total = calculate_hand_value(dealer_hand)
        player_total = calculate_hand_value(player_hand)
        
        if dealer_total > 21 or player_total > dealer_total:
            print("You Win!!")
            # Add winnings to bank
            bank += 2 * bet
        elif player_total == 21 and len(player_hand) == 2:
            print("BLACKJACK!!")
            # Blackjack pays 3 to 2
            bank += int(2.5 * bet)
        elif dealer_total == player_total:
            print("Push!!")
            # Add bet back to bank
            bank += bet
        else:
            print("House Wins")
        
        # Reshuffle deck when game deck is half depleted
        if len(game_deck) < (0.5 * len(create_game_deck(num_decks))):
            print("Shuffling a new deck...")
            game_deck = create_game_deck(num_decks)
            random.shuffle(game_deck)

    
main()