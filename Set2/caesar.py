                             # Caesar 

# Goal: Implement a program that runs the following examples: 
    
"""
~/workspace/ $ python caesar.py
key: 1
plaintext: Never gonna give you up, never gonna let you down
ciphertext: Ofwfs hpoob hjwf zpv vq, ofwfs hpoob mfu zpv epxo

~/workspace/ $ python caesar.py
key: 2
plaintext: Let's meet at the zoo!
ciphertext: Ngv'u oggv cv vjg bqq!


Cryptography: 
    Ever want to send a secret message? Cryptography is the process of converting 
    plaintext (normal English) into ciphertext (encoded text).

    The most simple of ciphers are ones where you add a value to each character. 
    For example a + 2 ➟ c! This is called a Caesar cipher. Of course, to interpret 
    the ciphertext, we would need to know what number is being added, but we’ll get back to that later!

Implementing Caesar: 
    Let’s make a program that uses a Caesar cipher to encode text like the below:
        ~/workspace/ $ python caesar.py
        key: 2
    plaintext: Let's meet at the zoo!
    ciphertext: Ngv'u oggv cv vjg bqq!

Be sure that your prompts look identical to this!
Note some important details.
    1. It seems that spaces and punctuation are not to be affected by this cipher.
    We’ll likely need to have some conditions to check for them!

    2. What is z + 2 equal? It looks like we will have to figure out a way to 
    wrap text around. It turns out that modulus operator (%) is quite useful for 
    ensuring that we stay within the alphabet. To do this, we need to think a 
    bit differently about letters.

Let’s say a is represented by the integer 0, b by 1, c by 2, … , and z by 25. 
This number is called the index! The index of b is 1!

Now, let’s use this info. c + 24 would be 26, but as the last character in the 
alphabet, z, is 25, this is problematic. Enter modulus. What is (c + 25) % 26? 
Well, this would be equivalent to (2 + 25) % 26, which is 27 % 26, which equals 
1, or a. Hazzah! We’ve wrapped around the alphabet.

However, uppercase A in ASCII (remember ASCII?) is 65 and lowercase a is 97! 😬

But note this: B - A will evaluate to 1. Why? Because ASCII! 66 - 65 = 1, 
which is the index of B! After converting letters into this index system we 
can use the modulus math to make sure things wrap around! Neat-o!

"""

# Code goes below 


# Constants
UPPER_START = 65
LOWER_START = 97
ALPHA = 26

key = int(input("Key: "))
plainText= input("Plaintext: ")

for char in plainText:
    if char.isupper():
        print(chr((ord(char) - UPPER_START + key) % ALPHA + UPPER_START), end="")
    elif char.islower():
        print(chr((ord(char) - LOWER_START + key) % ALPHA + LOWER_START), end="")
    else:
        print(char, end="")
print()

