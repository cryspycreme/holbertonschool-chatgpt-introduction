#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read input from command line, compute factorial, and print result
f = factorial(int(sys.argv[1]))
print(f)