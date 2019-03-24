import sys,datetime,array
from sqlUtils import *

# Ensure the correct number of arguments
#
if len(sys.argv) != 3:
    print("ERROR(1)")
    print("Usage: testarg.py <config file> <action taken>")
    print("       There were ",len(sys.argv)-1, "arguments")
    sys.exit(1)

# Set the variables
#
configFile=sys.argv[1]
takeAction=sys.argv[2]

# Is the action valid?
#
if takeAction not in ['validate','execute']:
    print("ERROR(3)")
    print(takeAction," is not a valid action")
    print("Valid Action: validate, execute")
    sys.exit(3)

# What time is it?
#
now = datetime.datetime.now()

# Header for log file
#
print ("---------------------------------------------------")
print ("SQL file executioner")
print ("Called: ",str(now),"\n")
print ("Configuration file: ",configFile)
print ("Action to take:     ",takeAction)
print ("---------------------------------------------------")

# If the configuration file is there, open it
#   -- my first use of exception handling in Python (woot!)
#
try:
    cfh = open(configFile,'r')
except FileNotFoundError:
    print("ERROR(2)")
    print (configFile," is not here!")
    sys.exit(2)

# Start reading the config file
#
row = cfh.readlines()

# Create lists of databases and scripts
#
db = []
script = []

# Set the sequence number to -1 so I can increment it
# before loading the lists
#
seq = -1
for line in row:
    seq+=1
    info = line.split('|')
    db.append(info[0])
    script.append(info[1])

print("The number of scripts to be "+takeAction+"d is ",seq+1)

# Loop through the lists of databases and scripts and take Action
#
for i in range(seq+1):
    if takeAction == 'validate':
        validateSQL(db[i],script[i])
    elif takeAction == 'execute':
        executeSQL(db[i],script[i])
    else:
        print ("This should never happen")

# Cleanup, cleanup, everybody everywhere
#
cfh.close()
