                                # Zip 

"""
Write a function that takes a list of integers such as 
[1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7] and returns a dictionary of each integer and 
the number of times it occurs in the list {1:1, 2:2, 3:1, 4:1, 5:3, 6:2, 7:1}. 

Hint: define a separate function called zip that returns a dictionary, and a 
print it out using the main function.

Example Run: 
    lst = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7]

    print(zip(lst))
    
    python zip.py 
    {1:1, 2:2, 3:1, 4:1, 5:3, 6:2, 7:1}

Bonus: Unzip 
Write a function that takes a dictionary of each integer and the number of times 
it occurs in the list such as {1:1, 2:2, 3:1, 4:1, 5:3, 6:2, 7:1} and returns a 
list of integers [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7]. 

"""

# Code goes below 
def zip(lst):
    dict = {}
    visited = [] 
    for element in lst:
        if element not in visited:
            dict[element] = lst.count(element)
            visited.append(element)
    return dict 

def unzip(dict): 
    lst = []
    for key in dict:
        for i in range(dict[key]):
            lst.append(key)

    return lst

