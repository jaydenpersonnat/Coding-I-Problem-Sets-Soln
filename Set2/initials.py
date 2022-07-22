                            # Initials 

"""
Implement a program that, given a person’s name, prints a person’s initials, per the below.

    $ python initials.py
    Name: Regulus Arcturus Black
    RAB

Background:
    To practice playing around with strings, we’re going to make a program 
    where we print initials given a name!


Your Mission: 
    Design and implement a program, initals, that, given a person name, prints
    a person's initals. 
        - Implement your program in a file called initials.py 
        - Your program should prompt a user for their name using input () to 
        obtain their name as a string 

        - You may assume that the user’s input will contain only letters 
        (uppercase and/or lowercase) plus spaces. You don’t need to worry about 
        names like Joseph Gordon-Levitt, Conan O’Brien, or David J. Malan

        - But the user’s input might be sloppy, in which case there might be 
        one or more spaces at the start and/or end of the user’s input or 
        even multiple spaces in a row.

        - Your program should print the user’s initials 
        (i.e., the first letter of each word in their name) with no spaces or 
        periods, followed by a newline (\n).
            -  Note that print() adds a newline by default! To change this, use 
            something like print("Hello!", end=""), signifying that you want to 
            end the line with no special character ("").

Example Runs: 
    $ python initials.py
    Name: Jayden Personnat
    JP 

    $ python initals.py 
    Name:  robert      thomas bowden 
    RTB  

"""

# Code goes below here 
# name = input("Name: ")

# # Capitalize first character in every word  
# name = name.title() 

# for letter in name:
#     if letter.isupper():
#         print(letter, end = "")

# print()

name = input("Name: ")

name_lst = name.split()

for element in name_lst:
    print(element[0].upper(), end = "")

print()


