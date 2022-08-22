In this assignment, you are going to write the function to determine
if there is a "peak" at a given index of a list.  As we discussed in the videos
leading up to this assignment, we will parameterize this over "w" which is the
width of the region in which a peak has to be largest.  In particular, we will say
that

Given some index i, it is a peak within width W if
   1. i is at least W (there are enough points to the left)
   2. i is less than len(data) - W (there are enough points to the right)
   3. data[i] is greater than the W values of data to its left
        (left meaning smaller indices, i-1, i-2, … i-W)
   4. data[i] is greater than or equal to the W values of data to the right
      (right meaning greater indices i+1, i+2, … i+W)

Start by opening up count_laps.py.  You will see that we have started you off with
three things:
  (1) A "placeholder" for is_peak_at.  At the moment, this function just returns True.
      You are going to replace that with the code for your is_peak_at function.
  (2) The code for count_laps from the video, which uses your is_peak_at function.
  (3) Some testing code (under if __name__ == "__main__").

Before you dive into writing is_peak_at, we want to take a moment to help you look
at the testing code that we set up for you.  Notice the first two non-comment lines:

    data0 = [160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162]
    peaksat0 = [2, 8]

Here, we are writing down the small example from one of the videos, and the
answer to it (for w=2): it has peaks at indicies 2 and 8 (also note that this answer
is sufficient to give us the answer for count_laps---which would be the length
of this list).

We do this for some other test cases, then put them all in a list of tuples:

    w2_data = [(data0, peaksat0), (data1, peaksat1), (data2, peaksat2),
               (data3, peaksat3), (data4, peaksat4), (data5, peaksat5),
               (data6, peaksat6)]

Notice that this combines together two concepts you have seen separately:
lists and tuples.  As with many things in programming, we can combine them
and each still follows their same rules.  We have a list where each item
is a tuple with the data and the answer.

Next, you will see that we call a function where we have abstracted
out most of the testing logic:

    all_right = tests_for_hr_data(w2_data, 2)

Testing is also a place where we want to use good abstraction!  
If you take a look inside of that function, you will see that it
iterates over data_and_answers (which is the list of tuples
that contains (data,answer)).  For each of these items,
it prints out a message about what it is testing, then iterates
over the data, calling your is_peak_at function.
It checks the answer of your is_peak_at based on what was
passed in from the tuple.   After checking each of these,
it calls count_laps to see if that gives the right answer.

Now that we have shown you the test setup we have provided, go
ahead and write the is_peak_at function.

Once you have written is_peak_at, be sure to run the tests we gave you
(C-u C-c C-c).  We'll briefly note that if you were developing this
program on your own, you would want to write is_peak_at first, test
it, and then write count_laps after you are confident in it.  Since we
developed count_laps together in the videos, we have gone ahead and
included the code for it in what we provided to you.


Now is a good time to stop and assess your test cases: how confident
do they make you in the code that you wrote?  Take a moment to think
about this before proceeding.

For me, the answer is "I am fairly confident when w=2, but not
confident when w has any other value, as I only tested with w=2".

Fortunately, we abstracted out our testing code into
tests_for_hr_data, so we can just re-use that to test with some other
values of w.  (We will note that if we had not abstracted that code
out into its own function, doing so now would be a good idea!)

We have already setup some data and answers for you for w=1 and w=4.
If you look into the testing code, you will see

    #w1_data = w2_data[:]
    #w1_data[1] = (data1, [2, 6, 8])
    #w1_data[5] = (data5, [1])
    #all_right = tests_for_hr_data(w1_data, 1) and all_right
    #w4_data = [(data0, []), (data1, []), (data2, [4]),
    #           (data3, []), (data4, []), (data5, []),
    #           (data6, [])]
    #all_right = tests_for_hr_data(w4_data, 4) and all_right
    
Just uncomment those lines  and run your code and compare
it to output.txt (C-c d in Emacs).

Once everything is good, git commit, git push, and grade!
