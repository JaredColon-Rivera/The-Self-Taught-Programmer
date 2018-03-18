# Encapsulation

class Rectangle():
	def __init__(self, w, l):
		self.width = w
		self.len = l

	def area(self):
		return self.width * self.len

class Data():
	def __init__(self):
		self.nums = [1, 2, 3, 4, 5]


	def change_data(self, index, n):
		self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 200)
print(data_two.nums)

class PublicPrivateExample:
	def __init__(self):
		self.public = "safe"
		self._unsafe = "unsafe"

	def public_method(self):
		# clients can use this
		pass

	def _unsafe_method(self):
		# clients shouldn't use this
		pass
