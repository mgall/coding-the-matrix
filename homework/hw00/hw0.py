# Please fill out this stencil and submit using the provided submission script.
from functools import reduce




## Problem 1
def myFilter(L, num): 
    return [l for l in L if l%num != 0]

## Problem 2
def myLists(L): 
    return [ list(range(1,i+1)) for i in L]

## Problem 3
def myFunctionComposition(f, g):
    return { k:g[f[k]] for k in f.keys() }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j 
complex_addition_b = 0 + 1j
complex_addition_c = -1 + .001j
complex_addition_d = .001 + 9j

## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L): 
    return reduce(lambda x,y:x+y, L, 0)

## Problem 7
def myProduct(L):
    if not L: return 0
    else : return reduce(lambda x,y:x*y, L, 1)



## Problem 8
def myMin(L):
    return reduce(lambda x,y: x if x < y else y, L, L[0])


## Problem 9
def myConcat(L): 
    return "".join(L)


## Problem 10
def myUnion(L): 
    return reduce(lambda a,b: a|b, L, set())




