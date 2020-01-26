# #Class

class Person:
	pass #An empty block

p = Person()
print(p)

#Method

class Person:
	def say_hi(self):
		print('Hello, how are you?')

p = Person()
p.say_hi()

# __init__ method

class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is ', self.name)

p = Person('Swaroop')
p.say_hi()

#-------------------------
class Person:
	def __init__(self, name, age, code, gender):
		self.name = name
		self.age = age
		self.code = code
		self.gender = gender
	def say_hi(self):
		print('my name is ', self.name)
	def say_age(self):
		print('I\'m ', self.age, ' years old')
	def say_code(self):
		print('My code is ', self.code)
	def say_gender(self):
		print('Gender is ', self.gender)
p = Person('John', 12, 123456, 'male')
p.say_hi()
p.say_age()
p.say_code()
p.say_gender()
			