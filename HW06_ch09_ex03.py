#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(inputWord, inputString):
    """ return True if word NOT forbidden"""
    
    # Loop through the inputString and check if inputWord contains any character
    for characters in inputString:
        if(inputWord.find(characters) == -1):
            continue
        else:
            return False

    return True

def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    
    inputString = input("Enter a String of Forbidden Letters: ")
    nCount = forbidden_param(inputString)

    print("Number of Words Not Forbidden By Input: " + str(nCount))

def forbidden_param(inputString):
    """ return count of words NOT forbidden by param"""

    fileObject = open("words.txt", "r")
    nCount = 0

    for words in fileObject:
        if(avoids(words, inputString)):
            nCount += 1

    return nCount

def find_five():

    # initialise a list that would contain the count of excluded words for different letters
    outputList = list()
    
    # loop through letters a - z and count the number of excluded words
    for x in range(97, 123):
        nCount = forbidden_param(chr(x))

        # append to the list if the lenght is less than 5, else replace
        if(len(outputList) < 5):
            outputList.append([nCount, chr(x)])
        else:
            # check if the element should be added to the list
            if(nCount > int(min(outputList)[0])):
                # remove the element with the maximum count
                outputList.sort()
                outputList.pop(0)
                outputList.append([nCount, chr(x)])
        
    # print the letters and the words excluded
    outputList.sort()
    outputString = ""
    # outputString = "".join(outputList)

    for items in outputList:
        outputString += str(items[1])
        print("Forbidden Letters: " + str(items[1]))

    print("Total Number of Words Excluded: " + str(forbidden_param(outputString)))


##############################################################################
def main():
    # Your final submission should only call five_five

    find_five()

if __name__ == '__main__':
    main()
