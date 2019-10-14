# Reading Files

#importing argv function from sys module
from sys import argv

#defining Variables as arguments
script, filename =argv

#opening filename provided as argv
txt= open(filename)


print(f"Here's your file {filename}:")
#reading and printing text file
print(txt.read())
txt.close()
print("Type the filename again:")
#getting file name as input
again_filename= input("> ")

txt_again=open(again_filename)
print(txt_again.read())

txt.close()
