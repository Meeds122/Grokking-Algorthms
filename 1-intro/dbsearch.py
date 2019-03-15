#!/usr/bin/python3

help_string = """
The point of this program is to show a practical example of where binary search
is useful. Ensure that you have all of the required files, dbgen.py, dbalg.py, 
and dbsearch.py

These are the possible arguments
--generate=1000     | Generate a database of 1000 "people"
--database=file.db  | Where to store or retrieve the data
--binary=012-35-5547| Do a binary search for this index
--iter=012-35-5547  | Do an iterative search for this index

Required arguments:
--database
--generate OR --binary OR --iter

Example session:
./dbsearch.py --database=temp.db --generate=1000
./dbsearch.py --database=temp.db --binary=012-35-5547

Questions? Comments? tristan@customcrypto.com!

TODO:
Write dbalg.py :)
"""

# generic imports
import sys

# custom imports
import dbgen
import dbalg

def main():

    #enables in-code tests
    TESTING_MODE = False

    # remind me of the testing mode status
    if TESTING_MODE == True:
        print("DEBUGGING MODE IS ENABLED")

    if len(sys.argv) != 3: #[progname, dbarg, access/generate] What happens after this sanity check, you deserve
        print(help_string)
        exit()
    
    #Break down command line arguments
    database = None
    generate = None
    binary = None
    iterate = None
    for argument in sys.argv:
        if 'database' in argument:
            database = argument[argument.find('=')+1:] # strip the value off the equal sign
        if 'generate' in argument:
            generate = int(argument[argument.find('=')+1:])
        if 'binary' in argument:
            binary = argument[argument.find('=')+1:]
        if 'iter' in argument:
            iterate = argument[argument.find('=')+1:]
    if database == None: # No database argument. It is required. Print help and die
        print(help_string)
        exit()
    
    #testing the above
    if TESTING_MODE == True:
        print("Variable: database =", database)
        print("Variable: generate =", generate)
        print("Variable: binary =", binary)
        print("Variable: iterate =", iterate)
    
    #split into seperate sections
    if generate != None:
        print("This might take some time depending on requested size. ")
        dbgen.makeDB(database, generate)
    elif binary != None:
        print("Doing a binary search for the requested value...")
        ret = dbalg.bsearch(database, binary)
        if ret[0] == None:
            # Value not found
            print("Value not found. Took", ret[1], "operations")
        else:
            # Value found
            print(ret[0], "found in", ret[1], "operations!")
    
        
    

if __name__ == "__main__":
    main()