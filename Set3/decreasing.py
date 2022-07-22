                            # Decreasing 

# Goal: Determine if a list of numbers is in decreasing order. 

"""
Background: This problem deals with lists of numbers. 
            Remember, a list can have no elements: []. 
            One element: ["cat"] 
            Five elements: [1, 2, 3, 4, 5]
            or any other number of elements. Say I create a variable that refers
            to a list, like this: 
                my_list = ["a", "b", "c"]

            This line of code says I have a variable my_list and its value 
            is set to the list ["a", "b", "c"].

            One thing we can do with a list is get elements out of it using 
            their index. The first element in a list is at index 0, the next 
            is at index 1, and so on.

            Another thing we can do with a list is append to it, or add something 
            to its end. If we have a list like this:
                numbers = [1, 2, 3]
            And then we do this: 
                numbers.append(4)

            Then numbers now has the value [1, 2, 3, 4]. I’ve appended 4 to the list.

            If I run the following code: 
                pets = []
                pets.append("cat")
                pets.append("dog")
                pets.append("fish")
            
            Then at the end pets has the value ["cat", "dog", "fish"].

Your Mission: 
    Write a function that takes a list of numbers as an argument and returns 
    True if the list is in decreasing order and False otherwise.

    Hint: a list is in decreasing order if it is empty or if each of its 
    elements besides the last is greater than or equal to the next element.


Suggested Steps: 
    1. Detect if lists of 0 or 1 elements are decreasing 
    2. Add code to detect if lists of 2 elements are decreasing 
    3. Add code to detect if lists of 3 or 4 elements are decreasing 
    4. Use a loop instead to detect if lists of at least 1 element are decreasing 

Bonus: 
    Change your function to detect if a list first decreases and then increases 
    (but does not decrease again).

"""

# Code goes below 
import sys 

# Using while loop 
def decreasing_one(lst):
    i = 0 
    
    if len(lst) == 0 or len(lst) == 1:
        return True
    else:
        while i < len(lst) - 1:
            if lst[i] >= lst[i + 1]:
                i += 1
            else:
                return False 

    return True

# Using for loop 
def decreasing_two(lst):
    cmp = sys.maxsize
    if len(lst) == 0:
        return True
    else:
        for element in lst:
            if element <= cmp:
                cmp = element 
            else:
                return False
    return True


# Using built-in functions 
def decreasing_three(lst):
    if lst == sorted(lst, reverse = True):
        return True
    
    return False


# Tests below 


decreasing_lst = [[], [7], [-5, -7, -8, -9, -10, -11, -13], [4, 4, 4], [9, 8, 7, 5, 5, 5, 4, 4, -2]]

nondecreasing_lst = [[2, 1, 2], [9, 8, 7, 6, 7, 5, 5, 5, 5, 4, 3]]

for lst in decreasing_lst: 
    assert(decreasing_one(lst))
    assert(decreasing_two(lst))
    assert(decreasing_three(lst))

for lst in nondecreasing_lst: 
    assert(not decreasing_one(lst))
    assert(not decreasing_two(lst))
    assert(not decreasing_three(lst))

print("All Tests Passed!")