                        # Review 

# Goal: Create a program that uses a for loop, prints the numbers 1 through 15, 
# line by line, with a string noting if the integer is odd or even 

"""
Goal: Create a program that uses a for loop, prints the numbers 1 through 15, 
line by line, with a string noting if the integer is odd or even


Example Run: 
python review.py 

1 odd
2 even
3 odd
4 even
5 odd
6 even
7 odd
8 even
9 odd
10 even
11 odd
12 even
13 odd
14 even
15 odd

"""

# Code goes below 
for i in range(1, 16): 
    if i % 2 != 0: 
        print(f"{i} odd")
    else:
        print(f"{i} even")