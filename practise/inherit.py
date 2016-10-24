#!/usr/bin/python
# Filename: inherit.py

class SchoolMember:
	'''Represents any school member'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("Initialized SchoolMember: %s") % self.name

	def tell(self):
		'''Tell my details.'''
		print("Name:\"%s\" Age:\"%d\"") % (self.name, self.age)

class Teacher(SchoolMember):
	'''Represents a teacher'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print("Initialized Teacher: %s") % self.name

	def tell(self):
		SchoolMember.tell(self)
		print("Salary: %d") % self.salary

class Student(SchoolMember):
	'''Represents a student'''
	def __init__(self, name, age, mark):
		SchoolMember.__init__(self, name, age)
		self.mark = mark
		print("Initialized Student: %s") % self.name

	def tell(self):
		SchoolMember.tell(self)
		print("Mark: %d") % self.mark

t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Kyle', 22, 80)

print	# prints a blank line

memebrs = [t, s]
for member in memebrs:
	member.tell()	# works for both Teachers and Students