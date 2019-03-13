#!/usr/bin/python3

def binarySearch(number_to_find, array):
    """
    binarySearch(number_to_find, array)
    given a number to find and a SORTED array of numbers, it will return the location of the number in the array or None if number not in array
    O(logN)
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == number_to_find:
            return mid
        elif guess > number_to_find:
            high = mid - 1
        else:
            low = mid + 1
    return None




import random as random

random.seed()

print("Generating random array of 10000 ints")
#probably should use a list comprehension
data_size = 10000
data_range = list() 
for i in range(data_size):
    data_range.append(random.randint(1,data_size))

print("Sorting array for binary search use")
data_range.sort()

number = 'a'
while number != 'e':
    number = input("What number are you looking for? [e]xit ")
    try:
        number = int(number)
        print("The location of that number is", binarySearch(number, data_range))
    except ValueError:
        continue