There are 25 horses. At most, 5 horses can race together at a time.
You must determine the fastest, second fastest, and third fastest horses.
Find the minimum number of races in which this can be done.



Let’s say that we have 5 races of 5 horses each, so each row in the table above
represents a race. So, “X1 X2 X3 X4 X5 ” represents a race, and “X6 X7 X8 X9 X10”
represents another race, etc. In each row, the fastest horses are listed in
descending order, from the fastest (extreme left) to the slowest (extreme right). The fastest horses in each race are the ones on the left –
so in the first race X1 was the fastest and X5 was the slowest.
In the second race X6 was the fastest, X7 was the second fastest and so on.


what if the 5 fastest horses just happened to be in the first race –
so X1 X2 X3 X4 X5 are the fastest horses. X1, X6, X11, X16, and X21 are all
the fastest horses in their individual groups, but there could be one group
that just happened to have all of the fastest horses.
Remember we haven’t compared all the horses to each other since we can only
run 5 horses in a race, so that is still a possibility.
This is very important to understand in this problem.

we can eliminate the slowest 2 horses in each group since those horses are
definitely not in the top 3.

we can race those 5 horses against each other (X1, X6, X11, X16, and X21)
and that would be the 6th race. Let’s say that the 3 fastest in that group are
X1, X6, and X11 –
automatically we can eliminate X16 and X21 since those 2 are definitely not in
the top 3.

we can safely eliminate X8. We can also eliminate X12 and X13 since
X11 was the 3rd fastest in the group leaders, and X12 and X13 were slower than
X11.

So, all together we can eliminate these horses after the 6th race:
        X17 X18 X22 X23 X16 X21, X12, X13, X8 and X1.

It takes 7 races to find the top 3 horses in this problem.




