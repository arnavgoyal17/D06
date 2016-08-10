def has_e(inputString):
	if(inputString.lower().find("e") == -1):
		return False
	else:
		return True

def find_names():
	fileObject = open("roster.txt", "r")
	nCount = 0

	writeFile = open("roster_e.txt", "w")

	for lines in fileObject:
		name = lines.split()[0]
		if(has_e(name)):
			nCount += 1
			writeFile.write(str(name) + "\n")

	writeFile.write(str(nCount))

def main():

	find_names()

if __name__ == '__main__':
	main()