from deck import Deck


class FutureCards:
    '''
    This class is used to handle the uknown/future cards.
    Attributes:
        future_cards: A list of decks.
    '''

    future_cards = []

    def __init__(self):
        self.future_cards = []
        pass

    def __str__(self):
        deck_string_list = []
        for deck in self.future_cards:
            deck_string_list.append(deck.__str__())
        return '\n'.join(deck_string_list)
        pass

    def __repr__(self):
        string_list = []
        idx = 0
        for deck in self.future_cards:
            string_list.append('?' + '{}'.format(idx) + ': ' + '{}'.format(deck.__str__()))
            idx += 1
        return 'FutureCards: \n' + '\n'.join(string_list)
        pass

    def add_future_card(self, ind, c):
        if(not c.is_known()):
            if(ind >= len(self.future_cards)):
                for i in range(ind - len(self.future_cards) + 1):
                    empty_deck = Deck()
                    self.future_cards.append(empty_deck)
                temp_deck = Deck()
                temp_deck.add_card(c)
                self.future_cards[ind] = temp_deck
            else:
                self.future_cards[ind].add_card(c)
        pass

    def future_cards_from_deck(self, d):
        idx = 0

        for deck in self.future_cards:
            drawn_card = d.draw()
            for i in range(len(deck.cards)):
                deck.cards[i].value = drawn_card.value
                deck.cards[i].suit = drawn_card.suit
            idx += 1
        pass
    pass
