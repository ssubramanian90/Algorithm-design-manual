'''What value is returned by the following function? Express your answer as a
function of n. Give the worst-case running time using the Big Oh notation.
function mystery(n)
        r := 0
        for i := 1 to n − 1 do
            for j := i + 1 to n do
                for k := 1 to j do
                    r := r + 1
                    return(r)'''

'''Ans:Value returend=
summation of i over 1 to n-1* summation of over i+1 to n*summation of  k over 1 to j
=summation of i over i to n-1 *summation of over i+1 to n*j
=(n^3-n)/3
