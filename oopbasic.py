# oopbasic.py

class Student:

	def __init__(self,name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

	def study(self):
		print(f'{self.name} is studying...')

	def sawatdee(self):
		if self.gender == 'Male':
			tail = 'kub'
			callme = 'Mr.'
		else:
			tail = 'ka'
			callme = 'Ms.'
		print(f'Hello {tail} I am {callme} {self.name}') # kub ka

#Overide
class SpecialStudent(Student):

	def __init__(self,name,age,gender,parent):
		super().__init__(name,age,gender)
		self.parent = parent

	def hello(self, person='friend'):
		if person == 'friend':
			print ('What up man')
		else:
			print ('Go go')

	def sawatdee(self):
		print(f'Hi there, I am {self.name}')

	def myfather(self):
		print('Do you know who I am?')
		print(f'My father is {self.parent}')

class Teacher: 

	def __init__(self,name,gender,subject):
		self.name = name
		self.gender = gender
		self.subject = subject

	def teach(self):
		print('Teacher {} is teaching {}'.format(self.name,self.subject))

if __name__ == '__main__':
	student1 = Student('Adam',14,'Male')
	student2 = Student('Ariana',14,'Female')
	special_student = SpecialStudent('Arniyo',16,'Male','Biden')

	teacher1 = Teacher('John','Male','English')
	print(teacher1.name)
	print(teacher1.subject)

	print('---8.30 am---')
	student1.sawatdee()
	student2.sawatdee()
	teacher1.teach()
	student1.study()
	student2.study()
	print('---8.45 am---')
	special_student.sawatdee()
	print('Walking to table')
	special_student.hello()
	print(f'Hi Teacher {teacher1.name}, I need a good grade')
	special_student.myfather()


