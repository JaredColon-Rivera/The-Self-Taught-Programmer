import math

class Circle():
	def __init__(self, r):
		self.radius = r

	def area(self):
		return math.pi * (self.radius * self.radius)

circle = Circle(5)
print(circle.area())

