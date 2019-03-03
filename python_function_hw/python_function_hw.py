#!/bin/python3
import os
import sys
import random
import string

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

#!sys.argv[1] = 'C:/Users/DellHome/Downloads/dict.txt'
word_array = open(sys.argv[1]).read().split("\n")

random_word = random.choice(word_array).upper()

word_to_show = '_ '*len(random_word)
print (word_to_show)

word_len = len(random_word)

while word_len>0:
    pos = 0
    letter = input("Please enter the letter: ").upper()[0:1]

    if letter in word_to_show[pos:]:
        pos = 1
    else:
        while letter in random_word[pos:]:
            pos = random_word.index(letter, pos)
            word_to_show = change_char(word_to_show,pos*2, letter )
            word_len = word_len -1
            pos = pos + 1

    if pos > 0:
        print('There is the letter "' + letter +'" in this word!')
        print(word_to_show)

    else:
        print('No luck, the letter "' + letter + '" is not in this word. Try again')
