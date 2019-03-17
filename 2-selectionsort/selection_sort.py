#!/usr/bin/python3

def selectionSort(array):
    """
    selectionSort(array)
        Returns a copy of the array in sorted order
        memory complexity O(n)
        time complexity O(n^2)
    """
    working_array = array.copy()
    N = len(working_array)

    return_array = list()

    while N > 0:
        # Reset lowest again
        lowest = working_array[0]
        lowest_loc = 0
        # Search array for smallest item
        for i in range(N):
            if lowest > working_array[i]:
                lowest = working_array[i]
                lowest_loc = i
        # Found lowest, decrement N, appened lowest to return_array, and del lowest from working array 
        N = N - 1
        return_array.append(lowest)
        del working_array[lowest_loc]
    #when N is 0, there are no elements left to check, return 
    return return_array


def main():
    #generate 10 random numbers
    import random as random

    array = list()
    for i in range(10):
        array.append(random.randint(0,10))
    
    print("Initial array:", array)
    new_array = selectionSort(array)
    print("Sorted array:", new_array)

if __name__ == "__main__":
    main()

