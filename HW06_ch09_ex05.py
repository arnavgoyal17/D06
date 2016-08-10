#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(inputString, inputLetters):
	for letter in inputLetters:
		if(inputString.find(letter) == -1):
			return False

	return True

def uses_aeiou(fileObject):

	nCount = 0
	for words in fileObject:
		if(uses_all(words.strip(), "aeiou")):
			nCount += 1

	fileObject.close()

	return nCount

def uses_aeiouy(fileObject):

	nCount = 0
	for words in fileObject:
		if(uses_all(words.strip(), "aeiouy")):
			nCount += 1

	fileObject.close()		

	return nCount	

##############################################################################
def main():
    
    fileObject = open("words.txt", "r")
    print("# of words that use all aeiou: " + str(uses_aeiou(fileObject)) + "\n")

    fileObject = open("words.txt", "r")
    print("# of words that use all aeiouy: " + str(uses_aeiouy(fileObject)))

if __name__ == '__main__':
    main()
