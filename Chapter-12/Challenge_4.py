class Hexagon():
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return 6 * self.side


hexagon = Hexagon(655)
print(hexagon.calculate_perimeter())