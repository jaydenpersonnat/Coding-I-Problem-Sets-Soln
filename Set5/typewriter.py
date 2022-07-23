                        # TypeWriter 

# Goal: Create a word processor 

"""
Background: 
To play around with file input and output, were going to make a basic text editor 
where we ask the user for lines to write to a txt file!

Txt files are like simple word doc files that don’t contain formatting information, but only the text.

Your Mission: 
    Have the user input the name of file to write to, i.e. “file.txt”
    Keep asking the user for a line to input and write the line to the file
    Be sure to have a special string a user can type to quit the loop!
"""

# Code goes below 
filename = input("Enter name of file to write into: ")
file = open(filename, "a")

while True: 
    line = input("Enter a line, enter @ to end: ")
    if line == "@": 
        break 
    file.write(line + "\n")


