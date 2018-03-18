class Square():
	def __init__(self, side):
		self.side = side

	def print_size(self):
		print("""{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side))

square = Square(29)
square.print_size()
