import textwrap,sys

def validateSQL(db,script):
    cscript = script.strip()
    print (textwrap.fill("Does the database "+db+" exist?"))
    # If the SQL script is there, open it
    #   -- my second use of exception handling in Python (woot!)
    #
    try:
        cfh = open(cscript,'r')
    except FileNotFoundError:
        print("ERROR(2)")
        print (cscript," is not here!")
        sys.exit(2)
    # File must be here
    #
    print (textwrap.fill("The file "+cscript+" does exist!"))

def executeSQL(db,script):
    cscript = script.strip()
    print ("sqlplus dbuser/dbpassword@"+db+" @"+cscript)
