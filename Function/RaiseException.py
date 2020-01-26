# Raise Exceptions

class LongInputException(Exception):

	''' A use-defined exception class. '''

	def __init__(self, length, atmost):
		Exception.__init__(self)
		self.length = length
		self.atmost = atmost

class ShortInputException(Exception):

	''' A use-defined exception class. '''

	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something--> ')

	if len(text) < 3:
		raise ShortInputException(len(text), 3)
		#Other work can continue as usual here

	elif len(text) > 10:
		raise LongInputException(len(text), 10)
		
except EOFError:
	print('Why did you do an EOF on me?')

except LongInputException as Lex:
	print(('LongInputException: The input was' + 
		' {0} long, excepted at most {1}')
		.format(Lex.length, Lex.atmost))

except ShortInputException as ex:
	print(('ShortInputException: The input was' + 
		' {0} long, excepted at least {1}')
		.format(ex.length, ex.atleast))

else:
	print('No exception was raised. ')


#--------------------------------------
import time

f = None
try:
	f = open("poem.txt")

	#Our usual file-reading idiom

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line, end=' ')
		sys.stdout.flush()
		print("Press ctrl+c now")

		#To make sure it runs for a while

		time.sleep(2)

except IOError:
	print('Could not find file poem.txt')

except KeyboardInerrupt:
	print('!! You cancelled the reading from the file.')

finally:
	if f:
		f.close()
	print("(Cleaning up : Closed the file)")