# Imports
import os

def main():
	print("Current Working Directory: " + str(os.getcwd()) + "\n")
	os.chdir("/Users/arnavgoyal/Documents/Berkeley/Fall 2016/Python Boot Camp/D05")

	print("List of Files in New Directory")
	print(os.listdir(os.getcwd()))

if __name__ == "__main__":
	main()
