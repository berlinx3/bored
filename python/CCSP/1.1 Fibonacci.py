
"""
Resursion
Infinite 
"""
def fib1(n):
    return fib1(n - 1) + fib1(n - 2)

"""
Recursion with base case
"""
def fib2(n):
    if n < 2:  #base case
        return n
    return fib2(n - 2) + fib2(n - 1)

"""
Memoization
"""
memo = {0:0, 1:1}
def fib3(n):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

"""
Automatic Memoization
"""
from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n):
    if n <2: 
        return n
    return fib4(n - 2) + fib4(n - 1)

"""
Iteration
***Any problem that can be solved recursively can also be solve iteratively
"""
def fib5(n):
    if n == 0:
        return n
    last = 0
    next = 1

    for _ in range(1, n):
        last, next = next, last + next

    return next


"""
Generator
"""
from typing import Generator
def fib6(n):
    yield 0
    if n > 0:
        yield 1
    
    last = 0
    next = 1

    for _ in range(1,n):
        last, next = next, last + next
        yield next


def testrun(fn):
    t = timeit.timeit(f"{fn}(50)", setup=f"from __main__ import {fn}", number=100)
    print(f"{fn} : {t:.10f}")

import timeit   
if __name__ == "__main__":
    #print(fib1(5))
    #print(fib2(5))
    testrun("fib3")
    testrun("fib4")
    testrun("fib5")
    # for i in fib6(50):
    #     print(i)