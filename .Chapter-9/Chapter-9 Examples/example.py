st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

with open("st.txt", "r") as f:
	print(f.read())

my_list = list()

with open("st.txt", "r") as f:
	my_list.append(f.read())

print(my_list)