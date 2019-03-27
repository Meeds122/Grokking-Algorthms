#!/usr/bin/python3

def quickSort(arr):
    working_array = arr.copy()
    working_array_length = len(working_array)
    if working_array_length <= 1:
        # Empty element or single element case
        return working_array
    elif working_array_length == 2:
        # only 2 elements case
        if working_array[0] <= working_array[1]:
            # already sorted
            return working_array
        else:
            # sort array
            return [working_array[1], working_array[0]]
    else:
        # more than 2 elements
        # select the last element as the pivot
        pivot = [working_array[working_array_length - 1]]
        less_array = []
        greater_array = []
        for i in range(working_array_length - 1):
            if working_array[i] > pivot[0]:
                greater_array.append(working_array[i])
            if working_array[i] <= pivot[0]:
                less_array.append(working_array[i])
        return quickSort(less_array) + pivot + quickSort(greater_array)

def testing():
    import random
    test_array = []
    for i in range(random.randint(1,20)):
        test_array.append(random.randint(1,30))
    print("Unsorted array:")
    print(test_array)
    print("Sorted array:")
    print(quickSort(test_array))

testing()