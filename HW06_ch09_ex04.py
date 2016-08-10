#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports
import random

# Body
def uses_only(inputWord, inputLetters):

	# lowercase both inputs
	inputWord = inputWord.lower()
	inputLetters = inputLetters.lower()

	# OutputList would only get populated if the word is made up of other letters
	outputList = [letter for letter in inputWord if letter not in inputLetters]

	if(len(outputList) >= 1):
		return False
	else:
		return True

def generate_sentence(numSentences):

	# open the file
	fileObject = open("words.txt", "r")

	# generate an empty list to hold the words that pass the uses_only function
	listWords = list()

	for words in fileObject:
		if(uses_only(words.strip(), "acefhlo")):
			listWords.append(words.strip())

	# store the last index of the list in a variable
	lenListWords = len(listWords) - 1

	# create a random number between 3 - 10 that decides the lenght of the sentence
	lenSentence = random.randint(3, 10)

	# randomly pull words from listWords and form sentences
	for x in range(numSentences):
		outputSentence = ''
		for y in range(lenSentence):
			# Generate a random number to fetch a random word from the list
			randNum = random.randint(0, lenListWords)
			outputSentence = outputSentence + " " + listWords[int(randNum)]

		print("Sentence #" + str(int(x)) + ": " + str(outputSentence))

##############################################################################
def main():
    
    num = int(input("How Many Sentences To Be Formed? "))

    generate_sentence(num)

if __name__ == '__main__':
    main()
