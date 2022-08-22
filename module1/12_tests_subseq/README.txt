In your next assignment, you are going to write Python code to find
the longest contiguous (meaning all together) increasing subsequence
in a list.  Before you do that, you are going to think about some test
cases for various mistakes that a programmer could make in doing this
assignment.  Not only will thinking through these test cases help you
avoid such mistakes, but it will also give you a nice set of test
cases to work from when you do the next assignment.  For each tests
case, you are going to write a little bit of Python code that will
call the maxSeq function on an input which you think is an appropriate
test case, and will then check that the result is correct.  You should
call the check function (which is not a standard Python function, but
is something for this assignment) passing in a first argument that is
the input to maxSeq( a list of numbers) and a second argument which is
what you expect the correct answer to be.  For example, if you wanted
to test that maxSeq([1,2,3]) gave an answer of 3, you would do:

check([1, 2, 3], 3)

If you want to see he instructions for the next assignment
(where you will be writing the code), you can look in the file
next-README.  Note that you should NOT write the program
until you have passed this testing assignment. You will write
the code for maxSeq in the next assignment.

As with the match5 assignment, one correct and several broken
implementations can be found in 
  /usr/local/sci/subseq 

These are provided as bytecode, .pyc files.  Each of them contains
an implementation of maxSeq, but you cannot see the code for it.
You should write a code in test-subseq.py that will test the maxSeq
function.  Note that we have already written code to import
the maxSeq function, and a "check" function which takes
a list to pass to maxSeq, and the expected answer.   

The script run_all.sh will test your test-subseq.py with all of the
implementations. 

Below we are going to tell you what is wrong with each broken
implementation, however, before you proceed, we want you to take
a few minutes to think about what test cases you need to write.

Broken implementation 0:
  Suppose the programmer did not properly handle the empty list

Broken implementation 1:
  Suppose the programmer mistakenly wrote code to count non-decreasing
  rather than strictly increasing sequences (that is, they consider
  equal elements to continue a sequence when they should only consider
  greater elements to continue a sequence).  

Broken implementation 2:
  Suppose the programmer made a mistake in which they were off by one
  in iterating over the input list and missed the last element.  

Broken implementation 3:
  Suppose the programmer made a mistake of returning the length of the
  last increasing subsequence rather than the longest increasing
  subsequence.

Broken implementation 4:
  Suppose the programmer made the mistake of putting their return
  statement in the wrong place, such that they return after the end of
  the first increasing subsequence, rather than finding the longest.

Broken implementation 5:

  Suppose the programmer decided to keep track of the previous value
  in the sequence to compare against (the last number seen to see if
  this number is bigger than it).  While this approach can work fine,
  the programmer made an incorrect assumption in initializing this
  value (picking what they would compare the first element in a newly
  started sequence against). In particular, they chose to initialize
  it to 0.

Broken implementation 6:

  Suppose the programmer iterates through the input, and at each step
  checks if the current number is larger than the previous or
  less-than-or-equal-to the previous.  If the current number is
  larger, the programmer increments the length of the current
  sequence.  If the current number is less-than-or-equal-to the
  previous number, then the current sequence has ended, so the
  programmer checks if the current sequence is longer than the max
  sequence (and if so, updates the max sequence), then resets the
  current sequence length to 0.  At the end, the programmer returns
  the max sequence length.

  This approach has a mistake where, if the longest sequences is in a
  particular position in the input, the maximum sequence length will
  not be updated with the current sequence length.  Write a test case
  which demonstrates this mistake

Broken implementation 7:

  Suppose the programmer wants to compare input[i] to input[i-1].
  Accordingly, they start their iteration at i=1 instead of i=0, and
  are off by one at the start of the list.

