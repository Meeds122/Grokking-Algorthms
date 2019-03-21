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

if __name__ == "__main__":
    print("Recursive factorial of 5:", recursiveFactorial(5))
    print("Iterative factorial of 5:", iterativeFactorial(5))
