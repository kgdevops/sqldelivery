import sys,re

myplat = sys.platform
print (myplat)
windows = myplat.count('w') 
linux = myplat.count('l')
print (windows)
print (linux)
if (linux > 0):
	print ("This is Linux!")

if (windows > 0):
	print ("This is Windows!")

