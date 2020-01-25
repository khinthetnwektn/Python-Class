#keyboardInterrupt

while True:
	try:
		x = int(input("Please enter a number: "))
		print(x)
		break
	except ValueError:
		print("Oops! That was no valid number. Try again...")


#--------------------------------------

#OSError, ValueError

import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())

except OSError as err:
	print("OS error: {0}".format(err))
except ValueError:
	print("Could not convert data to an integer.")
except:
	print("Unexcepted error:", sys.exc_info()[0])
	raise

#------------------------------------

#EOFError, KeyborardIntepruter

try:
	text = input('Enter something--> ')
except EOFError:
	print('Why did you do an EOF on me? ')
except KeyboardInterrupt:
	print('You cancel the operation. ')
else:
	print('You entered . {}'.format(text))


# Raise Exceptions

class ShortInputException(Exception):

	''' A use-defined exception class. '''

	def __init__(self, length, atlease):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

	try:
		text = input('Enter something--> ')

		if len(e=text) < 3:
			raise ShortInputException(len(text),3)
			#Other work can continue as usual here
			
		except EOFError:
			print('Why did you do an EOF on me?')

		except ShortInputException as ex:
			print(('ShortInputException: The input was' + 
				'{0} long, excepted at least{1}')
				.format(ex.length, ex.atleast))		
		else:
			print('No exception was raised. ')