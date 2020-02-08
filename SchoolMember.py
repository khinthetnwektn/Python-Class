#Inheritance

class SchoolMember:
	''' Represents any school member. '''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self.name))

	def tell(self):
		''' Tell my details '''
		print('Name: "{}" Age: "{}" '.format(self.name, self.age), end="")


class Teacher(SchoolMember):
	'''Represents a student. '''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Teacher: {})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks : "{:d}"'.format(self.marks))


class Student(SchoolMember):
	'''Represents a student'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student: {}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))


class Headmaster(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self.name, self.age)
		self.marks = marks
		print("Initialized Headmaster : {}".format(self.name))

	def tell(self):
		print("Headmaster Name : {}, Age : {}, Marks : {:d}".format(self.name, self.age, self.marks))



h = Headmaster("Mr. John", 50, 20)
t = Teacher('Mrs. Shrivida', 40, 30000)
s = Student('Swroop', 25, 75)

print()

members = [t,s]
for member in members:
	member.tell()