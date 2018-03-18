q = input("What is your favorite color?: ")

with open("color.txt", "w") as f:
	f.write("Favorite color: " + q)
