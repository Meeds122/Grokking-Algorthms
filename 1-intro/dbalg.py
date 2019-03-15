

def bsearch(dbfile, value_to_find):
    """
    bsearch(dbfile, value_to_find)
    Does a binary search of the dbfile for value_to_find
    returns a tuple consiting of (1, 2)
        1. Entry at value_to_find's index
        2. Number of operations required
    If the value is not found, return None in position 0
    """
    
    TESTING = False
    
    entry = None
    operations = 0

    dbfile_handle = open(dbfile, 'r')
    db_contents = list()
    for line in dbfile_handle.readlines():
        db_contents.append(line.strip())
    
    if TESTING == True:
        for i in range(10):
            print(db_contents[i])
    
    # Start Algorithm
    low = 0
    high = len(db_contents) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = db_contents[mid][:db_contents[mid].find(',')] # strip out the index
        operations += 1
        if guess == value_to_find:
            entry = guess
            return (entry, operations)
        elif guess > value_to_find:
            high = mid - 1
        else:
            low = mid + 1
    return (entry, operations)

def lsearch(dbfile, value_to_find):
    """
    lsearch(dbfile, value_to_find)
    Does a linear search of dbfile for value_to_find
    returns a tuple of (1, 2) where
        1. Entry at value_to_find's index
        2. Number of operations required
    If the value is not found, return Null in the 0th positon 
    """

    TESTING = False

    entry = None
    operations = 0

    dbfile_handle = open(dbfile, 'r')
    db_contents = list()
    for line in dbfile_handle.readlines():
        db_contents.append(line.strip())
    
    for i in range(len(db_contents)):
        operations += 1
        line = db_contents[i]
        if line[:line.find(',')] == value_to_find:
            entry = line
            return (entry, operations)
    
    # No value found after searching entire space
    return (entry, operations)

