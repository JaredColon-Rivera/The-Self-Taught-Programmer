class Horse():
	def __init__(self, name, size, rider):
		self.name = name
		self.size = size
		self.rider = rider

class Person():
	def __init__(self, name, horse):
		self.name = name
		self.horse = horse


apollo = Horse("Apollo 13", "Large", ["none", "balls"])
bruce = Person("Bruce Willis", apollo)

print(bruce.horse.name)
print(apollo.rider[1])