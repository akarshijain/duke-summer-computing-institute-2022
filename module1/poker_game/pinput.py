# import statements here
import random
from card import Card, card_from_num
from deck import Deck
from future import FutureCards


def hand_from_string(s, fc):
    card_string = s.split(" ")
    deck_in_hand = Deck()

    for card_str in card_string:
        if(card_str[0] == '?'):
            ind = int(card_str[1:])
            fc.add_future_card(ind, deck_in_hand.add_placeholder_card())
        else:
            value = card_str[0]
            suit = card_str[1]
            card_in_hand = Card(value, suit)
            deck_in_hand.add_card(card_in_hand)

    return deck_in_hand
    pass


def read_input(file, fc):
    with open(file) as input:
        list_of_hands = []
        for line in input:
            hand = hand_from_string(line, fc)
            list_of_hands.append(hand)
    return list_of_hands
    pass
