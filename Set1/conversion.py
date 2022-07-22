                          # Conversion 

# Goal: Convert user inputted hours and minutes into just minutes! Then, convert them into just hours. 

"""
Background: 
    Convert user inputted hours and minutes into just minutes. Then, covert them into just hours.

Your Mission: 
    Problem 0: 
        Take in input from the user for hours and minutes. Then, 
        we’ll use an integer to represent to total number of minutes 
        the user has entered after converting hours into minutes! 
        Lastly, we’ll print this value to the screen!

    Problem 1: 
       Take in input from the user for hours and minutes. Then, we want to 
       create a float for time in hours (where the digits to the left of the 
       decimal represent whole hours and to the right, fractions of an hour). 
       In other words, were converting all hours and minutes into total hours. 
       Lastly, we’ll print this value to the screen!
"""


# Problem 0 
print("Problem 0")

# Code 

# Get user input for hours and minutes 
hrs = input("Hours: ")
minutes = input("Minutes: ")

# Calculate total minutes and print 
total_min = int(hrs) * 60 + int(minutes)

print(f"Minutes: {total_min}")

print()

# Problem 1 
print("Problem 1")
# Code 

# Get user input for hours and minutes 
hrs = input("Hours: ")
minutes = input("Minutes: ")

# Calculate total hours and print 
total_hrs = int(hrs) + int(minutes) / 60

print(f"Hours: {total_hrs}")

