class Student:
    population = 0
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
        print("My name is : {}".format(self.name))

        Student.population += 1

    def tell(self):
        print("Name : {}, Age : {}, Subject : {}".format(self.name, self.age, self.subject))

    def transfer(self):
        print("The student '{}' is transferred".format(self.name))
        Student.population -= 1

    @classmethod
    def howmany(cls):
        print("Total number of student is {:d}".format(cls.population))


student1 = Student("Smith", 12, "Bio")
student2 = Student("John", 10, "Eco")
student3 = Student("Mary", 11, "Math")
print()

student1.tell()
student1.howmany()
print()

student2.tell()
student2.howmany()
print()

student3.tell()
student3.transfer()

student3.howmany()
