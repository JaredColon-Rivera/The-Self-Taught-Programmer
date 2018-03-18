class Apple():
	def __init__(self, color, size, taste, state):
		self.color = color
		self.size = size
		self.taste = taste
		self.state = state
		print("Apple created!")

first_apple = Apple("red", "large", "sweet", "California")

print(first_apple.color)
print(first_apple.size)
print(first_apple.taste)
print(first_apple.state)