
# Lexicon 

## Goal
Create a program that compares the size of rappers' lexicons. 

#### Background 

##### Rapper's Delight 
Who’s the GOAT? Jay-Z? Kanye? Kendrick? Drake?

One way to settle (or at least contribute to) the debate of the greatest rapper 
of all time is to compare the size of the vocabulary used by each rapper. 
Some people have looked into this subject quite a bit already. We’re going to do a 
little research ourselves using Python! First, we’re going to have to look at sets.

##### Sets 
In Python, the set data structure is like a list, but where duplicates are 
ignored. Let’s say that you have a list of heights such as the one below:

```
heights = (5.5, 5.7, 5.8, 5.2, 5.5, 6.1, 6.0, 6.0)
```

In this list, 5.5 and 6.0 have duplicates. Thus when we make a set based on this list, 
the extra 5.5 and 6.0 will be omitted.

```
height_set = set(heights)
```

In this case height_set will be ```{5.2, 5.5, 5.7, 5.8, 6.0, 6.1}```. Note the curly
braces; these indicate that height_set is a set.

If I wanted to make a brand new set called grades containing the grade levels of 
CS50 Summer at HSA students, it would look like this:
```
grades = {6, 7, 8, 9, 10, 11, 12}
```

##### Dictionaries 
Dictionaries, or dicts for short, are a convenient data structure for whenever 
you desire a key-value relationship for your data. For example, think of what 
you probably know of as dictionary! There are entries for various words and 
related definitions. The word “pizza” may have the definition “a traditional 
Italian dish consisting of a yeasted flatbread typically topped with tomato 
sauce and cheese and baked in an oven.” In this case “pizza” is the key, and 
the definition is the value.

In python we can create an empty new dictionary as such:
```
words = dict()
```
or 
```
words = {}
```
Note that we have to use {} when reffering to dictionaries, just like with sets! 
However, unless you created a set using the set() function, python will actually 
interpret {} to mean a dict!

Let’s say we want to add the word “happy” to our dict of words. We could do so 
by the following:
```
words["happy"] = "feeling or showing pleasure or contentment"
```

In this case “happy” is the key, accessed not unlike how we access a particular 
element in a list (exampleList[0], exampleList[1], …). The definition “feeling or 
showing pleasure or contentment” is the value stored in that place. Thus, you 
can think of dictionaries as lists that are not limited to only having integer 
indices, but strings or data types as the key to access a particular value!

#### Your Mission
We’re going to create a program that reads rap lyrics and determines how many 
unique words different rappers use! Although the program is partially created, 
it looks like there’s more work to be done!

You’re going to tackle a few TODO’s in lexicon.py.

0. Comment TODO's 
In the main function there are a few missing comments that I need your help 
completing! Can you give me an assist? Let me know what I was doing! Eek!

1. ```fill_words(rapper)```
You need to create the function that fills and returns a dictionary of words for 
a given rapper (given as an argument). The keys for this dictionary should be 
the words (but with no duplicates!) and the values should be the number of times 
the given word is repeated by the rapper.

For example, accessing words['the'] might give you the value 15, indicating that 
the rapper used the word ‘the’ 15 times.

Important Note: Pay attention to case! A rapper using 'The' and 'the' is considered
to be two uses of the word 'the'! 


2. ```examine_rapper(rapperWords, rappername)```
One more function to create! This one takes a rappers dictionary of words used as a parameter. This function should:

- Prompt the user for a word to search in the rapper’s lexicon.
- Then, if the word is used by the rapper, then the function should print the number of times the word is used.
Otherwise, the function should inform the user that the word isn’t used. No value to return here!


##### A Few Things to note 
1. You may assume that a word will be a string with no spaces. So, names such as Ms. Jackson can be considered 
as 2 words ("Ms" and "Jackson"). 

2. You do not need to handle words that are censored

3. You should be able to allow the user the type in words with apostrophes (such as 'gon and 'yo) 

4. In the distribution code, the rapper's txt file is split into string of words using the Python split method. 
Note that split will initially treat substrings such as "Uh," (pay attention to the comma here) as strings. You should 
remove leading and trailing punctuation from these strings with a few exceptions: quoted text such as "hello" should be considered
a word (with the quotation marks), words with apostrophes (look at point 3), and words that have punctuation in between letters (e.g. R.A.G.E).
