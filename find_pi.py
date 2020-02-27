#!/usr/bin/env python

"""Find digits of pi to the nth digit.
n = first and only argument.
Bailey-Browein-Plouffe (BPP) formula used
to calculate digits of pi."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys
from decimal import *

# hard limit for argument n
max_n = 1000

def step(k):
    """An individual step in the summation of BPP algorithm.
    Each divisor in the BPP is labeled d_1 through d_5 from
    left to right in the order they appear in the formula."""

    mult_1 = Decimal(1) / Decimal(16)**k

    mult_2 = Decimal(4) / Decimal(8*k +1)
    mult_2 -= Decimal(2) / Decimal(8*k + 4)
    mult_2 -= Decimal(1) / Decimal(8*k + 5)
    mult_2 -= Decimal(1) / Decimal(8*k + 6)

    return mult_1 * mult_2

def sum(n):
    """Get sum of steps of BBP algorithm from 0 to n.
    Requires n to be positive integer."""
    result = Decimal(0)
    for x in range(n):
        result += step(x)
    return result
            
                
def main():
    try:
        n = (int)(sys.argv[1])
        if n < 1:
            raise ValueError
        if n > 1000:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: pi.py [n]")
        print("[n] = number of digits of pi, up to 1000.")
        sys.exit(1)

    # set precision of Decimal
    getcontext().prec = n
    result = sum(n)
    print(result)

if __name__ == "__main__":
    main()
