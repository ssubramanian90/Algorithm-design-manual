'''Consider the following algorithm to find the minimum element in an array
of numbers A[0,...,n].

One extra variable tmp is allocated to hold the current minimum value.
Start from A[0]; ”tmp” is compared against A[1], A[2], . . . , A[N]
in order. When A[i] < tmp, tmp = A[i]. What is the expected number of times
that the assignment operation tmp = A[i] is performed?'''

'''Ans:


The expected number of times the assignment to tmp
is made is the sum of the probabilities that the nth element is the minimum.

If we assume the minimum is distributed uniformly in out sequence,
then the probability  og\\f getting minimum number is 1/n.

Expected time will be E(n) = E(n-1)+1/n
and E(1)=0
Thus, the complete expected time will be:
summation of 1/n over complete n.

thus, sum= ln n
'''

