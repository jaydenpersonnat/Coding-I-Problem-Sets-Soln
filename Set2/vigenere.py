                                # Vigenere

"""
Implement a program that runs like the following examples:
    ~/workspace/ $ python vigenere.py
    key: ABC
    plaintext: HELLO
    ciphertext: HFNLP

    ~/workspace/ $ python vigenere.py
    key: ABC
    plaintext: Hello, world!
    ciphertext: Hfnlp, yosnd!

The Vigenere Cypher 
    So the Caesar cipher isn’t all that secure. There are only going to be 
    26 different possible keys a hacker needs to try 
    (‘a’ doesn’t even change the message!). We have to be able to do better. 
    One slightly more secure cipher is the Vigenére cipher!

    Vigenère’s cipher improves upon Caesar’s cipher by encrypting messages 
    using a sequence of keys (or, put another way, a keyword). 
    In other words, if p is some plaintext and k is a keyword 
    (i.e., an alphbetical string, whereby A represents 0, B represents 1, 
    C represents 2, …, and Z represents 25), then each letter, 
    ci, in the ciphertext, c, is computed as:
        ci = (pi + kj) % 26

    Note this cipher’s use of kj as opposed to just k. And if k is shorter 
    than p, then the letters in k must be reused cyclically as many times as 
    it takes to encrypt p.

    In other words, if Vigenère himself wanted to say HELLO to someone 
    confidentially, using a keyword of, say, ABC, he would encrypt the H 
    with a key of 0 (i.e., A), the E with a key of 1 (i.e., B), and the 
    first L with a key of 2 (i.e., C), at which point he’d be out of letters 
    in the keyword, and so he’d reuse (part of) it to encrypt the second L 
    with a key of 0 (i.e., A) again, and the O with a key of 1 (i.e., B) again. 
    And so he’d write HELLO as HFNLP.

    Encrypting HELLO with a keyword of ABC (reused cyclically as ABCAB) yields HFNLP.
    
        plaintext	H	E	L	L	O
        key	        A	B	C	A	B
        key value	0	1	2	0	1
        ciphertext	H	F	N	L	P

Specification:
    Design and implement a program that encrypts messages using Vigenère’s cipher.

        Implement your program in a file called vigenere.py in a directory called vigenere.
        Your program must accept a single command-line argument: a keyword, k, 
        composed entirely of alphabetical characters.

        If your program is executed without any command-line arguments, 
        with more than one command-line argument, or with one command-line argument 
        that contains any non-alphabetical character, 
        your program should print an error (of your choice) and exit 
        immediately, with main returning 1 (thereby signifying an error).

        Otherwise, your program must proceed to prompt the user for a string of 
        plaintext, p, (as by a prompt for plaintext:) which it must then 
        encrypt according to Vigenère’s cipher with k, ultimately printing 
        the result (prepended with ciphertext: and ending with a newline) and 
        exiting, with main returning 0.

        With respect to the characters in k, you must treat A and a as 0, B and 
        b as 1, … , and Z and z as 25.

        Your program must only apply Vigenère’s cipher to a character in p if 
        that character is a letter. All other characters 
        (numbers, symbols, spaces, punctuation marks, etc.) must be outputted 
        unchanged. Moreover, if your code is about to apply the jth character of 
        k to the ith character of p, but the latter proves to be a 
        non-alphabetical character, you must wait to apply that jth character 
        of k to the next alphabetical character in p; you must not yet 
        advance to the next character in k.

        Your program must preserve the case of each letter in p.
"""

# Code goes below 
UPPER_START = 65
LOWER_START = 97
ALPHA = 26

key = input("key: ").upper()
plaintext = input("plaintext: ")

# Converts char to number such that A - 0, B - 1, ..., Z - 25
def convert_to_num(char): 
    if char.isupper():
        return ord(char) - UPPER_START
    else:
       return ord(char) - LOWER_START 

# Inverse of convert_to_num and preserves case  
def convert_to_char(char, num):
    if char.isupper():
        return chr(ci + UPPER_START)
    else:
        return chr(ci + LOWER_START)

# Set index to keep track of position in key 
index = 0 

# loop through each character in plaintext and convert to ciphertext 
for char in plaintext: 
    if not char.isupper() and not char.islower(): 
        print(char, end= "")
    else:
        ci = (convert_to_num(char) + convert_to_num(key[index % len(key)])) % ALPHA 
        print(convert_to_char(char, ci), end = "")
        index += 1 

print()



    

