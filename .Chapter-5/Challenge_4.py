my_stats = {
			"height" : [],
			"color" : [],
			"author" : []
			}


def main():
	height = input("What is your height?: ")
	color = input("What is your favorite color?: ")
	author = input("Who is your favorite author?: ")
	my_stats["height"].append(height)
	my_stats["color"].append(color)
	my_stats["author"].append(author)

main()

print(my_stats)