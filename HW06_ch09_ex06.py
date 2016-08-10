#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words: 596
##############################################################################
# Imports

# Body
def is_abecedarian(inputString):

	# convert the input to a list
	inputList = list(inputString)

	# stored the sorted list in a new variable
	sortedList = sorted(inputList)

	if(sortedList == inputList):
		return True
	else:
		return False

def count_abecedarian():
	fileObject = open("words.txt", "r")
	nCount = 0
	for words in fileObject:
		if(is_abecedarian(words.strip())):
			nCount += 1

	return nCount

##############################################################################
def main():
    print("# of abecedarian words: " + str(count_abecedarian()))

if __name__ == '__main__':
    main()
