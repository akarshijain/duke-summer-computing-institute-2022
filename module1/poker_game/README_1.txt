For the next few days, you will be working on building a program that estimates
the chances of each hand winning in poker in a situation described by an input
file. 

In this portion of the project, you are going write the Card class, as well as
any additional variables or helper functions you might need. Specifically, a
Card will represent information about a card's value and suit, as well as
convert that information to a human-readable format with a pair of letters that
describe a card. For example, the 2 of hearts would have the textual
representation '2h', where the first character is one of (2, 3, 4, 5, 6, 7, 8,
9, 0, J, Q, K, A) for the value, and the second character is one of (s, h, d,
c) for the suit.

We note that we are going to have the Card class use an internal
representation of values (numbers from 2 to 14, plus 0 for unknown)
that is easy to work with and an external representation (letters like
A, K,etc) that are easy for humans to read and write.  Anytime the
value is "inside" Card it should be in the 2-14.  Values coming in
from outside need to get converted.  For example, the constructor will
take 'A' for Ace, and need to convert it to 14. Anytime a value goes
back "outside" of Card, it should get converted back to human readable
letters (14 back to 'A').  Note how much easier these internal representations
are for things like "less than" to order cards.  Here is a quick table to help
clarify

 External Value Representation   |   Internal Value Representation
 --------------------------------+----------------------------------
             'A'                 |            14
             'K'                 |            13
             'Q'                 |            12
             'J'                 |            11 
             '0'                 |            10
             '9'                 |             9
             '8'                 |             8
             '7'                 |             7
             '6'                 |             6
             '5'                 |             5
             '4'                 |             4
             '3'                 |             3                                              
             '2'                 |             2
             '?'                 |             0

Note the external values are strings, and the internal values are integers.
             


In card.py, write:

Card class
  - value field, which should be a number 2-14 (inclusive), or 0 for a
    placeholder card (consider defining ACE = 14, KING = 13, QUEEN = 12, and
    JACK = 11 to make your code more readable). 
  - suit field, which should be a character: 's', 'h', 'd', 'c' for a known
    card or '?' for a placeholder card.
  - __init__ method to construct a card from letters for the value and suit; if
    no arguments are given, the default value letter is '?', and the default
    suit is '?'. You should make sure the arguments have the correct length and
    are valid. If not, you should raise a ValueError with a reasonable
    error message.  Note that you should not handle the ValueError here:
    the whole point of raising it is to indicate to the calling functions
    that they did something improper.
  - __str__ method to make a string representation of the card with two
    characters, for example, 'As'. 
  - __repr__ method that prints 'Card( )' around the string representation, for
    example, 'Card(As)'. 
  - __eq__ (equal to) method, which takes a parameter other and returns True if
    self and other have the same value and same suit and False otherwise.
  - __lt__ (less than) method, which takes a parameter other and returns True
    if self is less than other and False otherwise. If the cards have the same
    value, determine which suit is "less than": c < d < h < s.
  - is_known method, which returns True if the card is a card with known
    value and suit, and False otherwise (if it is a ? placeholder).

    
Other 'public' function (function should be defined in card.py, but it is not a
method of Card): 
  - card_from_num function to take a number 0-51 (inclusive) and return a Card
    in the standard deck. You can do the math however you like, but calling
    card_from_num on 0-51 (inclusive) should build a full deck. You should call
    is_known after constructing the card to make sure it is correct. If the
    argument is not in the range 0-51, you should raise a ValueError and print
    an error message.

Hint: to make your code for __init__ and __str__ easier to read, consider
abstracting parts out into the following helper functions: 
  - value_from_letter
  - check_suit 
  - letter_from_value

Now test your Card class in test-card.py. You will want to import Card
and card_from_num.