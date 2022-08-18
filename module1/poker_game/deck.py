from card import Card, card_from_num
import random


class Deck:
    '''
    This class is a representation of deck of cards.
    Attributes:
        cards(list): This list contains a list of cards.
    '''
    cards = []

    def __init__(self):
        self.cards = []
        pass

    def __str__(self):
        cards_list_string = []
        for card in self.cards:
            cards_list_string.append(card.__str__())
        return (" ".join(cards_list_string))

    def __repr__(self):
        card_list = self.__str__()
        return 'Deck(' + '{}'.format(card_list) + ')'
        pass

    def add_card(self, c):
        self.cards.append(c)
        pass

    def add_placeholder_card(self):
        placeholder_card = Card()
        self.add_card(placeholder_card)
        return placeholder_card
        pass
    def contains(self, c):
        for card in self.cards:
            if(c.__eq__(card)):
                return True
        return False
        pass

    def shuffle(self):
        return random.shuffle(self.cards)
        pass

    def assert_full(self):
        test_deck = Deck()
        num_cards = 52

        for i in range(num_cards):
            test_deck.add_card(card_from_num(i))

        for card in test_deck.cards:
            assert self.contains(card)

        assert len(test_deck.cards) == len(self.cards)
        return True
        pass

    # takes card from from deck, appends it to end, and returns it
    def draw(self):
        top_card = self.cards.pop(0)
        self.cards.append(top_card)
        return top_card
        pass

    # sorts high to low
    def sort(self):
        return self.cards.sort(reverse=True)
        pass
    pass

# builds and returns complete deck except for cards in hands
def build_remaining_deck(hands):
    full_deck = Deck()
    num_cards = 52

    for i in range(num_cards):
        full_deck.add_card(card_from_num(i))

    for deck in hands:
        for card in deck.cards:
            if(card in full_deck.cards and card.is_known()):
                full_deck.cards.remove(card)

    return full_deck
    pass
