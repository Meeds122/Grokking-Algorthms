#!/usr/bin/python3

def recursiveSum(arr):
    """
    This function will recursively sum all of the elements of an array including any subarrays ad infinitum
    sums integers and floats
    will recursively search lists and tuples
    """
    total = 0.0
    for element in arr: # loop naturally ends after exhausting all elements
        if type(element) == list or type(element) == tuple:
            total += recursiveSum(element)
        elif type(element) == int or type(element) == float:
            total += element
        else:
            print("[!] Skipping", str(element))
    return total


if __name__ == "__main__":
    a = [1, 2, [3, 4], 5, (1, 2, [3, 4, (5,)])]
    print("The following value should be 30")
    print(recursiveSum(a))