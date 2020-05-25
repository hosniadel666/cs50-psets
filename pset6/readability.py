#!/usr/bin/env python
from cs50 import get_string
import sys

# to calc how many sentance in string


def sentance_count(str):
    counter = 0
    for i in range(0, len(str)):
        if str[i] in("!", "?", "."):
            counter += 1
    return counter

# to count the word in the string


def word_count(str):
    counter = 0
    for i in range(0, len(str)):
        if str[i] == " ":
            counter += 1
    return counter+1

# to count letter in string


def letter_count(str):
    counter = 0
    for i in range(0, len(str)):
        if str[i].isalpha() or str[i].isnumeric():
            counter += 1
    return counter


name = get_string("What's the text?\n")
letter = letter_count(name)
word = word_count(name)
sentance = sentance_count(name)
# sub in Coleman-Liau formula
index = (0.0588 * ((letter / word) * 100) - 0.296 * ((sentance / word) * 100) - 15.8)
y = round(index)

if y < 1:
    print("Before Grade 1")
elif y > 16:
    print("Grade 16+")
else:
    print("Grade ", y)