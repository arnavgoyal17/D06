""" Print 10 Random Numbers to a File """

# Imports
import random

# Body

def write_numbers(fileName):

	fileObject = open(fileName + ".txt", "w")

	for n in range(9):
		fileObject.write(str(random.randint(1, 10000)) + "\n")

	fileObject.write(str(random.randint(1, 10000)) + "\n")		

	fileObject.close()

def main():

	usrInput = input("Enter Name of the File to be Created: ")
	write_numbers(usrInput)

if __name__ == '__main__':
	main()