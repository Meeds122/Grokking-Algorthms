

def bsearch(dbfile, value_to_find):
    """
    bsearch(dbfile, value_to_find)
    returns a tuple consiting of (1, 2)
        1. Entry at value_to_find's index
        2. Number of operations required
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