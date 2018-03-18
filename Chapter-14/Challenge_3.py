def compare(name, other_name):
	if name is other_name:
		print("They are the same!")
	else:
		print("They are not the same!")

compare("Jared", "Carl")

def compare(obj1, obj2):
	return obj1 is obj2

print(compare("a", "b"))