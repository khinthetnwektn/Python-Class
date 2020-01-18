# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - text

# "b" - Binary

#------------------------------------------

#open & Read File
# f = open('test.txt', 'r')  #R - Read

# print(f.name)

# f.close()
#------------------------------------------

# with open('test1.txt', 'a') as g:

# 	g.write('This is line number 8' + "\n")

# 	print(g, end=" ")

#------------------------------------------
with open("test.txt", 'r') as f:

	# f_text = f.readline()  #read each line in file
	# print(f_text, end='')

	# f_text = f.readline()
	# print(f_text, end='')

	# for line in f:
	# 	print(line, end='')

	# f_text = f.read(60)  #read characters in file
	# print(f_text, sep=',')

	size_to_read = 10
	f_text = f.read(size_to_read)

	length = len(f_text)
	while length > 0:
		print(f_text, end='')
		length -= 1