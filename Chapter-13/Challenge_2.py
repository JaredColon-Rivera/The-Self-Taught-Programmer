class Square():
	def __init__(self, s):
		self.side = s

	def calculate_perimeter(self):
		return 4 * self.side

	def change_size(self, new_size):
		self.side += new_size

square = Square(100)
print(square.calculate_perimeter())
square.change_size(200)
print(square.calculate_perimeter())
