class Triangle():
	def __init__(self, b, h):
		self.base = b
		self.height = h

	def area(self):
		return (1/2) * self.base * self.height

triangle = Triangle(15, 45)
print(triangle.area())