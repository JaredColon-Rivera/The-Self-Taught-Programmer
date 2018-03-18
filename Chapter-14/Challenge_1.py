class Square():
	square_list = []

	def __init__(self, side):
		self.side = side
		self.square_list.append(self.side)

s1 = Square(1)
s2 = Square(4)
s3 = Square(10)

print(Square.square_list)