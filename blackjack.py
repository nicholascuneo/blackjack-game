"""
Blackjack Game

This program simulates a simplified version of the card game Blackjack.
Players compete against the dealer to achieve a hand value as close to 21
as possible without exceeding it ("busting"). The game supports:
- Multiple decks (user-specified, defaults to 2 decks)
- Automatic deck reshuffling when half of the cards are used
- Basic Blackjack rules, including the dealer standing on hard 17
- Support for betting with a starting bank of $100

How to Play:
1. The player starts with $100 in the bank and can place bets on each hand.
2. Commands during gameplay:
   - "Hit" (or "h") to draw another card.
   - "Stay" (or "s") to end the turn and let the dealer play.
3. The game ends when the player runs out of money or chooses to quit.

"""

import os
import platform
import random


def clear_screen():
    """Clear screen for better readability."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def generate_suit(card_ranks, suit_initial):
    """Form a complete suit of cards"""
    return [rank + suit_initial for rank in card_ranks]


def create_game_deck(num_decks=2):
    """Create main gameplay deck based on the preferred number of decks"""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    # Generate all suits for a single deck
    clubs = generate_suit(ranks, "c")
    diamonds = generate_suit(ranks, "d")
    hearts = generate_suit(ranks, "h")
    spades = generate_suit(ranks, "s")

    # Combine all suits to form a single complete deck
    single_deck = clubs + diamonds + hearts + spades

    # Form complete game deck based on num_decks
    game_deck = single_deck * num_decks
    return game_deck


def print_cards(cards):
    """Render cards side by side and return a string representation of the cards"""
    # Create dictionary for suit symbols
    suit_symbols = {"c": "♣", "d": "♦", "h": "♥", "s": "♠"}

    # Convert each card to a formatted string
    card_lines = [""] * 7  # Each card has 7 lines in ASCII format

    for card in cards:
        rank, suit = card[:-1], card[-1]
        suit_symbol = suit_symbols.get(suit, "?")
        card_template = [
            "+---------+",
            f"|{rank:<2}       |",
            "|         |",
            f"|    {suit_symbol}    |",
            "|         |",
            f"|       {rank:>2}|",
            "+---------+",
        ]

        # Append each line of the card to the corresponding line in card_lines
        for i in range(len(card_lines)):
            card_lines[i] += card_template[i] + "  "  # Add space between cards

    # Print each line of cards side by side
    return "\n".join(card_lines)


def card_value(card):
    """Assign numerical value to face cards and return it"""
    rank = card[:-1]
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)  # Convert rank to integer for numeric cards


def calculate_hand_value(hand):
    """Calculate the total value of a hand, adjusting the value of aces if the total exceeds 21"""
    values = [card_value(card) for card in hand]
    total = sum(values)
    # Adjust for aces if total exceeds 21
    ace_count = values.count(11)
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total


def draw_card(hand, deck):
    """Draw a card and add it to the hand. Modifies the hand in place."""
    hand.append(deck.pop())  # Remove top card from deck and add to hand
    return hand


def display_hands(dealer, player, hide_dealer_first_card=True):
    """Displays the dealer's and player's hands side by side"""
    print("\n====================== HAND STATUS ======================")
    print("Dealer's Hand:")
    if hide_dealer_first_card:
        # Hide the dealer's first card
        hidden_hand = dealer[:1] + ["??"]
        print(print_cards(hidden_hand))
        dealer_total = "??"  # Hide total when first card is hidden
    else:
        # Show dealer's full hand
        print(print_cards(dealer))
        dealer_total = calculate_hand_value(dealer)

    print(f"Dealer Total: {dealer_total}")
    print("\nPlayer's hand:")
    print(print_cards(player))
    print(f"Your Total: {calculate_hand_value(player)}")
    print("=======================================================\n")


def instructions():
    """Print game instructions"""
    print(
        """\n=============================================
    ♠ ♥ ♦ ♣ WELCOME TO BLACKJACK! ♣ ♦ ♥ ♠
=============================================
Draw cards to beat the dealer's hand without \nexceeding 21.

House Rules:
  - Dealer stands on hard 17.
  - Blackjack pays 3 to 2.
  - Reno rule: Double down only on 9, 10, 11.

Commands:
  - Hit: Draw another card.
  - Stay: Keep your hand and end your turn.
  - Help: View instructions.
  - Quit: Exit the game.
=============================================
"""
    )


def main():
    """Main game loop"""
    # Initialize player bank with 100 bucks
    bank = 100
    bet = 0

    clear_screen()
    instructions()
    input("\nPress Enter to continue...")
    clear_screen()

    try:
        num_decks = int(
            input("\nEnter the number of decks to play with (e.g., 1 or 2): ")
        )
        clear_screen()
    except ValueError:
        print("\nInvalid input! Defaulting to 2 decks.")
        input("\nPress Enter to continue...")
        clear_screen()
        num_decks = 2

    game_deck = create_game_deck(num_decks)
    random.shuffle(game_deck)  # Shuffle game deck

    print("Game deck created with {} cards".format(len(game_deck)))
    print("=============================================")

    while bank > 0:
        print("Bank: ${}".format(bank))

        # Input validation for betting
        while True:
            bet = input("Enter your bet (min. 5) or 'q' to quit: ").strip().lower()
            if bet in ["q", "quit"]:
                print("Thanks for playing! Goodbye!")
                return  # Exit main() completely and end game
            if bet.isdigit() and 5 <= int(bet) <= bank:
                bet = int(bet)
                break  # Break out of input validation if bet is valid
            print("Invalid bet. Please try again.")

        bank -= bet

        # Dealer and player draw 2 cards to start
        dealer_hand = []
        player_hand = []
        for _ in range(2):
            draw_card(dealer_hand, game_deck)
            draw_card(player_hand, game_deck)

        # Display dealer and player hands
        display_hands(dealer_hand, player_hand, hide_dealer_first_card=True)

        # Check for BlackJack
        if calculate_hand_value(player_hand) == 21:
            clear_screen()
            display_hands(dealer_hand, player_hand, hide_dealer_first_card=False)
            print("BLACKJACK!!")
            # Blackjack pays 3 to 2
            bank += int(2.5 * bet)
            input("\nPress Enter to continue..")
            clear_screen()
            continue

        # Player move
        while calculate_hand_value(player_hand) <= 21:
            if len(player_hand) == 2 and calculate_hand_value(player_hand) in [
                9,
                10,
                11,
            ]:
                if bank >= bet:
                    player_move = (
                        input("Hit, Stay, or Double Down? (h/s/dd): ").strip().lower()
                    )
                else:
                    player_move = input("Hit or Stay? (h/s): ").strip().lower()
            else:
                player_move = input("Hit or Stay? (h/s): ").strip().lower()

            if player_move in ["stay", "s"]:
                clear_screen()
                break
            elif player_move in ["hit", "h"]:
                clear_screen()
                # Draw another card and add to player hand
                draw_card(player_hand, game_deck)
                # Print dealer hand and updated player hand
                display_hands(dealer_hand, player_hand, hide_dealer_first_card=True)
            elif (
                player_move in ["double down", "dd", "d"]
                and len(player_hand) == 2
                and calculate_hand_value(player_hand) in [9, 10, 11]
            ):
                if bank >= bet:
                    # Subtract from bank and double bet
                    bank -= bet
                    bet *= 2
                    # Draw single card and end hand
                    draw_card(player_hand, game_deck)
                    print("\nYou doubled down!")
                    display_hands(dealer_hand, player_hand, hide_dealer_first_card=True)
                    input("Press Enter to continue..")
                    break
                else:
                    print("Insufficient funds to double down.")
            elif player_move in ["help", "?"]:
                instructions()
                display_hands(dealer_hand, player_hand, hide_dealer_first_card=True)
            else:
                print("Invalid input.")

        if calculate_hand_value(player_hand) > 21:
            print("You busted! You exceeded 21. Dealer wins.")
            input("\nPress Enter to continue...")
            clear_screen()
            continue

        # Once player holds, reveal dealer's full hand
        display_hands(dealer_hand, player_hand, hide_dealer_first_card=False)
        dealer_total = calculate_hand_value(dealer_hand)
        player_total = calculate_hand_value(player_hand)

        # Dealer stands on hard 17
        while dealer_total < 17:
            draw_card(dealer_hand, game_deck)
            display_hands(dealer_hand, player_hand, hide_dealer_first_card=False)
            # Update dealer total after each card draw
            dealer_total = calculate_hand_value(dealer_hand)

        if dealer_total > 21 or player_total > dealer_total:
            print("YOU WIN!!\n")
            bank += 2 * bet  # Add winnings to bank
        elif dealer_total == player_total:
            print("PUSH!! It's a tie.\n")
            bank += bet  # Add bet back to bank
        else:
            print("House Wins..\n")

        # Reshuffle deck when game deck is half depleted
        if len(game_deck) < (0.5 * len(create_game_deck(num_decks))):
            print("Shuffling a new deck...\n")
            game_deck = create_game_deck(num_decks)
            random.shuffle(game_deck)

        input("Press Enter to continue...")
        clear_screen()

    print("\nYou're out of money.. Game over.")


if __name__ == "__main__":
    main()
