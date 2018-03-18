list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
guess_q = "What number is in the list?: "
while True:
	print("Input q to quit")
	guess = input(guess_q)
	if guess == "q":
		print("Goodbye")
		break
	try:
		guess = int(guess)
	except ValueError:
		print("please type a number or q to quit")
	if guess in list_num:
		print("You got it right! {} was in the list".format(guess))
		break
	else:
		print("WRONG")
