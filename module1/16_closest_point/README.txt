Previously, we worked through the first 4 steps for the "closest point" problem---given
a set S and a point P, find the member of S which is closest to P. Now you
are ready to turn this into code, though as we will describe below, we are
going to change the problem slightly (so you will want to work back through
Steps 1--4).

You already have a Point class from a previous assignment, which you will use for
this assignment.  As you have done before, you will want to symlink point.py
from assignment 14:

  ln -s ../14_point/point.py  ./

You will also need to import the Point class, as you did in the "circle" assignment.

In a file called cp.py, you should write the function:

closestPoint(s,p)

where
  s is a set of Points
and
  p is a Point
such that this function returns the subset of points from s closest to p.

Note that this is slightly different than what we did in the first four steps,
where we returned one single point.  However, as there may be more than one point
at the same distance from p, it makes sense to return a set.
For example, if

s = { (3,4), (-3, -4), (5, 6), (12,8) }

and
p = (0,0)

then both (3,4) and (-3, -4) are the same distance (5) from p.  So this function would return

 { (3,4), (-3, -4) }

Also note that by returning a set, we can say that when the input set (s) is empty,
you can just return the empty set.

You should also write test cases for your function to convince yourself
that it is correct.