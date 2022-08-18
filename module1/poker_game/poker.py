import sys
from future import FutureCards
from pinput import read_input
from deck import build_remaining_deck
from evaluate import compare_hands


def find_winning_hand(hands, n):
    num_winner = 0
    winner = hands[0]

    for i in range(1, n):
        result = compare_hands(winner, hands[i])
        if(result == 0):
            num_winner = n
        if(result < 0):
            num_winner = i
            winner = hands[i]
    return num_winner


# provided
def print_results(wins, n):
    for i in range(0, len(wins) - 1):
        print('Hand {} won {} / {} times'.format(i, wins[i], n))
        pass
    print('and there were {} ties'.format(wins[len(wins) - 1]))
    pass


def main():
    # get count of command line arguments
    argc = len(sys.argv)

    # check user input
    if(argc < 2 or argc > 3):
        sys.exit(1)

    if(argc == 3):
        num_trials = int(sys.argv[2])
    else:
        num_trials = 10000

    # read from file
    filename = sys.argv[1]
    fc = FutureCards()

    hands = read_input(filename, fc)
    remaining_cards = build_remaining_deck(hands)

    # do monte carlos
    wins = [0]*(len(hands)+1)

    for i in range(num_trials):
        remaining_cards.shuffle()
        fc.future_cards_from_deck(remaining_cards)

        num_winner = find_winning_hand(hands, len(hands))
        wins[num_winner] += 1

    # print results
    print_results(wins, num_trials)
    pass

if __name__ == '__main__':
    main()