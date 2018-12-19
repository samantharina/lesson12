print('-'*65)
print('Narrative Bot')
print()
name = input ('Student Name: ')
grade = input('Grade: ')

grade = int(grade)

if grade >= 65:
	print(name + 'your final grade in AP Computer Science is a' + grade + '%.' )
	print('You have excelled in all components of the class!')
	print('Good luck in your continued success in the next semester.')

else: 
	print(name + 'your final grade in AP Computer Science is a' + grade + '%' )
	print('This is largely a result of you missing assignments and class.')
	print('Unfortunately, because of this grade, you will have to complete an MBA next semester.')


print ('-'*65)