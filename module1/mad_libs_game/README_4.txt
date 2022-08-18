Now you are ready to finish your random story program!

The last remaining task is to implement backreferences---the numeric
blanks that refer to a word that you have previously used.

As a quick reminder, all blanks (both category and numeric), count in
the numbering scheme, so if we look at


Once upon a time there was a _animal.  The _0 lived in a very scary _place.
One day, the _0 left his _2 and went in search of a _food.  


We will see that the blanks are

0: _animal
1: _0
2: _place
3: _0
4: _2
5: _food

Accordingly, the _2 blank references whatever place was selected.

You should now go modify your randomStory function to track which words
were used in each blank, and whenever you encounter a numeric blank,
use the appropriate previously selected word.