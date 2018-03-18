def main():

	"""
	Takes an input
	and converts it
	into a float number

	"""
	try:
		x = input("Type in a number to be converted to a float: ")
		floatnum = float(x)
		print(floatnum)
	except(ValueError):
		print("Could not convert the string to a float")
	

main()