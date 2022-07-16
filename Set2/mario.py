                                # Mario 

"""
Create a program that prints the following shape with a user-inputted height: 

~/workspace/ $ mario.py
height: 5
    ## - 4 spaces / line # : 0   
   ### - 3 spaces / line # : 1 
  #### - 2 spaces / line # : 2 
 ##### - 1 space / line # : 3 
###### - 0 spaces / line # : 4 

How can we relate the variable line number to the number of the hashes there are? 
line = 0 
hashes = 2 

line = 1 
hashes = 3 

line = 4 
hashes = 6 

line + 2 = hashes 

height = 5 
line = 0 
spaces = 4 

height = 5 
line = 1 
spaces = 3 

height - line - 1 = spaces 
5 - 0 - 1 = 4 

5 - 1 - 1 = 3 



Specification: 
    1. First prompt the user for the height of the pyramid 
    2. Generate the desired half-pyramid (with the help of print and one or more loops)
    3. Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.
"""

# Code goes below here 

# Goal: print the pryamid using spaces and hashes 
