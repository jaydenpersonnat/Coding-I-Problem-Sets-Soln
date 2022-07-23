"""
Rap Lexicon
Spencer L Tiberi
SCA 1, July 2018
"""

# All the info for this problem set can be found in lexicon.md! 

import os
from string import punctuation 

def main():
    rappertexts = []

    # Directory where lyrics are stored
    directory = os.fsencode("lyrics/")

    # Fill list of rappers with txt filenames
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith(".txt"):
            rappertexts.append(filename)
            continue
        else:
            continue

    # Create a dict that has a rapper name and then set of words
    rappers = dict()

    # Fill dict with rapper names as keys and dicts of words as values then print name, wordcount, etc. to screen
    for rappertext in rappertexts:
        words = fill_words(rappertext)
        # Create rapper name from filefame (remove .txt and capitalize)
        rapper_name = rappertext[:-4].capitalize()

        # Add key-value pair to rappers dictionary 
        # key: rapper_name, value : dictionaries includding words and # of          # times they occur 
        rappers[rapper_name] = words

        # Create a dotted line for formating based on length of the rapper's name
        line = "." * (40 - len(rapper_name))

        print("%s%s\n\tWord Count: %s\n\tLargest Word: %s\n\tMost Used Word: %s" % \
              (rapper_name, line, len(rappers[rapper_name]), \
              max(rappers[rapper_name], key=len), max(rappers[rapper_name], key=rappers[rapper_name].get)))

    # repeatedly ask user to examine rapper 
    # if user types quit, program ends
    # alert user with error if rapper is not in lyrics 
    while True:
        rapper = input("Choose a rapper to further examine (or type 'quit'): ")

        if rapper == 'quit':
            break
        elif rapper in rappers:
            examine_rapper(rappers[rapper], rapper)
        else:
            print("Invalid rapper!")

# Fills and returns a dict cotaining a set of words as keys and use count as values for a given rapper file
def fill_words(rapper):

    words = []

    words_dict = {}
    # Opens the file for each rapper
    with open("lyrics/" + rapper, "r") as f:
        words = f.read().split()
    
    words = [word.lower().strip("!#$%&()+,-./:;<=>?@[\]^_`{|}~") for word in words]

        # TODO: Create a dictionary of words
    for word in set(words): 
        words_dict[word] = words.count(word)
    return words_dict

# Examines the number of times the rapper uses a user-inputted word and prints results to the screen
def examine_rapper(rapperWords, rappername):
    word = input("Enter a word: ")
    if word.lower() in rapperWords: 
        print(f"{rappername} used {word} {rapperWords[word.lower()]} times.")
        return rapperWords[word.lower()]
    else: 
        print(f"{rappername} did not use {word}.")
        return None 

if __name__ == '__main__':
    main()
