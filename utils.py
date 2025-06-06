from treys import Card

class Range:
    # class to represent a range of poker hands
    def __init__(self):
        self.hands = set() # Using a set to avoid duplicates
    
    # Adds a card to the range
    def add_hand(self, card):
        if isinstance(card, Hand):
            self.hands.add(card)
        else:
            raise ValueError("Expected a Hand instance")
    
    # Removes a card from the range
    def remove_hand(self, hand):
        # Ensure card is a Card instance
        if not isinstance(hand, Hand):
            raise ValueError("Expected a Hand instance")

        # check if card is in the range
        if hand in self.hands:
            self.hands.remove(hand)
        else:
            raise ValueError("Hand not found in range")
    
    def __str__(self):
        return ", ".join(str(hand) for hand in self.hands)

class Hand:
    # class to represent a poker hand
    def __init__(self, cards):
        if len(cards) != 2:
            raise ValueError("A hand must consist of exactly two cards")
        if cards[0] == cards[1]:
            raise ValueError("A hand cannot consist of two identical cards")


        self.cards = set() # using a set to avoid duplicates and for comparison without order
        for card in cards:
            self.cards.add(card)
            
    def __eq__(self, other):
        if isinstance(other, Hand):
            return self.cards == other.cards
        return False
    
    def __str__(self):
        return f"Hand: {', '.join(Card.int_to_pretty_str(card) for card in self.cards)}"
    
    def __hash__(self):
        hash_value = 1
        for card in self.cards:
            hash_value *= card
        return hash_value

# def add_pocket_pairs():