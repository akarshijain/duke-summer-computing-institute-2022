from card import Card, card_from_num, ACE, KING, QUEEN, JACK
from deck import Deck


# finds flush suit
def find_flush(hand):
    suit_dict = {}

    for card in hand.cards:
        if card.suit not in suit_dict.keys():
            suit_dict[card.suit] = 1
        else:
            suit_dict[card.suit] += 1
    for suit in suit_dict:
        if (suit_dict[suit]) >= 5:
            return suit
    return None
    pass


# makes dictionary of cards values to count of their occurances
def count_values(hand):
    suit_dict = {}
    for card in hand.cards:
        if card.value not in suit_dict.keys():
            suit_dict[card.value] = 1
        else:
            suit_dict[card.value] += 1
    return suit_dict
    pass

# uses counts dict and returns a tuple (value with most n of a kind, n)
def get_max_count(hand, counts):
    highest_value = max(list(counts.keys()))
    highest_count_key = max(counts, key=counts.get)
    highest_count = counts[highest_count_key]
    for key in counts:
        if(counts[key] == highest_count):
            return (highest_value, counts[key])
        return (highest_count_key, highest_count)
    pass


# finds index of second pair or returns -1 for no sec pair
def find_secondary_pair(hand, counts, val):
    for key in counts:
        if(counts[key] > 1 and key != val):
            return get_kind_index(hand, key)
    return -1
    pass


# get first index of value in hand
def get_kind_index(hand, value):
    for card in hand.cards:
        if card.value == value:
            return hand.cards.index(card)
    pass

# build hand with n of a kind starting at ind
def build_of_a_kind(hand, n, ind):
    ans = Deck()

    filled_cards = 0
    for i in range(n):
        ans.add_card(hand.cards[ind + i])
        filled_cards += 1

    before_cards = ind
    for i in range(before_cards):
        if(filled_cards != 5):
            ans.add_card(hand.cards[i])
            filled_cards += 1

    if(filled_cards != 5):
        remaining_cards = 5-filled_cards
        for i in range(remaining_cards):
            ans.add_card(hand.cards[ind+n+i])
            filled_cards += 1
    return ans
    pass


# adds secondary pair (for full house or two pair)
def add_pair(hand, pi, ans, ai):
    sec_pair = Deck()

    for i in range(ai):
        sec_pair.add_card(ans.cards[i])

    sec_pair.add_card(hand.cards[pi])
    sec_pair.add_card(hand.cards[pi+1])

    if(ai+2 != 5):
        if(ans.cards[ai] != hand.cards[pi]):
            sec_pair.add_card(ans.cards[ai])
        else:
            sec_pair.add_card(ans.cards[ai+2])
    return sec_pair

# helper for is_straight_at
def is_n_length_straight_at(hand, ind, fs, n):
    count_straight = 1
    if fs is None:
        for i in range(len(hand.cards)-ind-1):
            if(hand.cards[ind+i+1].value == hand.cards[ind+i].value):
                continue
            if(hand.cards[ind+i+1].value != hand.cards[ind+i].value - 1):
                return 0
            if(hand.cards[ind+i+1].value == hand.cards[ind+i].value - 1):
                count_straight += 1
                if(count_straight == n):
                    return 1
    else:
        head = Card()
        head.value = hand.cards[ind].value
        head.suit = hand.cards[ind].suit
        if(head.suit != fs):
            return 0
        for i in range(len(hand.cards)-ind-1):
            if(hand.cards[ind+i+1].suit != fs):
                continue
            if((hand.cards[ind+i+1].value != head.value - 1)):
                return 0
            if((hand.cards[ind+i+1].value == head.value - 1)):
                count_straight += 1
                if(count_straight == n):
                    return 1
            head.value = hand.cards[ind+i+1].value
            head.suit = hand.cards[ind+i+1].suit
    return 0
# helper for is_straight_at
#if Ace is at 1st position then 5, 4, 3, 2 can be at max 2nd or 3rd position because total cards are seven
def is_ace_low_straight_at(hand, ind, fs):
    if(hand.cards[ind].value != ACE):
        return 0
    if(hand.cards[ind].value == ACE):
        if(hand.cards[ind+1].value == 5):
            return is_n_length_straight_at(hand, ind+1, fs, 4)

        elif(hand.cards[ind+2].value == 5):
            return is_n_length_straight_at(hand, ind+2, fs, 4)
        elif(hand.cards[ind+3].value == 5):
            return is_n_length_straight_at(hand, ind+3, fs, 4)
        return 0
    return 0


# if fs = None, look for any straight
# if fs = suit, look for straight in suit
# returns -1 for ace-low, 1 for straight, 0 for no straight
def is_straight_at(hand, ind, fs):
    if(is_ace_low_straight_at(hand, ind, fs)):
        return -1
    return is_n_length_straight_at(hand, ind, fs, 5)
    pass

# provided
def copy_straight(hand, ind, fs, ace_low=False):
    ans = Deck()
    last_card = None
    target_len = 5
    assert not fs or hand.cards[ind].suit == fs
    if ace_low:
        assert hand.cards[ind].value == ACE
        last_card = hand.cards[ind]
        target_len = 4
        to_find = 5
        ind += 1
        pass
    else:
        # regular straight
        to_find = hand.cards[ind].value
        pass
    while len(ans.cards) < target_len:
        assert ind < len(hand.cards)
        if hand.cards[ind].value == to_find:
            if not fs or hand.cards[ind].suit == fs:
                ans.add_card(hand.cards[ind])
                to_find -= 1
                pass
            pass
        ind += 1
        pass
    if last_card is not None:
        ans.add_card(last_card)
        pass
    assert len(ans.cards) == 5
    return ans
# provided
# looks for a straight (or straight flush if fs is not None)
# calls the student's is_straight_at for each index
# if found, copy_straight returns cards used for straight
def find_straight(hand, fs):
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == 1:
            # straight
            return copy_straight(hand, i, fs)
        pass
    for i in range(0, len(hand.cards) - 4):
        is_straight = is_straight_at(hand, i, fs)
        if is_straight == -1:
            # ace-low straight
            return copy_straight(hand, i, fs, True)
        pass
    return None


# provided
# builds hand with flush suit fs
def build_flush(hand, fs):
    ans = Deck()
    i = 0
    while len(ans.cards) < 5:
        assert i < len(hand.cards)
        if hand.cards[i].suit == fs:
            ans.add_card(hand.cards[i])
            pass
        i += 1
        pass
    return ans
# provided
def evaluate_hand(hand):
    # straight flush
    fs = find_flush(hand)
    straight = find_straight(hand, fs)
    if fs and straight:
        return straight, 'straight flush'
    # four of a kind
    val_counts = count_values(hand)
    v, n = get_max_count(hand, val_counts)
    assert n <= 4
    ind = get_kind_index(hand, v)
    if n == 4:
        return build_of_a_kind(hand, 4, ind), 'four of a kind'
    # full house
    sec_pair = find_secondary_pair(hand, val_counts, v)
    if n == 3 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 3, ind)
        ans = add_pair(hand, sec_pair, ans, 3)
        return ans, 'full house'
    # flush
    if fs:
        return build_flush(hand, fs), 'flush'
    # straight
    if straight:
        return straight, 'straight'
    # three of a kind
    if n == 3:
        return build_of_a_kind(hand, 3, ind), 'three of a kind'
    # two pair
    if n == 2 and sec_pair >= 0:
        ans = build_of_a_kind(hand, 2, ind)
        ans = add_pair(hand, sec_pair, ans, 2)
        return ans, 'two pair'
    # pair
    if n == 2:
        return build_of_a_kind(hand, 2, ind), 'pair'
    # high card
    ans = Deck()
    ans.cards = hand.cards[0:5]
    return ans, 'high card'


def num_from_rank(r):
    ranks = ['high card', 'pair', 'two pair', 'three of a kind', \
                 'straight', 'flush', 'full house', \
                 'four of a kind', 'straight flush']
    return ranks.index(r)


# returns positive if hand1 > hand2,
# 0 for tie, or
# negative for hand2 > hand 1
def compare_hands(hand1, hand2):
    hand1.sort()
    hand2.sort()

    hand1_eval, rank1 = evaluate_hand(hand1)
    hand2_eval, rank2 = evaluate_hand(hand2)

    num_rank1 = num_from_rank(rank1)
    num_rank2 = num_from_rank(rank2)

    if(num_rank1 > num_rank2):
        return 1
    if(num_rank1 < num_rank2):
        return -1
    if(num_rank1 == num_rank2):
        for i in range(5):
            if(hand1_eval.cards[i].value > hand2_eval.cards[i].value):
                return 1
            if(hand1_eval.cards[i].value < hand2_eval.cards[i].value):
                return -1
            if(hand1_eval.cards[i].value == hand2_eval.cards[i].value):
                continue
    return 0
    pass
'''
card_list = []
for i in range(52):
    card_list.append(card_from_num(i))

full_deck = Deck()
for card in card_list:
    full_deck.add_card(card)

full_deck.shuffle()

hand = Deck()
for i in range(7):
    hand.add_card(full_deck.cards[i])

hand.sort()
print(hand)
print(evaluate_hand(hand))

card1 = Card('J', 's')
card2 = Card('8', 'd')
card3 = Card('Q', 'c')
card4 = Card('9', 'h')
card5 = Card('3', 'd')
card6 = Card('3', 'c')
card7 = Card('8', 'h')

card8 = Card('7', 'h')
card9 = Card('6', 'h')
card10 = Card('5', 'h')
card11 = Card('3', 's')
card12 = Card('Q', 'h')
card13 = Card('4', 's')
card14 = Card('0', 'h')

hand1 = Deck()
hand2 = Deck()

deck1 = [card1, card2, card3, card4, card5, card6, card7]
deck2 = [card8, card9, card10, card11, card12, card13, card14]
for card in deck1:
    hand1.add_card(card)

for card in deck2:
    hand2.add_card(card)

hand1.sort()
#hand2.sort()
print(hand1)
#print(hand2)
print(evaluate_hand(hand1))
#print(evaluate_hand(hand2))
#print(compare_hands(hand1, hand2))

hand1_e, rank = evaluate_hand(hand1)
#print(hand1_e)
'''
