For this assignment, you are going to be writing three functions:

 1.  find_moving_average(data, n)
     which returns the n-element moving average of the data.
     Recall from the videos that this answer will also be a list,
     and will be shorter than the input list.
     Note that you may assume n is positive (greater than, and
     not equal to 0) as you can only take the averge of a positive
     number of data points.

 2.  get_only_peaks(data, w)
     which returns only the peaks of the data.  This function
     should use is_peak_at from the previous assignment.  To make
     use of that, we are going to symlink the file from the other
     assignment into this directory:
        ln -s ../10_hr_peaks/count_laps.py ./
     Then in your python code, an import statement like this:
        from count_laps import is_peak_at
     will let you use is_peak at. 
     Note that this function should return a list which is just the
     values of the peaks.  For example, given
      [160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162]
     and w = 2, this function would return
        [162, 164]
     We will also briefly note that in "normal" programming you would just put your
     various files for one project in the same directory and not need to symlink
     them---we are just doing this because things are divided between assignments
     here. 

 3.  moving_average_of_peaks(data, n, w)
     This function should give you the n-unit moving average of
     only the peaks of the data, using w as the "width" of our peak-finding
     algorithm.  Note that this function should be quite short (2--3 lines long)
     as you have already done all the work in (1) and (2).


If you open moving_avg.py, you will find that we have put in placeholders for
these three functions, as well as the import statement to use is_peak_at.
We have also put a little bit of testing code at the bottom.  If you evaluate
that buffer (C-u C-c C-c), you will see that the code fails many test cases
(because it is not implemented yet).    Implement each function one at a time,
and test it before proceeding to the next (write find_moving_average,
test find_moving_average, write get_only_peaks, test get_only_peaks,
write moving_average_of_peaks, test moving_average_of_peaks).
  
