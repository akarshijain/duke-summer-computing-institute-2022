The next step in the poker project is to create a class for a Deck, which
contains a list of Cards. This class can be used to represent either a deck
of cards or a hand.

In deck.py, write:

Deck class
  - a docstring describing the class
  - cards field, which is a list of cards
  - __init__ method, which initializes the cards field to an empty list.
  - __str__ method, which should make a string containing each
    two-character string representing a card, each separated by a space,
    for example, 'As 0c 8h'.
  - __repr__ method, which has a 'Deck( )' around the string
    representation, for example, 'Deck(As 0c 8h)'. 
  - add_card method, which takes a card as a parameter and adds that card
    to the cards list. 
  - add_placeholder_card method, which adds a placeholder card to the cards 
    list and returns that card. 
  - contains method, which takes a card as a parameter and returns True if
    the deck contains that card and False otherwise. Recall that you wrote
    the __eq__ method for Card, so the == operator will use that. 
  - shuffle method, which should put the cards into a random order. There
    are many ways to do this, so choose one that appeals to you! (Check out
    the Python module random.)
  - assert_full method, which uses the 'assert [expr]' statement to make
    sure the deck contains one of every card. (You may want to make use of
    contains and card_from_num.) 
  - draw method, which takes the first card in the Deck and both puts it at
    the end of the deck and returns that card. (Consider the list methods
    pop and append.) 
  - sort method, which sorts the cards list by value and suit, from
    greatest to least. (See list's method sort or the built-in sorted
    function, both of which use the elements' < operator (which you defined
    in Card as __lt__) and have a reverse option.)

Other 'public' function (meaning this function is contained in deck.py, but
it is not a method of Deck)
  - build_remaining_deck function, which takes a list of Decks named
    "hands" and builds a deck that has all 52 cards except for those found
    in hands and returns the answer Deck. Note that each Deck in hands may
    contain duplicate cards.

Now test your Deck class in test-deck.py. Note that we have provided import 
statements that import your Deck from your deck module and Card and
card_from_num from your card module.  