class dog:
	def __init__(self, name):
		self.name = name
		print('Dog\'s name ', self.name)

	def color(self, color):
		self.color = color
		print('Dog\'s color ', self.color)

	def owner(self, owner):
		self.owner = owner
		print('Dog\'s owner ', self.owner)

	def age(self, age):
		self.age = age
		print('Dog\'s age ', self.age)

	def bark(self):
		print("wote wote")

	def eat(self):
		print('Eat cookie')

	def sleep(self):
		print('Time to slee')

	def bite(self):
		print('It bites')


dog1 = dog('Aung Net')
dog1.color('Black')
dog1.owner('U Kaung')
dog1.age(2)

print()

dog2 = dog('Rosie')
dog2.color('Gold')
dog2.owner('Jucy')
dog2.age(1)
