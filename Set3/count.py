                                # Counting 

"""
Background: 
    To solidify for strings and indexing, we’re going to create a program that 
    asks the user for a string as input and calculates the number of words and 
    characters present in the string.

    Create a program called count.py that asks the user for a string. 
    Then, use a for loop to go through each character of the string and keep counters
    for the number of words and characters.  


Example Runs:
    $ python count.py

    Enter string: Hello world

    Number of words in the string:

    2

    Number of characters in the string:

    11

    

    $ python count.py

    Enter string: I love python

    Number of words in the string:

    3

    Number of characters in the string:

    13

"""

# Code goes below 



string = input("Enter string: ")

counter_chars = 0 
words = 0 

string = string.title() 

for char in string:
    # count number of characters 
    counter_chars += 1
    # count number of words 
    if char.isupper():
        words += 1

print(f"Number of words in string:\n{words}")
print(f"Number of characters in string:\n{counter_chars}")