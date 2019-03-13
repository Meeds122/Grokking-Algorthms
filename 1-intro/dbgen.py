#!/usr/bin/python3

import random

def makeDB(db_file, quantity):
    """
    This function generates a sorted quantity length list of random data in csv format and saves it to db_file
    """
    
    #enables in-code tests
    TESTING_MODE = False

    LETTERS = 'abcdefghijklmnopqrstuvwxyz' # list of letters for the name generator
    random.seed() # Seeds the random number generator by using the system time by default

    file_handle = open(db_file, 'w')

    to_write = [] # elements to write to the database. Must be stored in memory first to sort effiently

    # build data array
    for i in range(quantity):
        # build index
        # this is very slow process but I'm being lazy and not optimizing the function calls due to zero padding issues.
        # this also seems like a great canidate to include multiprocessing calls. It should be safe as long as to_write gets locked
        # some ideas no o.O ?
        index = ''
        index += str(random.randint(0,9))
        index += str(random.randint(0,9))
        index += str(random.randint(0,9))
        index += '-'
        index += str(random.randint(0,9))
        index += str(random.randint(0,9))
        index += '-'
        index += str(random.randint(0,9))
        index += str(random.randint(0,9))
        index += str(random.randint(0,9))
        index += str(random.randint(0,9))

        # Simulate first and last name using random characters
        name = ''.join(random.choices(LETTERS, k=random.randint(5,10))) + ' ' + ''.join(random.choices(LETTERS, k=random.randint(5,10))) 

        #generate CSV entry
        to_write.append(str(index) + ',' + str(name))

    # sort the items in to_write
    def keyFunc(string):
        return string[:string.find(',')]
    to_write.sort(key=keyFunc)

    if TESTING_MODE == True:
        print(to_write)

    # write to_write to file
    for item in to_write:
        file_handle.write(item + '\n')


    file_handle.close()