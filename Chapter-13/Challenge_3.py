class Shape():
	def what_am_i(self):
		print("I am a shape")

class Rectangle(Shape):
	def __init__(self, w, l):
		self.width = w
		self.len = l
		pass
	def calculate_perimeter(self):
		return 2 * (self.len + self.width)

class Square(Shape):
	def __init__(self, s):
		self.side = s
		pass
	def calculate_perimeter(self):
		return 4 * self.side

rectangle = Rectangle(20, 20)
square = Square(29)
rectangle.what_am_i()
square.what_am_i()

