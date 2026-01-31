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

def main():
    deck = create_deck()
    player_hand = deal_hand(deck)
    dealer_hand = deal_hand(deck)

    print("Player hand:", player_hand)
    print("Dealer hand:", dealer_hand)
    print("Cards left in deck:", len(deck))

if __name__ == "__main__":
    main()