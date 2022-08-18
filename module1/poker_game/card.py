ACE = 14
KING = 13
QUEEN = 12
JACK = 11


def value_from_letter(let):
    letter_to_value = {'?': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return letter_to_value[let]
    pass


def check_suit(let):
    suits_dict = {'?': 0, 'c': 1, 'd': 2, 'h': 3, 's': 4}
    return suits_dict[let]
    pass


def letter_from_value(val):
    value_to_letter = {0: '?', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '0', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    return value_to_letter[val]
    pass

class Card:
    '''
    This is a class for creating a card with valid values and suits.

    Attributes:
        values(list): List of values of cards in a standard deck.
        suits(list): List of suits in a sandard card deck.
    '''

    values = ['?', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    suits = ['?', 'c', 'd', 'h', 's']

    def __init__(self, value=None, suit=None):
        if value is None:
            value = '?'
        if suit is None:
            suit = '?'
        if(value not in self.values or suit not in self.suits):
            raise ValueError("Enter valid card and suit")

        if((value == '?' and suit != '?') or (value != '?' and suit == '?')):
            raise ValueError("Enter valid card and suit")

        self.value = value_from_letter(value)
        self.suit = suit
        pass

    def __str__(self):
        value = letter_from_value(self.value)
        suit = self.suit
        return value + suit
        pass

    def __repr__(self):
        card_name = self.__str__()
        return 'Card(' + '{}'.format(card_name) + ')'
        pass
    def __eq__(self, other):
        if(self.value == other.value and self.suit == other.suit):
            return True
        else:
            return False
        pass

    def __lt__(self, other):
        if(self.value < other.value):
            return True
        elif(self.value == other.value):
            self_suit = check_suit(self.suit)
            other_suit = check_suit(other.suit)
            if(self_suit < other_suit):
                return True
            return False
        return False
        pass

    def is_known(self):
        value = letter_from_value(self.value)
        if (value == '?' or self.suit == '?'):
            return False
        return True
        pass
    pass


def card_from_num(num):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A']
    suits = ['c', 'd', 'h', 's']
    deck = {}
    idx = 0

    if (num not in range(52)):
        raise ValueError("Range of number should be between 0-51 (inclusive)")
    for value in values:
        for suit in suits:
            card = Card(value, suit)
            if (card.is_known()):
                deck[idx] = card
                idx += 1
    return deck[num]
