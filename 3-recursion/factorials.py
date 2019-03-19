#!/usr/bin/python3

def recursiveFactorial(x):
    if x <= 1:
        return 1
    else:
        return x * recursiveFactorial(x - 1)

def iterativeFactorial(x):
    total = 1
    while x > 1:
        total = total * x
        x = x - 1
    return total
