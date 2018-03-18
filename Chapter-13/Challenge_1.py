class Rectangle():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def calculate_perimeter(self):
		return 2 * (self.len + self.width)

rectangle = Rectangle(5, 4)
print(rectangle.calculate_perimeter())

class Square():
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return 4 * self.side

square = Square(4)
print(square.calculate_perimeter())