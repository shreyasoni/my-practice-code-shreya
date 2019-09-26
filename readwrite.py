'''# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str1 = fo.read(15)
print ("Read String is : ", str1)

# Close opened file
fo.close()

import os

# Rename a file from test1.txt to test2.txt
os.rename( "foo.txt", "test2.txt" )
'''
import os

# Delete file test2.txt
os.remove("test2.txt")