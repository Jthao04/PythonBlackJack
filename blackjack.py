import random

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_hand(deck):
    hand = []
    for _ in range(2):
        hand.append(deck.pop())
    return hand

def hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
            aces += 1
        else:
            total += int(rank)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

def player_turn(hand, deck):
    total = hand_value(hand)

    while True:
        print("Your hand:", hand)
        print("Your total:", total)
        choice = input("Would you like to hit or stand? ").lower()

        if choice == "hit":
            card = deck.pop()
            hand.append(card)
            total = hand_value(hand)
            if total > 21:
                print("Bust! Your total is", total)
                break
        elif choice == "stand":
            print("You chose to stand. Total:", total)
            break
        else:
            print("Invalid choice. Type 'hit' or 'stand'.")

    return total, hand

def main():
    deck = create_deck()
    player_hand = deal_hand(deck)
    dealer_hand = deal_hand(deck)

    print("Player hand:", player_hand)
    print("Dealer shows:", dealer_hand[0])
    print("Cards left in deck:", len(deck))

    player_total, player_hand = player_turn(player_hand, deck)

    print("Player final hand:", player_hand)
    print("Player final total:", player_total)

if __name__ == "__main__":
    main()