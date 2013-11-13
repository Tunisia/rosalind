#!/usr/bin/python

# http://www.rosalind.info/problems/fib/

def fib(n,k):
    popn = 1
    for gen in range(n):
        yield popn
        popn *= k+1
    return

n = 40
k = 5

print list(fib(n,k))