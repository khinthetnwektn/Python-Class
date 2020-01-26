#Class And Object Variables

class Robot:
	""" Represent a robot, with a name. """

	population = 0

	def __init__(self, name):
		""" Initializes the data """

		self.name = name
		print("(Initializing {})".format(self.name))

		Robot.population += 1

	def die(self):
		""" I'm dying """

		print("{} is being destroyed! ".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print("{} was the last one. ".format(self.name))
		else:
			print("There are still {:d} robots working. ".format(Robot.population))

	def say_hi(self):
		""" Greeting by the robot.
		Yeah, they can do that. """

		print("Greetings, my sisters call me {}. ".format(self.name))


	@classmethod
	def how_many(cls):
		""" Prints the current population."""
		print("We have {:d} robots.".format(cls.population))


dorid1 = Robot("R2-D2")
dorid1.say_hi()
dorid1.how_many()

print()

dorid2 = Robot('C-3P0')
dorid2.say_hi()
dorid2.how_many()

print()

dorid3 = Robot('Q35')
dorid3.say_hi()
dorid3.how_many()

print()

dorid4 = Robot('RP2')
dorid4.say_hi()
dorid4.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. so let's destroy them")

dorid1.die()
dorid2.die()
dorid3.die()
dorid4.die()

Robot.how_many()



#********** String Formatino ************

d - for integers
b - for floating point number
o - for octal number
x - for octal hexadecimal numbers
s - for string
f - for floating
e - for floating


for x in range(1, 11):
	print('{0:1d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))