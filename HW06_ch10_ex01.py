# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# Imports

# Body
def nested_sum(inputList):

	# define variables to be used
	sumList = 0

	# loop through all the elements in the list
	for element in inputList:
		# check if the element is a list, if it is a list, call the same function again with the element as the parameter
		if(type(element) == list):
			sumList = sumList + nested_sum(element)
		else:
			sumList = sumList + float(element)

	return sumList

def main():

	l1 = [1,2,3,4,5,6]
	print(str(nested_sum(l1)) + "\n")

	l2 = [[1,2,3,4], 5, 6, [7,[8,[9,[10]]]]]
	print(nested_sum(l2))

if __name__ == '__main__':
	main()