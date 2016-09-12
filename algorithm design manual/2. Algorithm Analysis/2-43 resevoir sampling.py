what kind of procedure should the person use if he wants to give all the numbers an equal chance, 1/n?
First of all, he has to choose the last number with probability 1/n, since the last number wins if and only if he decides to chooses the last number.

Now what about the second-to-last number?
In order for it to win, he has to decide to choose on the (n-1)th step, and then also decide to not chooses the nth number.
This happens with probability  pn−1*(n-1)/n, where  pn−1  is the probability that he chooses the (n-1)th number;
and (n-1)/n is the probability he does not choose the nth number.

Solving for pn−1,

pn−1*(n-1)/n = 1/n

Therefore, pn-1=1/(n-1)


Another way of thinking about it is:
Now that our reservoir is full, we may or may not add this (k+1)th element to the reservoir. The probability that we add it to the reservoir is:

The number of ways of choosing k elements from k+1 elements such that the (k+1)th element is in this selected k / The total number of ways of choosing k elements from k+1 elements

This is equal to:
1 - (The number of ways of choosing k elements from k+1 elements such that the (k+1)th element is not in this selected k / The number of ways of choosing k elements from k+1 elements) 

The denominator of the term in the above expression is simply (k+1) choose k, which is (k+1), and the numerator is simply 1,
since there is only 1 way to choose k elements from (k+1) elements without including the (k+1)th element.

Thus, the probability we add the (k+1)th element to the reservoir is:

1 - (1 / (k+1)) = (k + 1 - 1) / (k+1) = k / (k+1)

By similar logic, the probability that we add the (k+2)th element to the reservoir that can hold a maximum of k elements is:

k / (k+2)

and so on, where the probability of adding the nth element to this reservoir (where n >= (k+1)) is:

k / n

As 'n' increases more and more, (k / n) gets smaller and smaller for a fixed 'k' (reservoir size). Thus, the larger 'n' is, the smaller (k / n) is.



Weighted Reservoir Sampling Variation


How would you sample from a weighted distribution where each element has a given weight associated with it in the stream?



As you process the stream, assign each item a "key". For each item in the stream , let  be the item's "key",
let  be the weight of that item and let  be a random number between 0 and 1. The "key" () is a random number to the
nth root where n is weight of that item in the stream:

ki=ui^(1/wi)

Now, simply keep the top n elements ordered by their keys (), where n is the size of your sample. Easy.

Explanation-
For  non-weighted elements (ie: weight = 1),

wi is always 1, so the key is simply a random number and this algorithm degrades into the simple algorithm mentioned above.

The probability of choosing i over j is the probability that ki > kj. ki can have any value from 0 - 1.

However, it is more likely to be closer to 1 the higher w is.

We can see what the distribution of this looks like when comparing to a weight 1 element by integrating k over all values of
random numbers from 0 - 1. You get something like this:
        


integration of ki over 0 to 1= wi/(1+wi)

Thus, higher the weights, higher the keys





Reservoir Sampling-

The reservoir sampling algorithm outputs a sample of N lines from a file of undetermined size. It does so in a single pass, using memory proportional to N.

Let's say  we are to sample 5 lines randomly from a 6-line file. So,i=the line number of the input, and N=the size of sample desired. 
import sys
import random

def reservoirSample(stream):
 
sample=[]

for i, line in enumerate(stream):
        if i <N:#For the first 5 lines (where i < = N), our sample fills entirely. 
                sample.append(line)
        elif i>= N and random.random()<N/float(i+1) :# Reservoir sampling begins- the 6th line will have 5/6th probability 
                replace= random.randint(0,  len(sample)-1)# Thus, the6th line will rpelace one of the existing lines with probability of 5/6*1/5= 1/6
                sample[replace]=line
                
for line in sample:
        sys.stdout.write(line)

In general, as more lines are seen, the chance that any additional line is chosen for the sample falls;
but the chance that any previously chosen line could be replaced grows. These two balance such that the probability for any given line of input to be sampled is identical.

